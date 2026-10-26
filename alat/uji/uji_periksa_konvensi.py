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
id: konvensi/contoh
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

[F-3] Lihat [F-1] dan Bagian 1.1 serta Lampiran A.

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
        self.assertIn("frontmatter", kode(periksa(CONTOH_SESUAI.replace("id: konvensi/contoh\n", "id: [\n"))))
        self.assertIn("frontmatter", kode(periksa(CONTOH_SESUAI.replace("nama: Konvensi Contoh\n", ""))))
        self.assertIn("R-1", kode(periksa(CONTOH_SESUAI.replace("versi: 0.1.0", "versi: 0.1"))))

    def test_identitas(self):
        t = periksa(CONTOH_SESUAI.replace("| Versi | 0.1.0 |", "| Versi | 0.2.0 |"))
        self.assertEqual(kode(t), ["identitas"])
        t = periksa(CONTOH_SESUAI.replace("berstatus **draf**", "berstatus **final**"))
        self.assertEqual(kode(t), ["identitas"])
        t = periksa(CONTOH_SESUAI.replace("| 0.1.0 | 2026-10-26 | Draf", "| 0.0.9 | 2026-10-26 | Draf"))
        self.assertEqual(kode(t), ["R-2"])

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
