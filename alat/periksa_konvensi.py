#!/usr/bin/env python3
"""Pemeriksa dokumen Konvensi Artup.

Memeriksa dokumen konvensi (bukan berkas transkripsi) terhadap:

- aturan format Bagian 4.1 [F-1] sampai [F-7];
- frontmatter YAML yang valid dan konsisten dengan tabel identitas;
- blok kode (fence) yang seimbang;
- kode aturan yang tidak ganda dan tanpa lompatan penomoran;
- rujukan kode aturan, "Bagian n.n", dan "Lampiran X" yang benar-benar ada;
- daftar isi yang sesuai dengan heading.

Keluaran per baris berformat ``berkas:baris: [kode] pesan``.
Kode keluar: 0 bila bersih, 1 bila ada temuan, 2 bila berkas tidak dapat dibaca.

Penulis: Claude (Claude Opus 5.5, model AI buatan Anthropic), atas permintaan
dan di bawah arahan Ananda Putra, 2026-10-26.

Sumber: ditulis baru untuk proyek ini; tidak ada kode yang disalin dari skrip
atau proyek lain. Satu-satunya pustaka luar adalah PyYAML (pyyaml.org), dipakai
sebagai dependensi biasa. Aturan yang diperiksa diambil dari dokumen Konvensi
Artup sendiri; pengenalan heading ATX dan blok kode berpagar mengikuti
CommonMark Spec 0.31.2 (spec.commonmark.org), Bagian 4.2 dan 4.5.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import yaml

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
        rujukan = next((v for k, v in tabel.items() if k.startswith("Rujukan singkat")), None)
        if rujukan and RE_SEMVER.match(versi):
            mayor_minor = ".".join(versi.split(".")[:2])
            m = re.search(r"transkripsi-peraturan/(\d+\.\d+)", rujukan[1])
            if not m or m.group(1) != mayor_minor:
                self.lapor(rujukan[0], "R-1",
                           f"rujukan singkat tidak sama dengan transkripsi-peraturan/{mayor_minor}")

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
        if self.gaya:
            self.periksa_gaya(dok)
        self.temuan.sort(key=lambda t: t.baris)
        return self.temuan


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
                        help="tambahkan heuristik gaya: satu kalimat per baris")
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
