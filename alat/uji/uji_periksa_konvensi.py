"""Uji pemeriksa dokumen konvensi.

Contoh dibangun di dalam kode, bukan disimpan sebagai berkas, agar penyunting
teks tidak membetulkan pelanggaran yang sengaja dibuat (spasi di akhir baris, CR, tab).

Jalankan: .venv/bin/python -m unittest discover -s alat/uji -p 'uji_*.py'

Penulis: Claude (Claude Opus 5.5, model AI buatan Anthropic), atas permintaan
dan di bawah arahan Ananda Putra, 2026-10-26. Ditulis baru untuk proyek ini;
tidak ada kode yang disalin dari sumber lain.
"""

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import periksa_konvensi as pk  # noqa: E402

CONTOH_SESUAI = """\
---
id: transkripsi-peraturan
nama: Konvensi Contoh
judul: Konvensi Contoh
versi: 0.1.0
status: draf
tanggal: 2026-10-26
---

# Konvensi Contoh

| Identitas | Nilai |
|---|---|
| Versi | 0.1.0 |
| Status | Draf |
| Tanggal | 2026-10-26 |
| Rujukan singkat dalam berkas transkripsi | `transkripsi-peraturan/0.1` |

## Status Dokumen Ini

Dokumen ini berstatus **draf**.

## Daftar Isi

1. Format
2. Lampiran A: Riwayat Perubahan

## 1. Format

### 1.1. Baris

- [F-1] Berkas WAJIB berupa UTF-8.
- [F-2] Akhir baris WAJIB berupa LF.

[F-3] Rujukan WAJIB menunjuk ketentuan yang ada.
Lihat [F-1] dan Bagian 1.1 serta Lampiran A.

| Kode | Pemeriksaan | Ketentuan |
|---|---|---|
| L-01 | UTF-8 | F-1 s.d. F-3 |

```markdown
[F-99] di dalam blok kode tidak dihitung; Bagian 42 juga tidak.
```

## 2. Lampiran A: Riwayat Perubahan

| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1.0 | 2026-10-26 | Draf pertama. |
"""


def periksa(teks: str | bytes, gaya: bool = False) -> list[pk.Temuan]:
    data = teks.encode("utf-8") if isinstance(teks, str) else teks
    return pk.Pemeriksa("uji.md", gaya=gaya).periksa(data)


def kode(temuan: list[pk.Temuan]) -> list[str]:
    return [t.kode for t in temuan]


class UjiSkema(unittest.TestCase):
    """Keselarasan tabel isian Bagian 9.3 dan 9.4 dengan JSON Schema di lampiran, diuji pada dokumen kerja."""

    @classmethod
    def setUpClass(cls):
        cls.dok = pk.DOKUMEN_KERJA.read_text(encoding="utf-8")

    def temuan_skema(self, teks: str) -> list[str]:
        return [t.pesan for t in periksa(teks) if t.kode == "skema"]

    def ubah(self, lama: str, baru: str) -> list[str]:
        self.assertEqual(self.dok.count(lama), 1, lama)
        return self.temuan_skema(self.dok.replace(lama, baru))

    def test_dokumen_kerja_selaras(self):
        self.assertEqual(self.temuan_skema(self.dok), [])

    def test_sifat_wajib_berbeda(self):
        t = self.ubah("| `karya.singkatan` | BOLEH |", "| `karya.singkatan` | WAJIB |")
        self.assertEqual(len(t), 1)
        self.assertIn("sifat wajib isian `karya.singkatan`", t[0])
        t = self.ubah("| `hash_badan` | WAJIB |", "| `hash_badan` | BOLEH |")
        self.assertIn("`verifikasi[].hash_badan`", t[0])

    def test_tipe_berbeda(self):
        t = self.ubah("| `karya.tahun` | WAJIB | bilangan |", "| `karya.tahun` | WAJIB | string |")
        self.assertEqual(t, ["tipe isian `karya.tahun` (string) berbeda dengan JSON Schema"])
        t = self.ubah("| `sumber[].diakses` | WAJIB | tanggal |", "| `sumber[].diakses` | WAJIB | string |")
        self.assertEqual(t, ["tipe isian `sumber[].diakses` (string) berbeda dengan JSON Schema"])
        t = self.ubah("| `transkripsi.metode` | WAJIB | string |", "| `transkripsi.metode` | WAJIB | tanggal |")
        self.assertEqual(len(t), 1)

    def test_isian_hanya_di_salah_satu(self):
        t = self.ubah("| `karya.pemrakarsa` | BOLEH | string | Instansi pemrakarsa |\n", "")
        self.assertEqual(t, ["isian `karya.pemrakarsa` ada di JSON Schema tetapi tidak ada di tabel"])
        t = self.ubah("| `karya.pemrakarsa` | BOLEH | string | Instansi pemrakarsa |\n",
                      "| `karya.pemrakarsa` | BOLEH | string | Instansi pemrakarsa |\n| `karya.baru` | BOLEH | string | x |\n")
        self.assertEqual(t, ["isian `karya.baru` tidak ada di JSON Schema"])

    def test_skema_rusak(self):
        t = self.ubah('  "$schema": "https://json-schema.org/draft/2020-12/schema",', '  "$schema": "https://json-schema.org/draft/2020-12/schema"')
        self.assertTrue(t and t[0].startswith("JSON tidak valid"))
        t = self.ubah('"pattern": "^[0-9a-f]{64}$"', '"pattern": 64')
        self.assertTrue(t and t[0].startswith("bukan JSON Schema Draft 2020-12 yang valid"))


class UjiContohUji(unittest.TestCase):
    """Lampiran contoh uji pada dokumen kerja: berkas dasar lolos dan setiap kasus menghasilkan temuan yang ditetapkan."""

    @classmethod
    def setUpClass(cls):
        cls.dok = pk.DOKUMEN_KERJA.read_text(encoding="utf-8")

    def temuan_contoh(self, teks: str) -> list[str]:
        return [t.pesan for t in periksa(teks) if t.kode == "contoh-uji"]

    def ubah(self, lama: str, baru: str) -> list[str]:
        self.assertEqual(self.dok.count(lama), 1, lama)
        return self.temuan_contoh(self.dok.replace(lama, baru))

    def test_dokumen_kerja_lolos(self):
        self.assertEqual(self.temuan_contoh(self.dok), [])

    def test_harapan_salah_terdeteksi(self):
        lama = "  aturan: [M-4, M-9]\n  pemeriksaan: [L-05]"
        t = self.ubah(lama, "  aturan: [M-4, M-9]\n  pemeriksaan: [L-07]")
        self.assertEqual(t, ["kasus U-18: diharapkan tanpa temuan untuk pemeriksaan yang dapat dinilai alat ini, didapat L-05"])

    def test_berkas_dasar_rusak(self):
        t = self.ubah("  transkriptor: [Transkriptor Contoh]\n", "  transkriptor: []\n")
        self.assertIn("berkas dasar menimbulkan temuan L-05", t)

    def test_teks_dari_tidak_unik(self):
        t = self.ubah('    dari: "MEMUTUSKAN:\\n"', '    dari: "Cukup jelas."')
        self.assertTrue(any(p.startswith("kasus U-15: teks `dari` muncul") for p in t), t)

    def test_tingkat_berbeda(self):
        t = self.ubah("- kode: U-41\n  hasil: peringatan", "- kode: U-41\n  hasil: galat")
        self.assertIn("kasus U-41: tingkat L-11 (peringatan) berbeda dengan hasil `galat`", t)

    def test_kode_tidak_didefinisikan(self):
        t = self.ubah("  aturan: [K-4]\n  pemeriksaan: [L-20]", "  aturan: [K-4]\n  pemeriksaan: [L-99]")
        self.assertIn("kasus U-31 merujuk kode L-99 yang tidak didefinisikan", t)


class UjiPemeriksa(unittest.TestCase):
    def test_contoh_sesuai_bersih(self):
        self.assertEqual(periksa(CONTOH_SESUAI), [])

    def test_dokumen_kerja_terbaca(self):
        # Dokumen kerja tidak boleh membuat pemeriksa gagal; temuannya dilaporkan, bukan diuji di sini.
        self.assertIsInstance(pk.periksa_berkas(pk.DOKUMEN_KERJA), list)

    def test_format_bagian_4_1(self):
        teks = CONTOH_SESUAI.replace("# Konvensi Contoh\n", "# Konvensi Contoh \n\n\n\tx\n")
        self.assertEqual(sorted(kode(periksa(teks))), ["F-4", "F-5", "F-7"])
        self.assertEqual(kode(periksa(b"\xef\xbb\xbf" + CONTOH_SESUAI.encode())), ["F-1"])
        self.assertIn("F-1", kode(periksa(CONTOH_SESUAI.encode() + b"\xff\n")))
        self.assertEqual(kode(periksa(CONTOH_SESUAI.replace("\n", "\r\n", 1))), ["F-2"])
        self.assertEqual(kode(periksa(CONTOH_SESUAI.replace("Draf pertama", "Café"))), ["F-3"])
        self.assertEqual(kode(periksa(CONTOH_SESUAI.rstrip("\n"))), ["F-6"])
        self.assertEqual(kode(periksa(CONTOH_SESUAI + "\n")), ["F-6"])

    def test_frontmatter(self):
        self.assertIn("frontmatter", kode(periksa(CONTOH_SESUAI.replace("id: transkripsi-peraturan\n", "id: [\n"))))
        self.assertIn("frontmatter", kode(periksa(CONTOH_SESUAI.replace("nama: Konvensi Contoh\n", ""))))
        self.assertIn("R-1", kode(periksa(CONTOH_SESUAI.replace("versi: 0.1.0", "versi: 0.1"))))

    def test_identitas(self):
        t = periksa(CONTOH_SESUAI.replace("| Versi | 0.1.0 |", "| Versi | 0.2.0 |"))
        self.assertEqual(kode(t), ["identitas"])
        t = periksa(CONTOH_SESUAI.replace("berstatus **draf**", "berstatus **final**"))
        self.assertEqual(kode(t), ["identitas"])
        t = periksa(CONTOH_SESUAI.replace("| 0.1.0 | 2026-10-26 | Draf", "| 0.0.9 | 2026-10-26 | Draf"))
        self.assertEqual(kode(t), ["R-2"])

    def test_pengenal(self):
        t = periksa(CONTOH_SESUAI.replace("id: transkripsi-peraturan", "id: konvensi/transkripsi-peraturan"))
        self.assertEqual(kode(t), ["R-7"])
        dengan_baris = CONTOH_SESUAI.replace("| Versi | 0.1.0 |", "| Pengenal | `transkripsi-peraturan` |\n| Versi | 0.1.0 |")
        self.assertEqual(periksa(dengan_baris), [])
        t = periksa(dengan_baris.replace("| Pengenal | `transkripsi-peraturan` |", "| Pengenal | `lain` |"))
        self.assertEqual(kode(t), ["R-7"])
        t = periksa(CONTOH_SESUAI.replace("`transkripsi-peraturan/0.1`", "`transkripsi-peraturan/0.2`"))
        self.assertEqual(kode(t), ["R-1"])

    def test_kode_ganda_dan_lompatan(self):
        t = periksa(CONTOH_SESUAI.replace("- [F-2]", "- [F-1]"))
        self.assertIn("kode F-1 ganda (pertama di baris 32)", [x.pesan for x in t])
        t = periksa(CONTOH_SESUAI.replace("- [F-2] Akhir baris WAJIB berupa LF.\n", ""))
        self.assertIn("kode", kode(t))

    def test_aturan_dihapus(self):
        dihapus = CONTOH_SESUAI.replace("- [F-2] Akhir baris WAJIB berupa LF.", "- [F-2] Dihapus dalam versi 0.2.0.")
        self.assertEqual(kode(periksa(dihapus)), ["rujukan"])  # dirujuk lewat rentang F-1 s.d. F-3

    def test_rujukan(self):
        t = periksa(CONTOH_SESUAI.replace("Lihat [F-1]", "Lihat [F-9]"))
        self.assertEqual([x.pesan for x in t], ["merujuk kode F-9 yang tidak didefinisikan"])
        t = periksa(CONTOH_SESUAI.replace("Bagian 1.1 serta", "Bagian 1.2 serta"))
        self.assertEqual([x.pesan for x in t], ["merujuk Bagian 1.2 yang tidak ada"])
        t = periksa(CONTOH_SESUAI.replace("Lampiran A.", "Lampiran B."))
        self.assertEqual([x.pesan for x in t], ["merujuk Lampiran B yang tidak ada"])
        t = periksa(CONTOH_SESUAI.replace("F-1 s.d. F-3", "F-3 s.d. F-1"))
        self.assertEqual(kode(t), ["rujukan"])

    def test_daftar_isi(self):
        t = periksa(CONTOH_SESUAI.replace("1. Format\n", "1. Format Berkas\n", 1))
        self.assertEqual(kode(t), ["daftar-isi"])
        t = periksa(CONTOH_SESUAI.replace("2. Lampiran A: Riwayat Perubahan\n", "", 1))
        self.assertEqual(kode(t), ["daftar-isi"])

    def test_penomoran_bagian(self):
        t = periksa(CONTOH_SESUAI.replace("### 1.1. Baris", "### 1.2. Baris").replace("Bagian 1.1", "Bagian 1.2"))
        self.assertEqual(kode(t), ["heading"])

    def test_fence(self):
        t = periksa(CONTOH_SESUAI.replace("```\n\n## 2.", "\n## 2."))
        self.assertIn("fence", kode(t))

    def test_gaya(self):
        teks = CONTOH_SESUAI.replace("WAJIB berupa LF.", "WAJIB berupa LF. CR TIDAK BOLEH ada.")
        self.assertEqual(kode(periksa(teks, gaya=True)), ["gaya"])
        self.assertEqual(periksa(CONTOH_SESUAI, gaya=True), [])

    def test_kata_kunci(self):
        def temuan(teks: str) -> list[tuple[int, str]]:
            return [(t.baris, t.pesan) for t in periksa(teks, gaya=True) if t.kode == "kata-kunci"]

        def baris_ke(teks: str, potongan: str) -> int:
            return teks.split("\n").index(potongan) + 1

        # Kata kunci di paragraf tanpa kode; dalam tabel, kode sebaris, tanda kutip, dan blok kode tidak dihitung.
        teks = CONTOH_SESUAI.replace("[F-3] Rujukan", "Lepas WAJIB dicatat.\n\n[F-3] Rujukan")
        self.assertEqual(temuan(teks), [(baris_ke(teks, "Lepas WAJIB dicatat."), "kata kunci normatif di luar ketentuan berkode")])
        for lepas in ("Istilah `WAJIB` dan \"BOLEH\" dikutip.", "| WAJIB | tabel |", "```\nWAJIB\n```"):
            self.assertEqual(temuan(CONTOH_SESUAI.replace("[F-3] Rujukan", f"{lepas}\n\n[F-3] Rujukan")), [], lepas)

        # Lanjutan ketentuan: baris dalam paragraf yang sama dan daftar sesudah titik dua.
        lanjutan = ("[F-3] Rujukan berikut:\n\n- a. WAJIB menunjuk ketentuan;\n- b. BOLEH memakai rentang.\n"
                    "Lihat [F-1] dan Bagian 1.1 serta Lampiran A.")
        self.assertEqual(temuan(CONTOH_SESUAI.replace("[F-3] Rujukan WAJIB menunjuk ketentuan yang ada.\n"
                                                      "Lihat [F-1] dan Bagian 1.1 serta Lampiran A.", lanjutan)), [])

        # Paragraf sesudah blok kode tidak lagi termasuk ketentuan, walaupun ketentuannya diakhiri titik dua.
        teks = CONTOH_SESUAI.replace("[F-3] Rujukan WAJIB menunjuk ketentuan yang ada.",
                                     "[F-3] Rujukan WAJIB berbentuk:\n\n```text\nF-n\n```\n\nBentuk lain TIDAK BOLEH dipakai.")
        self.assertEqual([b for b, _ in temuan(teks)], [baris_ke(teks, "Bentuk lain TIDAK BOLEH dipakai.")])

        # Butir daftar tanpa kode sesudah butir berkode bukan bagian ketentuan.
        teks = CONTOH_SESUAI.replace("- [F-2] Akhir baris WAJIB berupa LF.",
                                     "- [F-2] Akhir baris WAJIB berupa LF.\n- Catatan: CR TIDAK BOLEH ada.")
        self.assertEqual([b for b, _ in temuan(teks)], [baris_ke(teks, "- Catatan: CR TIDAK BOLEH ada.")])

        # Ketentuan tanpa kata kunci; kelompok P dan aturan yang dihapus dikecualikan.
        teks = CONTOH_SESUAI.replace("[F-2] Akhir baris WAJIB berupa LF.", "[F-2] Akhir baris berupa LF.")
        self.assertEqual(temuan(teks), [(baris_ke(teks, "- [F-2] Akhir baris berupa LF."),
                                         "ketentuan [F-2] tidak memuat kata kunci normatif")])
        self.assertEqual(temuan(teks.replace("[F-2] Akhir baris berupa LF.", "[F-2] Dihapus dalam versi 0.2.0.")), [])
        teks = CONTOH_SESUAI.replace("## 1. Format\n", "## 1. Format\n\n[P-1] Transkripsi setia pada isi.\n")
        self.assertEqual(temuan(teks), [])

    def test_hanya_format(self):
        with tempfile.TemporaryDirectory() as tmp:
            jalur = Path(tmp) / "bebas.md"
            jalur.write_bytes(b"# Tanpa frontmatter\n\nBaris akhir \n")
            self.assertEqual(kode(pk.periksa_berkas(jalur, hanya_format=True)), ["F-5"])
            self.assertIn("frontmatter", kode(pk.periksa_berkas(jalur)))
            with redirect_stdout(io.StringIO()) as keluaran:
                self.assertEqual(pk.main(["--hanya-format", str(jalur)]), 1)
            self.assertRegex(keluaran.getvalue(), r"^.+bebas\.md:3: \[F-5\] ")


if __name__ == "__main__":
    unittest.main()
