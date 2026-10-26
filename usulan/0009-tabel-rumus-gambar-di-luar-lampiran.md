# Usulan 0009: Tabel, Rumus, dan Gambar di Luar Lampiran

| Identitas | Nilai |
|---|---|
| Nomor | 0009 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diajukan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [F-9], [F-10], [S-21], [S-22], [S-23], [C-1] butir 13 |
| Jenis perubahan | penambahan |
| Usulan versi berikutnya | MINOR |

## Latar Belakang

Tabel GFM dan HTML `<table>` hanya diizinkan untuk "Tabel … dalam Lampiran" ([F-9]), dan aturan tabel, rumus, serta gambar ([S-21] sampai [S-23]) terletak di Bagian 6.9 Lampiran.
[C-1] butir 13 juga hanya menyebut tabel, rumus, dan gambar sebagai isi Lampiran.

Batang tubuh dan Penjelasan dapat memuat tabel atau rumus.
Contoh yang perlu diverifikasi terhadap naskah: tabel lapisan penghasilan kena pajak dalam Pasal 17 Undang-Undang Pajak Penghasilan sebagaimana diubah, dan rumus perhitungan dalam peraturan di bidang keuangan negara.
Menurut rumusan sekarang, tabel semacam itu tidak dapat ditranskripsi tanpa melanggar [F-9].

## Rumusan Lama

[F-9], baris tabel: `| Tabel GFM | Tabel sederhana dalam Lampiran (Bagian 6.9) |` dan `| HTML <table> terbatas | Tabel kompleks dalam Lampiran (Bagian 6.9) |`.

## Rumusan Baru

1. Pindahkan [S-21], [S-22], dan [S-23] ke subbagian baru "6.10. Tabel, Rumus, dan Gambar" (kode tetap) dan nyatakan berlaku di seluruh badan teks.
   Bagian 6.9 mempertahankan [S-20] dan merujuk Bagian 6.10.
2. [F-9]: ganti "dalam Lampiran (Bagian 6.9)" menjadi "(Bagian 6.10)".
3. Tambahkan ketentuan untuk tabel di dalam rincian atau ayat:

```markdown
[S-26] Tabel yang terletak di dalam rincian WAJIB disarangkan dengan indentasi butir rinciannya.
```

## Dampak terhadap Berkas Transkripsi

Tidak ada berkas yang sesuai menjadi tidak sesuai; penambahan ini memungkinkan berkas yang sebelumnya tidak dapat ditulis.

## Kompatibilitas Versi

MINOR (penambahan yang kompatibel).

## Keputusan
