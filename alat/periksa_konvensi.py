#!/usr/bin/env python3
"""Pemeriksa dokumen Konvensi Artup.

Memeriksa dokumen konvensi (bukan berkas transkripsi) terhadap:

- aturan format Bagian 4.1 [F-1] sampai [F-7];
- frontmatter YAML yang valid dan konsisten dengan tabel identitas;
- blok kode (fence) yang seimbang;
- kode aturan yang tidak ganda dan tanpa lompatan penomoran;
- rujukan kode aturan, "Bagian n.n", dan "Lampiran X" yang benar-benar ada;
- daftar isi yang sesuai dengan heading;
- JSON Schema frontmatter di lampiran yang valid dan selaras dengan tabel isian Bagian 9.3 dan 9.4;
- contoh uji di lampiran: berkas dasar lolos dan setiap kasus menghasilkan temuan yang ditetapkan,
  sejauh dapat dinilai alat ini (format byte, JSON Schema, [I-4], dan [M-8]).

Dengan ``--gaya``, ditambah heuristik yang temuannya tidak memblokir pull request: satu kalimat per baris,
kata kunci normatif di luar ketentuan berkode, dan ketentuan berkode tanpa kata kunci
(kecuali kelompok P, yang berupa pernyataan prinsip).

Keluaran per baris berformat ``berkas:baris: [kode] pesan``.
Kode keluar: 0 bila bersih, 1 bila ada temuan, 2 bila berkas tidak dapat dibaca.

Penulis: Claude (Claude Opus 5.5, model AI buatan Anthropic), atas permintaan
dan di bawah arahan Ananda Putra, 2026-10-26.

Sumber: ditulis baru untuk proyek ini; tidak ada kode yang disalin dari skrip
atau proyek lain. Pustaka luar yang dipakai sebagai dependensi biasa adalah
PyYAML (pyyaml.org) dan jsonschema (python-jsonschema.readthedocs.io). Aturan yang diperiksa diambil dari dokumen Konvensi
Artup sendiri; pengenalan heading ATX dan blok kode berpagar mengikuti
CommonMark Spec 0.31.2 (spec.commonmark.org), Bagian 4.2 dan 4.5.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError

AKAR = Path(__file__).resolve().parent.parent
DOKUMEN_KERJA = AKAR / "konvensi" / "konvensi-artup.md"
FOLDER_RILIS = AKAR / "rilis"

AWALAN_KODE = "PFCSNKMIVRL"
RE_KODE = re.compile(rf"(?<![\w-])([{AWALAN_KODE}])-(\d+)(?![\w-])")
RE_RENTANG = re.compile(
    rf"(?<![\w-])([{AWALAN_KODE}])-(\d+)\]?\s+(?:s\.d\.|sampai(?: dengan)?)\s+\[?([{AWALAN_KODE}])-(\d+)(?![\w-])"
)
RE_DEFINISI = re.compile(rf"^(?:- )?\[([{AWALAN_KODE}])-(\d+)\]")
RE_DIHAPUS = re.compile(r"^\s*dihapus\b", re.IGNORECASE)
RE_BAGIAN = re.compile(r"\bBagian\s+(\d+(?:\.\d+)*)(?![\d])")
RE_LAMPIRAN = re.compile(r"\bLampiran\s+([A-Z])(?![\w])")
RE_HEADING = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+#+)?[ \t]*$")
RE_HEADING_BERNOMOR = re.compile(r"^(\d+(?:\.\d+)*)\.\s+(.+)$")
RE_HEADING_LAMPIRAN = re.compile(r"\bLampiran\s+([A-Z])\b")
RE_FENCE = re.compile(r"^( {0,3})(`{3,}|~{3,})(.*)$")
RE_KODE_SEBARIS = re.compile(r"(`+)(.+?)\1")
RE_SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
RE_SHA256 = re.compile(r"^[0-9a-f]{64}$")

# Angka Romawi yang lazim dipakai sebagai nomor Lampiran peraturan, misalnya "Lampiran I".
HURUF_ROMAWI = {"I", "V", "X"}

ISIAN_FRONTMATTER_WAJIB = ("id", "nama", "judul", "versi", "status", "tanggal")
NILAI_STATUS = ("draf", "final")

# Tabel isian frontmatter berkas transkripsi (Bagian 9.3 dan 9.4) dan padanan tipenya di JSON Schema.
KEPALA_TABEL_ISIAN = "| Isian | Wajib | Tipe | Keterangan |"
KEPALA_TABEL_VERIFIKASI = "| Isian | Wajib | Keterangan |"
TIPE_SKEMA = {"string": "string", "bilangan": "integer", "objek": "object", "daftar": "array"}
REF_TANGGAL = "#/$defs/tanggal"

# Pemeriksaan berkas transkripsi (Bagian 12) yang dapat dinilai alat ini pada contoh uji.
DAPAT_DINILAI = {"L-01", "L-02", "L-03", "L-04", "L-05", "L-19", "L-22"}
PETA_FORMAT = {"F-1": "L-01", "F-2": "L-02", "F-3": "L-03", "F-4": "L-04", "F-5": "L-04", "F-6": "L-04", "F-7": "L-04"}
HASIL_KASUS = ("sesuai", "galat", "peringatan")

# Kata kunci normatif Bagian 2.1, dan kelompok kode yang ketentuannya berupa pernyataan.
RE_KATA_KUNCI = re.compile(r"(?<![\w-])(?:WAJIB|TIDAK BOLEH|SEBAIKNYA(?: TIDAK)?|BOLEH)(?![\w-])")
RE_KUTIPAN = re.compile(r"\"[^\"]*\"|“[^”]*”")
KELOMPOK_TANPA_KATA_KUNCI = "PL"

# Singkatan yang titiknya bukan akhir kalimat.
RE_SINGKATAN = re.compile(r"\b(?:s\.d|dll|dsb|dst|dkk|No|hlm|mis|yth|a\.n|u\.p)\.$")


@dataclass
class Temuan:
    berkas: str
    baris: int
    kode: str
    pesan: str

    def __str__(self) -> str:
        return f"{self.berkas}:{self.baris}: [{self.kode}] {self.pesan}"


@dataclass
class Dokumen:
    nama: str
    baris: list[str]
    awal_badan: int = 0
    frontmatter: dict | None = None
    dalam_kode: list[bool] = field(default_factory=list)


class Pemeriksa:
    def __init__(self, nama: str, gaya: bool = False):
        self.nama = nama
        self.gaya = gaya
        self.temuan: list[Temuan] = []
        self.definisi: dict[str, int] = {}
        self.tingkat: dict[str, str] = {}

    def lapor(self, baris: int, kode: str, pesan: str) -> None:
        self.temuan.append(Temuan(self.nama, baris, kode, pesan))

    # -- Format Bagian 4.1 -------------------------------------------------

    def periksa_byte(self, data: bytes) -> str | None:
        if data.startswith(b"\xef\xbb\xbf"):
            self.lapor(1, "F-1", "berkas diawali BOM")
            data = data[3:]
        try:
            teks = data.decode("utf-8")
        except UnicodeDecodeError as e:
            self.lapor(data.count(b"\n", 0, e.start) + 1, "F-1", f"bukan UTF-8 yang valid: {e.reason}")
            return None

        baris = teks.split("\n")
        if teks.endswith("\n"):
            baris.pop()
        kosong_sebelumnya = False
        for i, b in enumerate(baris, 1):
            if "\r" in b:
                self.lapor(i, "F-2", "memuat CR (U+000D)")
                b = b.replace("\r", "")
            if not unicodedata.is_normalized("NFC", b):
                self.lapor(i, "F-3", "teks tidak dalam bentuk NFC")
            if "\t" in b:
                self.lapor(i, "F-4", "memuat karakter tab")
            if b != b.rstrip(" \t"):
                self.lapor(i, "F-5", "baris diakhiri spasi")
            kosong = b.strip(" \t") == ""
            if kosong and kosong_sebelumnya:
                self.lapor(i, "F-7", "baris kosong berturut-turut")
            kosong_sebelumnya = kosong

        if not teks.endswith("\n"):
            self.lapor(max(len(baris), 1), "F-6", "berkas tidak diakhiri LF")
        elif teks.endswith("\n\n") or teks == "\n":
            self.lapor(len(baris), "F-6", "berkas diakhiri lebih dari satu LF")
        return teks.replace("\r", "")

    # -- Frontmatter -------------------------------------------------------

    def periksa_frontmatter(self, dok: Dokumen) -> None:
        if not dok.baris or dok.baris[0] != "---":
            self.lapor(1, "frontmatter", "dokumen tidak diawali frontmatter '---'")
            return
        try:
            tutup = dok.baris.index("---", 1)
        except ValueError:
            self.lapor(1, "frontmatter", "frontmatter tidak ditutup dengan '---'")
            return
        dok.awal_badan = tutup + 1
        try:
            isi = yaml.safe_load("\n".join(dok.baris[1:tutup]))
        except yaml.YAMLError as e:
            tanda = getattr(e, "problem_mark", None)
            baris = tanda.line + 2 if tanda else 1
            self.lapor(baris, "frontmatter", f"YAML tidak valid: {getattr(e, 'problem', e)}")
            return
        if not isinstance(isi, dict):
            self.lapor(1, "frontmatter", "frontmatter bukan pemetaan YAML")
            return
        dok.frontmatter = isi

        for kunci in ISIAN_FRONTMATTER_WAJIB:
            if kunci not in isi or isi[kunci] in (None, ""):
                self.lapor(1, "frontmatter", f"isian '{kunci}' tidak ada atau kosong")
        versi = isi.get("versi")
        if versi is not None and not (isinstance(versi, str) and RE_SEMVER.match(versi)):
            self.lapor(self.baris_isian(dok, "versi"), "R-1", f"versi '{versi}' bukan MAYOR.MINOR.PATCH")
        status = isi.get("status")
        if status is not None and status not in NILAI_STATUS:
            self.lapor(self.baris_isian(dok, "status"), "frontmatter",
                       f"status '{status}' bukan salah satu dari {', '.join(NILAI_STATUS)}")
        tanggal = isi.get("tanggal")
        if tanggal is not None and not isinstance(tanggal, datetime.date):
            self.lapor(self.baris_isian(dok, "tanggal"), "frontmatter", f"tanggal '{tanggal}' bukan YYYY-MM-DD")

    @staticmethod
    def baris_isian(dok: Dokumen, kunci: str) -> int:
        for i in range(1, max(dok.awal_badan, 1)):
            if dok.baris[i].startswith(f"{kunci}:"):
                return i + 1
        return 1

    def periksa_identitas(self, dok: Dokumen, bagian: list[tuple[int, int, str]]) -> None:
        """Mencocokkan frontmatter dengan tabel identitas, status, dan riwayat perubahan."""
        fm = dok.frontmatter
        if not fm:
            return
        versi = str(fm.get("versi", ""))
        status = str(fm.get("status", ""))
        tanggal = str(fm.get("tanggal", ""))
        akhir_pembuka = bagian[0][0] - 1 if bagian else len(dok.baris)

        tabel = {}
        for i in range(dok.awal_badan, akhir_pembuka):
            m = re.match(r"^\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|$", dok.baris[i])
            if m:
                tabel.setdefault(m.group(1), (i + 1, m.group(2)))
        harapan = {"Versi": versi, "Status": status, "Tanggal": tanggal}
        for kunci, nilai in harapan.items():
            if kunci not in tabel:
                self.lapor(dok.awal_badan + 1, "identitas", f"tabel identitas tidak memuat baris '{kunci}'")
            elif tabel[kunci][1].lower() != nilai.lower():
                self.lapor(tabel[kunci][0], "identitas",
                           f"{kunci} '{tabel[kunci][1]}' berbeda dengan frontmatter '{nilai}'")
        pengenal = str(fm.get("id", ""))
        if "Pengenal" in tabel and tabel["Pengenal"][1].strip("`") != pengenal:
            self.lapor(tabel["Pengenal"][0], "R-7",
                       f"Pengenal '{tabel['Pengenal'][1]}' berbeda dengan id frontmatter '{pengenal}'")
        rujukan = next((v for k, v in tabel.items() if k.startswith("Rujukan singkat")), None)
        if rujukan and RE_SEMVER.match(versi):
            mayor_minor = ".".join(versi.split(".")[:2])
            m = re.search(r"`([^`/]+)/(\d+\.\d+)`", rujukan[1])
            if not m:
                self.lapor(rujukan[0], "R-1", "rujukan singkat bukan `pengenal/MAYOR.MINOR`")
            else:
                if m.group(1) != pengenal:
                    self.lapor(rujukan[0], "R-7",
                               f"pengenal teknis '{m.group(1)}' berbeda dengan id frontmatter '{pengenal}'")
                if m.group(2) != mayor_minor:
                    self.lapor(rujukan[0], "R-1",
                               f"rujukan singkat tidak sama dengan {pengenal}/{mayor_minor}")

        for i in range(dok.awal_badan, akhir_pembuka):
            m = re.search(r"berstatus \*\*(\w+)\*\*", dok.baris[i])
            if m and m.group(1).lower() != status.lower():
                self.lapor(i + 1, "identitas", f"'Status Dokumen Ini' menyebut '{m.group(1)}', frontmatter '{status}'")

        riwayat = next((b for b in bagian if "Riwayat Perubahan" in b[2]), None)
        if riwayat is None:
            self.lapor(1, "identitas", "tidak ada bagian Riwayat Perubahan")
            return
        versi_riwayat = []
        for i in range(riwayat[0], len(dok.baris)):
            if dok.dalam_kode[i]:
                continue
            if RE_HEADING.match(dok.baris[i]) and i != riwayat[0] - 1:
                break
            m = re.match(r"^\|\s*(\d+\.\d+\.\d+)\s*\|\s*([^|]*?)\s*\|", dok.baris[i])
            if m:
                versi_riwayat.append((i + 1, m.group(1), m.group(2)))
        cocok = [r for r in versi_riwayat if r[1] == versi]
        if not cocok:
            self.lapor(riwayat[0], "R-2", f"riwayat perubahan tidak memuat versi {versi}")
        elif status == "final" and cocok[0][2] != tanggal:
            self.lapor(cocok[0][0], "identitas", f"tanggal riwayat versi {versi} berbeda dengan frontmatter")

    # -- Blok kode ---------------------------------------------------------

    def tandai_blok_kode(self, dok: Dokumen) -> None:
        dok.dalam_kode = [False] * len(dok.baris)
        pembuka = None  # (baris, karakter, panjang)
        for i in range(dok.awal_badan, len(dok.baris)):
            b = dok.baris[i]
            m = RE_FENCE.match(b)
            if pembuka is None:
                if m and not (m.group(2)[0] == "`" and "`" in m.group(3)):
                    pembuka = (i, m.group(2)[0], len(m.group(2)))
                    dok.dalam_kode[i] = True
                continue
            dok.dalam_kode[i] = True
            if m and m.group(2)[0] == pembuka[1] and len(m.group(2)) >= pembuka[2] and not m.group(3).strip():
                pembuka = None
        if pembuka is not None:
            self.lapor(pembuka[0] + 1, "fence", "blok kode dibuka tetapi tidak ditutup")

    # -- Heading dan daftar isi -------------------------------------------

    def kumpulkan_heading(self, dok: Dokumen) -> list[tuple[int, int, str]]:
        hasil = []
        for i in range(dok.awal_badan, len(dok.baris)):
            if dok.dalam_kode[i]:
                continue
            m = RE_HEADING.match(dok.baris[i])
            if m:
                hasil.append((i + 1, len(m.group(1)), (m.group(2) or "").strip()))
        return hasil

    def periksa_penomoran_bagian(self, heading: list[tuple[int, int, str]]) -> dict[str, int]:
        nomor_bagian: dict[str, int] = {}
        terakhir: list[int] = []
        for baris, tingkat, teks in heading:
            m = RE_HEADING_BERNOMOR.match(teks)
            if not m:
                continue
            nomor = m.group(1)
            angka = [int(x) for x in nomor.split(".")]
            if len(angka) != tingkat - 1:
                self.lapor(baris, "heading", f"nomor bagian {nomor} tidak sesuai tingkat heading {'#' * tingkat}")
            if nomor in nomor_bagian:
                self.lapor(baris, "heading", f"nomor bagian {nomor} ganda (pertama di baris {nomor_bagian[nomor]})")
                continue
            nomor_bagian[nomor] = baris
            induk, ke = angka[:-1], angka[-1]
            if induk != terakhir[: len(induk)] or len(terakhir) < len(induk):
                self.lapor(baris, "heading", f"bagian {nomor} tidak berada di bawah bagian induknya")
            else:
                sebelumnya = terakhir[len(induk)] if len(terakhir) > len(induk) else 0
                if ke != sebelumnya + 1:
                    harap = ".".join(str(x) for x in induk + [sebelumnya + 1])
                    self.lapor(baris, "heading", f"nomor bagian {nomor} tidak berurutan (diharapkan {harap})")
            terakhir = angka
        return nomor_bagian

    def periksa_daftar_isi(self, dok: Dokumen, heading: list[tuple[int, int, str]]) -> None:
        idx = next((k for k, h in enumerate(heading) if h[1] == 2 and h[2] == "Daftar Isi"), None)
        if idx is None:
            self.lapor(dok.awal_badan + 1, "daftar-isi", "tidak ada bagian '## Daftar Isi'")
            return
        mulai = heading[idx][0]
        akhir = heading[idx + 1][0] - 1 if idx + 1 < len(heading) else len(dok.baris)
        isi: list[tuple[int, str, str]] = []
        for i in range(mulai, akhir):
            m = re.match(r"^(\d+(?:\.\d+)*)\.\s+(.+)$", dok.baris[i])
            if m:
                isi.append((i + 1, m.group(1), m.group(2).strip()))
            elif dok.baris[i].strip():
                self.lapor(i + 1, "daftar-isi", "baris daftar isi bukan butir 'N. Judul'")

        tingkat_isi = {n.count(".") for _, n, _ in isi} or {0}
        target = [
            (b, RE_HEADING_BERNOMOR.match(t).group(1), RE_HEADING_BERNOMOR.match(t).group(2))
            for b, _, t in heading
            if RE_HEADING_BERNOMOR.match(t) and RE_HEADING_BERNOMOR.match(t).group(1).count(".") in tingkat_isi
        ]
        peta_isi = {n: (b, j) for b, n, j in isi}
        peta_target = {n: (b, j) for b, n, j in target}
        for n, (b, j) in peta_isi.items():
            if n not in peta_target:
                self.lapor(b, "daftar-isi", f"butir {n} tidak memiliki heading padanan")
            elif peta_target[n][1] != j:
                self.lapor(b, "daftar-isi", f"judul butir {n} '{j}' berbeda dengan heading '{peta_target[n][1]}'")
        for n, (b, j) in peta_target.items():
            if n not in peta_isi:
                self.lapor(b, "daftar-isi", f"heading {n} '{j}' tidak tercantum di daftar isi")
        urutan = [n for _, n, _ in isi if n in peta_target]
        if urutan != [n for _, n, _ in target if n in peta_isi]:
            self.lapor(mulai, "daftar-isi", "urutan daftar isi berbeda dengan urutan heading")

    # -- Kode aturan dan rujukan ------------------------------------------

    def baris_teks(self, dok: Dokumen):
        """Baris badan teks di luar blok kode, dengan kode sebaris dihapus."""
        for i in range(dok.awal_badan, len(dok.baris)):
            if not dok.dalam_kode[i]:
                yield i + 1, RE_KODE_SEBARIS.sub(lambda m: " " * len(m.group(0)), dok.baris[i])

    def periksa_kode_aturan(self, dok: Dokumen, nomor_bagian: dict[str, int],
                            lampiran: dict[str, int]) -> None:
        definisi: dict[str, int] = {}
        dihapus: set[str] = set()
        rujukan: list[tuple[int, str]] = []
        kepala_tabel: list[str] | None = None
        sebelumnya_tabel = False

        for baris, teks in self.baris_teks(dok):
            tabel = teks.startswith("|")
            sel = [s.strip() for s in teks.strip().strip("|").split("|")] if tabel else []
            if tabel and not sebelumnya_tabel:
                kepala_tabel = sel
            sebelumnya_tabel = tabel
            if not tabel:
                kepala_tabel = None

            awal_rujukan = 0
            m = RE_DEFINISI.match(teks)
            kode_def = None
            if m:
                kode_def = f"{m.group(1)}-{m.group(2)}"
                awal_rujukan = m.end()
                if RE_DIHAPUS.match(teks[m.end():]):
                    dihapus.add(kode_def)
            elif tabel and kepala_tabel and kepala_tabel[0] == "Kode" and sel is not kepala_tabel:
                m2 = re.fullmatch(rf"([{AWALAN_KODE}])-(\d+)", sel[0])
                if m2:
                    kode_def = sel[0]
                    if "Tingkat" in kepala_tabel and len(sel) == len(kepala_tabel):
                        self.tingkat[kode_def] = sel[kepala_tabel.index("Tingkat")]
                    awal_rujukan = teks.index(sel[0]) + len(sel[0])
                    if len(sel) > 1 and RE_DIHAPUS.match(sel[1]):
                        dihapus.add(kode_def)
            if kode_def:
                if kode_def in definisi:
                    self.lapor(baris, "kode", f"kode {kode_def} ganda (pertama di baris {definisi[kode_def]})")
                else:
                    definisi[kode_def] = baris

            sisa = teks[awal_rujukan:]
            for r in RE_RENTANG.finditer(sisa):
                if r.group(1) != r.group(3) or int(r.group(2)) >= int(r.group(4)):
                    self.lapor(baris, "rujukan", f"rentang {r.group(0)} tidak sah")
                    continue
                lebar = len(r.group(2))
                for n in range(int(r.group(2)) + 1, int(r.group(4))):
                    rujukan.append((baris, f"{r.group(1)}-{n:0{lebar}d}"))
            for r in RE_KODE.finditer(sisa):
                rujukan.append((baris, f"{r.group(1)}-{r.group(2)}"))

            if not RE_HEADING.match(teks):
                for r in RE_BAGIAN.finditer(teks):
                    if r.group(1) not in nomor_bagian:
                        self.lapor(baris, "rujukan", f"merujuk Bagian {r.group(1)} yang tidak ada")
                for r in RE_LAMPIRAN.finditer(teks):
                    if r.group(1) not in HURUF_ROMAWI and r.group(1) not in lampiran:
                        self.lapor(baris, "rujukan", f"merujuk Lampiran {r.group(1)} yang tidak ada")

        self.definisi = definisi
        for baris, kode in rujukan:
            if kode not in definisi:
                self.lapor(baris, "rujukan", f"merujuk kode {kode} yang tidak didefinisikan")
            elif kode in dihapus:
                self.lapor(baris, "rujukan", f"merujuk kode {kode} yang telah dihapus")

        per_kelompok: dict[str, list[tuple[int, int]]] = {}
        for kode, baris in definisi.items():
            awalan, nomor = kode.split("-")
            per_kelompok.setdefault(awalan, []).append((int(nomor), baris))
        for awalan, daftar in per_kelompok.items():
            ada = {n for n, _ in daftar}
            for n in range(1, max(ada) + 1):
                if n not in ada:
                    berikut = min((b for k, b in daftar if k > n), default=1)
                    lebar = 2 if awalan == "L" else 1
                    self.lapor(berikut, "kode",
                               f"kode {awalan}-{n:0{lebar}d} tidak didefinisikan (lompatan penomoran; "
                               "aturan yang dihapus tetap dicantumkan dengan tanda 'dihapus')")

    # -- Gaya --------------------------------------------------------------

    def periksa_gaya(self, dok: Dokumen) -> None:
        for baris, teks in self.baris_teks(dok):
            if teks.startswith("|") or RE_HEADING.match(teks):
                continue
            for m in re.finditer(r"(\S+)([.!?])\s+(?=[\"(\[]?[A-Z])", teks):
                kata = m.group(1) + m.group(2)
                if RE_SINGKATAN.search(kata) or re.fullmatch(r"[\d.]+", kata) or m.start() == 0 and "-" in kata:
                    continue
                self.lapor(baris, "gaya", "lebih dari satu kalimat pada satu baris")
                break

    def periksa_kata_kunci(self, dok: Dokumen) -> None:
        """Kata kunci normatif di luar ketentuan berkode, dan ketentuan berkode tanpa kata kunci (Bagian 2.1).

        Ketentuan berkode mencakup paragraf atau butir daftar yang diawali kode, baris lanjutannya,
        dan blok berikutnya bila baris sebelumnya diakhiri titik dua, misalnya daftar rincian.
        Tabel, blok kode, kode sebaris, dan teks dalam tanda kutip tidak diperiksa.
        """
        aturan: tuple[int, str, bool, list[str]] | None = None  # (baris, kode, butir daftar, teks)
        ikat = False  # baris sebelumnya bagian dari ketentuan dan diakhiri titik dua
        daftar_terikat = False  # daftar yang sedang berjalan terikat ke ketentuan
        paragraf_baru = True

        def tutup() -> None:
            if aturan is None:
                return
            baris, kode, _, teks = aturan
            isi = " ".join(teks)
            if kode[0] not in KELOMPOK_TANPA_KATA_KUNCI and not RE_DIHAPUS.match(isi) \
                    and not RE_KATA_KUNCI.search(isi):
                self.lapor(baris, "kata-kunci", f"ketentuan [{kode}] tidak memuat kata kunci normatif")

        for i in range(dok.awal_badan, len(dok.baris)):
            if dok.dalam_kode[i] or dok.baris[i].startswith("|"):
                ikat = daftar_terikat = False
                continue
            teks = RE_KODE_SEBARIS.sub(lambda m: " " * len(m.group(0)), dok.baris[i])
            if not teks.strip():
                paragraf_baru = True
                continue
            if RE_HEADING.match(teks):
                tutup()
                aturan, ikat, daftar_terikat, paragraf_baru = None, False, False, True
                continue
            teks = RE_KUTIPAN.sub(" ", teks)
            m = RE_DEFINISI.match(teks)
            butir = teks.startswith("- ")
            if m:
                tutup()
                aturan = (i + 1, f"{m.group(1)}-{m.group(2)}", butir, [teks[m.end():]])
                daftar_terikat = False
            elif aturan is not None:
                if butir and (ikat or daftar_terikat):
                    daftar_terikat = True
                elif paragraf_baru and not ikat or butir and aturan[2]:
                    tutup()
                    aturan = None
                if aturan is not None:
                    aturan[3].append(teks)
            if aturan is None and RE_KATA_KUNCI.search(teks):
                self.lapor(i + 1, "kata-kunci", "kata kunci normatif di luar ketentuan berkode")
            ikat = aturan is not None and teks.rstrip().endswith(":")
            paragraf_baru = False
        tutup()

    # -- JSON Schema frontmatter ------------------------------------------

    def ambil_tabel(self, dok: Dokumen, kepala: str) -> list[tuple[int, list[str]]] | None:
        """Baris data tabel yang diawali kepala tertentu, sebagai (nomor baris, sel), atau None."""
        for i in range(dok.awal_badan, len(dok.baris)):
            if dok.baris[i] == kepala and not dok.dalam_kode[i]:
                hasil = []
                for j in range(i + 2, len(dok.baris)):
                    if not dok.baris[j].startswith("|"):
                        break
                    hasil.append((j + 1, [s.strip() for s in dok.baris[j].strip().strip("|").split("|")]))
                return hasil
        return None

    def ambil_skema(self, dok: Dokumen, mulai: int, akhir: int) -> dict | None:
        """Blok ```json pertama di antara dua nomor baris, diurai dan diperiksa terhadap metaskema."""
        for i in range(mulai, akhir - 1):
            if dok.baris[i].strip() != "```json":
                continue
            isi = []
            for j in range(i + 1, len(dok.baris)):
                if RE_FENCE.match(dok.baris[j]):
                    break
                isi.append(dok.baris[j])
            try:
                skema = json.loads("\n".join(isi))
            except json.JSONDecodeError as e:
                self.lapor(i + 1 + e.lineno, "skema", f"JSON tidak valid: {e.msg}")
                return None
            try:
                Draft202012Validator.check_schema(skema)
            except SchemaError as e:
                self.lapor(i + 1, "skema", f"bukan JSON Schema Draft 2020-12 yang valid: {e.message}")
                return None
            return skema
        self.lapor(mulai, "skema", "lampiran JSON Schema tidak memuat blok ```json")
        return None

    @staticmethod
    def urai_ref(simpul: dict, skema: dict) -> dict:
        while isinstance(simpul, dict) and "$ref" in simpul:
            simpul = skema["$defs"][simpul["$ref"].removeprefix("#/$defs/")]
        return simpul

    def simpul_jalur(self, skema: dict, jalur: str) -> tuple[dict, dict, dict] | None:
        """(induk, simpul mentah, simpul terurai) untuk jalur seperti `sumber[].jenis`; `a[]` masuk ke items."""
        induk, mentah, simpul = None, skema, skema
        for seg in jalur.split(".") if jalur else []:
            daftar = seg.endswith("[]")
            induk = simpul
            mentah = induk.get("properties", {}).get(seg.removesuffix("[]"))
            if mentah is None:
                return None
            simpul = self.urai_ref(mentah, skema)
            if daftar:
                simpul = self.urai_ref(simpul.get("items", {}), skema)
        return induk, mentah, simpul

    def periksa_skema(self, dok: Dokumen, heading: list[tuple[int, int, str]]) -> dict | None:
        tabel_isian = self.ambil_tabel(dok, KEPALA_TABEL_ISIAN)
        if tabel_isian is None:
            return
        idx = next((k for k, h in enumerate(heading) if h[1] == 2 and "JSON Schema" in h[2]), None)
        if idx is None:
            self.lapor(tabel_isian[0][0] - 2, "skema", "tabel isian frontmatter ada, tetapi lampiran JSON Schema tidak ada")
            return
        akhir = next((h[0] for h in heading[idx + 1:] if h[1] <= 2), len(dok.baris) + 1)
        skema = self.ambil_skema(dok, heading[idx][0], akhir)
        if skema is None:
            return None

        baris_tabel = [(b, sel[0].strip("`"), sel[1], sel[2]) for b, sel in tabel_isian]
        for b, sel in self.ambil_tabel(dok, KEPALA_TABEL_VERIFIKASI) or []:
            baris_tabel.append((b, "verifikasi[]." + sel[0].strip("`"), sel[1], None))

        jalur_tabel = {j for _, j, _, _ in baris_tabel}
        for b, jalur, wajib, tipe in baris_tabel:
            ketemu = self.simpul_jalur(skema, jalur)
            if ketemu is None:
                self.lapor(b, "skema", f"isian `{jalur}` tidak ada di JSON Schema")
                continue
            induk, mentah, simpul = ketemu
            nama = jalur.rsplit(".", 1)[-1].removesuffix("[]")
            if (wajib == "WAJIB") != (nama in induk.get("required", [])):
                self.lapor(b, "skema", f"sifat wajib isian `{jalur}` ({wajib}) berbeda dengan `required` di JSON Schema")
            if tipe is None:
                continue
            if tipe == "tanggal":
                cocok = mentah.get("$ref") == REF_TANGGAL
            else:
                cocok = (tipe in TIPE_SKEMA and simpul.get("type") == TIPE_SKEMA[tipe]
                         and mentah.get("$ref") != REF_TANGGAL)
            if not cocok:
                self.lapor(b, "skema", f"tipe isian `{jalur}` ({tipe}) berbeda dengan JSON Schema")

        induk_tabel = {""} | {j.rsplit(".", 1)[0] for j in jalur_tabel if "." in j}
        for induk in sorted(induk_tabel):
            ketemu = self.simpul_jalur(skema, induk)
            if ketemu is None:
                continue
            for nama in ketemu[2].get("properties", {}):
                anak = f"{induk}.{nama}" if induk else nama
                if anak not in jalur_tabel and not any(j.startswith((anak + ".", anak + "[].")) for j in jalur_tabel):
                    self.lapor(tabel_isian[0][0] - 2, "skema", f"isian `{anak}` ada di JSON Schema tetapi tidak ada di tabel")
        return skema

    # -- Contoh uji ---------------------------------------------------------

    @staticmethod
    def ambil_blok(dok: Dokumen, mulai: int, akhir: int, bahasa: str) -> tuple[int, str] | None:
        """(nomor baris pembuka, isi diakhiri LF) blok kode berbahasa tertentu yang pertama di antara dua baris."""
        for i in range(mulai, min(akhir, len(dok.baris))):
            if dok.baris[i].strip() == "```" + bahasa:
                isi = []
                for j in range(i + 1, len(dok.baris)):
                    if dok.baris[j].strip() == "```":
                        break
                    isi.append(dok.baris[j])
                return i + 1, "\n".join(isi) + "\n"
        return None

    def periksa_contoh_uji(self, dok: Dokumen, heading: list[tuple[int, int, str]], skema: dict | None) -> None:
        idx = next((k for k, h in enumerate(heading) if h[1] == 2 and "Contoh Uji" in h[2]), None)
        if idx is None:
            return
        mulai = heading[idx][0]
        akhir = next((h[0] for h in heading[idx + 1:] if h[1] <= 2), len(dok.baris) + 1)
        dasar = self.ambil_blok(dok, mulai, akhir, "markdown")
        kasus = self.ambil_blok(dok, mulai, akhir, "yaml")
        if dasar is None or kasus is None:
            self.lapor(mulai, "contoh-uji", "lampiran contoh uji tidak memuat blok ```markdown dan ```yaml")
            return
        if skema is None:
            self.lapor(mulai, "contoh-uji", "contoh uji tidak dapat dinilai karena JSON Schema tidak tersedia")
            return
        b_dasar, teks_dasar = dasar
        nilai = nilai_berkas_uji(teks_dasar.encode("utf-8"), skema)
        if nilai:
            self.lapor(b_dasar, "contoh-uji", f"berkas dasar menimbulkan temuan {', '.join(sorted(nilai))}")
        b_kasus, teks_kasus = kasus
        try:
            daftar = yaml.safe_load(teks_kasus)
        except yaml.YAMLError as e:
            self.lapor(b_kasus, "contoh-uji", f"daftar kasus bukan YAML yang valid: {getattr(e, 'problem', e)}")
            return
        if not isinstance(daftar, list):
            self.lapor(b_kasus, "contoh-uji", "daftar kasus bukan urutan YAML")
            return
        terlihat: set[str] = set()
        for k in daftar:
            kode = str(k.get("kode")) if isinstance(k, dict) else "?"
            b = next((i + 1 for i in range(b_kasus, len(dok.baris)) if dok.baris[i] == f"- kode: {kode}"), b_kasus)
            if not isinstance(k, dict) or not isinstance(k.get("ganti"), dict):
                self.lapor(b, "contoh-uji", f"kasus {kode} tidak memuat isian `ganti`")
                continue
            if kode in terlihat:
                self.lapor(b, "contoh-uji", f"kode kasus {kode} ganda")
            terlihat.add(kode)
            hasil, pemeriksaan, aturan = k.get("hasil"), k.get("pemeriksaan") or [], k.get("aturan") or []
            if hasil not in HASIL_KASUS:
                self.lapor(b, "contoh-uji", f"kasus {kode}: hasil `{hasil}` bukan salah satu dari {', '.join(HASIL_KASUS)}")
            if (hasil == "sesuai") != (not pemeriksaan):
                self.lapor(b, "contoh-uji", f"kasus {kode}: isian `pemeriksaan` tidak sesuai dengan hasil `{hasil}`")
            for c in [*pemeriksaan, *aturan]:
                if c not in self.definisi:
                    self.lapor(b, "contoh-uji", f"kasus {kode} merujuk kode {c} yang tidak didefinisikan")
                elif c in self.tingkat and self.tingkat[c] != hasil:
                    self.lapor(b, "contoh-uji", f"kasus {kode}: tingkat {c} ({self.tingkat[c]}) berbeda dengan hasil `{hasil}`")
            dari, menjadi = str(k["ganti"].get("dari", "")), str(k["ganti"].get("menjadi", ""))
            jumlah = teks_dasar.count(dari) if dari else 0
            if jumlah != 1:
                self.lapor(b, "contoh-uji", f"kasus {kode}: teks `dari` muncul {jumlah} kali di berkas dasar, bukan tepat satu kali")
                continue
            didapat = nilai_berkas_uji(teks_dasar.replace(dari, menjadi).encode("utf-8"), skema)
            harap = set(pemeriksaan) & DAPAT_DINILAI
            if didapat != harap:
                self.lapor(b, "contoh-uji", f"kasus {kode}: diharapkan {', '.join(sorted(harap)) or 'tanpa temuan'}"
                                            f" untuk pemeriksaan yang dapat dinilai alat ini, didapat {', '.join(sorted(didapat)) or 'tanpa temuan'}")

    # -- Jalankan ----------------------------------------------------------

    def periksa(self, data: bytes) -> list[Temuan]:
        teks = self.periksa_byte(data)
        if teks is None:
            return self.temuan
        baris = teks.split("\n")
        if teks.endswith("\n"):
            baris.pop()
        dok = Dokumen(self.nama, baris)
        self.periksa_frontmatter(dok)
        self.tandai_blok_kode(dok)
        heading = self.kumpulkan_heading(dok)
        nomor_bagian = self.periksa_penomoran_bagian(heading)
        bagian_utama = [h for h in heading if h[1] == 2 and RE_HEADING_BERNOMOR.match(h[2])]
        lampiran = {}
        for b, _, t in bagian_utama:
            m = RE_HEADING_LAMPIRAN.search(t)
            if m:
                lampiran[m.group(1)] = b
        self.periksa_daftar_isi(dok, heading)
        self.periksa_identitas(dok, bagian_utama)
        self.periksa_kode_aturan(dok, nomor_bagian, lampiran)
        skema = self.periksa_skema(dok, heading)
        self.periksa_contoh_uji(dok, heading, skema)
        if self.gaya:
            self.periksa_gaya(dok)
            self.periksa_kata_kunci(dok)
        self.temuan.sort(key=lambda t: t.baris)
        return self.temuan


def tanggal_ke_string(nilai):
    """Meniru skema inti YAML 1.2: tanggal yang diurai PyYAML (YAML 1.1) dikembalikan menjadi string."""
    if isinstance(nilai, dict):
        return {k: tanggal_ke_string(v) for k, v in nilai.items()}
    if isinstance(nilai, list):
        return [tanggal_ke_string(v) for v in nilai]
    if isinstance(nilai, (datetime.date, datetime.datetime)):
        return nilai.isoformat()
    return nilai


def nilai_berkas_uji(data: bytes, skema: dict) -> set[str]:
    """Kode pemeriksaan Bagian 12 yang dilanggar sebuah berkas transkripsi, terbatas pada DAPAT_DINILAI."""
    pemeriksa = Pemeriksa("uji")
    teks = pemeriksa.periksa_byte(data)
    hasil = {PETA_FORMAT[t.kode] for t in pemeriksa.temuan}
    if teks is None:
        return hasil
    baris = teks.split("\n")
    if baris[0] != "---" or "---" not in baris[1:]:
        return hasil | {"L-05"}
    try:
        fm = tanggal_ke_string(yaml.safe_load("\n".join(baris[1:baris.index("---", 1)])))
    except yaml.YAMLError:
        return hasil | {"L-05"}
    if not Draft202012Validator(skema).is_valid(fm):
        hasil.add("L-05")
    if isinstance(fm, dict) and isinstance(fm.get("karya"), dict) and isinstance(fm.get("ekspresi"), dict):
        karya, ekspresi = fm["karya"], fm["ekspresi"]
        if ekspresi.get("id") != f"{karya.get('id')}/{ekspresi.get('bahasa')}@{ekspresi.get('tanggal')}":
            hasil.add("L-19")
        sumber = fm.get("sumber") if isinstance(fm.get("sumber"), list) else []
        gabungan = {c for s in sumber if isinstance(s, dict) for c in (s.get("komponen") or [])}
        if gabungan != set(ekspresi.get("komponen") or []):
            hasil.add("L-22")
    return hasil


def periksa_berkas(jalur: Path, nama: str | None = None, gaya: bool = False,
                   hanya_format: bool = False) -> list[Temuan]:
    pemeriksa = Pemeriksa(nama or str(jalur), gaya=gaya)
    data = jalur.read_bytes()
    if hanya_format:
        pemeriksa.periksa_byte(data)
        return pemeriksa.temuan
    return pemeriksa.periksa(data)


def periksa_rilis(folder: Path) -> list[Temuan]:
    """Mencocokkan setiap baris rilis/RILIS.md dengan salinan beku dan hashnya."""
    daftar = folder / "RILIS.md"
    nama = str(daftar.relative_to(AKAR)) if daftar.is_relative_to(AKAR) else str(daftar)
    temuan: list[Temuan] = []
    if not daftar.exists():
        return [Temuan(nama, 1, "R-3", "daftar rilis tidak ditemukan")]
    tercatat = set()
    for i, b in enumerate(daftar.read_text(encoding="utf-8").split("\n"), 1):
        m = re.match(r"^\|\s*(\d+\.\d+\.\d+)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|", b)
        if not m:
            continue
        versi, _, _, sha = m.groups()
        if versi in tercatat:
            temuan.append(Temuan(nama, i, "R-3", f"versi {versi} tercatat lebih dari sekali"))
        tercatat.add(versi)
        beku = folder / f"konvensi-artup-{versi}.md"
        if not RE_SHA256.match(sha):
            temuan.append(Temuan(nama, i, "R-3", f"SHA-256 versi {versi} bukan heksadesimal huruf kecil 64 karakter"))
        elif not beku.exists():
            temuan.append(Temuan(nama, i, "R-3", f"salinan beku {beku.name} tidak ditemukan"))
        elif hashlib.sha256(beku.read_bytes()).hexdigest() != sha:
            temuan.append(Temuan(nama, i, "R-3", f"SHA-256 {beku.name} tidak cocok dengan daftar rilis"))
    for beku in sorted(folder.glob("konvensi-artup-*.md")):
        versi = beku.name.removeprefix("konvensi-artup-").removesuffix(".md")
        if versi not in tercatat:
            temuan.append(Temuan(nama, 1, "R-3", f"salinan beku {beku.name} tidak tercatat di daftar rilis"))
    return temuan


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Pemeriksa dokumen Konvensi Artup.")
    parser.add_argument("berkas", nargs="*", type=Path,
                        help=f"dokumen yang diperiksa (bawaan: {DOKUMEN_KERJA.relative_to(AKAR)})")
    parser.add_argument("--gaya", action="store_true",
                        help="tambahkan heuristik gaya: satu kalimat per baris, kata kunci normatif "
                             "di luar ketentuan berkode, dan ketentuan berkode tanpa kata kunci")
    parser.add_argument("--rilis", action="store_true",
                        help="cocokkan rilis/RILIS.md dengan salinan beku dan hashnya")
    parser.add_argument("--hanya-format", action="store_true",
                        help="hanya periksa format byte Bagian 4.1 [F-1] s.d. [F-7]; "
                             "untuk berkas Markdown selain dokumen konvensi")
    args = parser.parse_args(argv)
    if args.hanya_format and not args.berkas:
        parser.error("--hanya-format memerlukan daftar berkas")

    berkas = args.berkas or [DOKUMEN_KERJA]
    temuan: list[Temuan] = []
    for jalur in berkas:
        try:
            nama = str(jalur.relative_to(Path.cwd())) if jalur.is_absolute() and jalur.is_relative_to(Path.cwd()) else str(jalur)
            temuan += periksa_berkas(jalur, nama, gaya=args.gaya, hanya_format=args.hanya_format)
        except OSError as e:
            print(f"{jalur}: tidak dapat dibaca: {e.strerror}", file=sys.stderr)
            return 2
    if args.rilis:
        temuan += periksa_rilis(FOLDER_RILIS)

    for t in temuan:
        print(t)
    return 1 if temuan else 0


if __name__ == "__main__":
    sys.exit(main())
