# Usulan 0016: JSON Schema Frontmatter sebagai Lampiran Normatif

| Identitas | Nilai |
|---|---|
| Nomor | 0016 |
| Pengusul | Claude (Anthropic), atas keputusan Ananda Putra |
| Tanggal | 2026-10-27 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | Bagian 9, [M-9] (baru), L-05, L-22 (baru), lampiran |
| Jenis perubahan | penambahan |
| Usulan versi berikutnya | MINOR |

## Latar Belakang

Aturan frontmatter berkas transkripsi hanya tertulis dalam prosa dan tabel (Bagian 9.3 dan 9.4).
Setiap pembuat alat pemeriksa harus menerjemahkannya sendiri, sehingga dua alat dapat menafsirkan secara berbeda, misalnya tentang tipe `karya.tahun` atau isian tambahan yang dilarang [M-6].

Ananda memutuskan (2026-10-27) bahwa aturan frontmatter juga ditulis dalam bentuk yang dapat dibaca mesin, dan bentuk itu menjadi bagian resmi (normatif) konvensi.

## Rumusan Lama

Tidak ada.

## Rumusan Baru

1. **Lampiran C (normatif): JSON Schema Frontmatter**, ditulis menurut JSON Schema Draft 2020-12 dan dimuat di dalam dokumen konvensi.
   Dengan begitu, skema ikut dibekukan dan ter-hash bersama dokumen saat rilis ([R-3]), tanpa mengubah format daftar rilis.
   Lampiran Referensi dan Riwayat Perubahan bergeser menjadi Lampiran D dan E.
2. **[M-9]** di Bagian 9.1:

```markdown
[M-9] Frontmatter, setelah diurai menurut skema inti (*core schema*) YAML 1.2, WAJIB valid terhadap JSON Schema di Lampiran C.
Ketentuan Bagian 9 yang tidak dapat dinyatakan dalam skema tetap berlaku di samping skema tersebut (Bagian 16.1).
Apabila tabel Bagian 9.3 atau Bagian 9.4 berbeda dengan Lampiran C, Lampiran C yang berlaku, dan perbedaan itu WAJIB diperbaiki dalam versi konvensi berikutnya.
```

3. **L-05** merujuk `M-1 s.d. M-7, M-9`.
4. **L-22** (baru): gabungan `sumber[].komponen` sama dengan `ekspresi.komponen` ([M-8]), yang sebelumnya tidak memiliki pemeriksaan.
5. Bagian 9.5 diberi catatan bahwa contohnya memakai tanda `…` sehingga belum valid terhadap skema.

Isi skema:

- isian wajib, tipe, dan larangan isian tambahan (`additionalProperties: false`) sesuai tabel Bagian 9.3 dan 9.4;
- pola untuk `konvensi`, pengenal karya ([I-1], [I-3]) termasuk daftar kode jenis, pengenal ekspresi ([I-4]), tanggal ([M-4]), hash SHA-256, URL, versi berkas transkripsi, dan kode bahasa;
- nilai tertutup untuk `ekspresi.jenis_teks` dan komponen naskah.

Yang tidak dapat dinyatakan dalam skema, dan karena itu tetap diatur dalam prosa: isian "WAJIB bila ada", cara penulisan tanda kutip ([M-6]), [M-8], dan kesesuaian pengenal ekspresi dengan pengenal karya ([I-4]).

## Dampak terhadap Berkas Transkripsi

- Berkas yang sesuai Bagian 9 seharusnya juga valid terhadap skema.
  Pola pengenal dan hash kini diperiksa secara tegas, sehingga nilai seperti hash berhuruf kapital atau pengenal berhuruf besar menjadi tidak sesuai.
- Alat pemeriksa berkas transkripsi dapat memakai validator JSON Schema siap pakai untuk L-05.
  Pengurai YAML 1.1 perlu mengubah tanggal menjadi string sebelum validasi (Bagian 16.1).

## Kompatibilitas Versi

MINOR (penambahan; MAYOR masih 0), ditampung di draf 0.1.0.

## Alternatif yang Dipertimbangkan

- Skema informatif (rekomendasi semula Claude): tidak dipilih; Ananda memutuskan skema menjadi normatif.
- Skema sebagai berkas `.json` terpisah: tidak dipilih, karena daftar rilis mencatat satu berkas per versi dan skema terpisah dapat tertinggal dari dokumen.

## Keputusan

2026-10-27, Ananda Putra: aturan frontmatter ditulis dalam bentuk yang dapat dibaca mesin dan menjadi bagian resmi konvensi.
Rincian rumusan diputuskan oleh Claude atas kuasa Ananda.

Diterapkan pada draf 0.1.0 tanpa menaikkan versi.
Alat pemeriksa konvensi kini memvalidasi skema terhadap metaskema Draft 2020-12 dan memeriksa keselarasannya dengan tabel Bagian 9.3 dan 9.4 (nama isian, sifat wajib, tipe); dependensi `jsonschema` ditambahkan.
