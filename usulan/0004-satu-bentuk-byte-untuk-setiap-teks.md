# Usulan 0004: Satu Bentuk Byte untuk Setiap Teks

| Identitas | Nilai |
|---|---|
| Nomor | 0004 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [S-13], N-3, N-8, Lampiran A |
| Jenis perubahan | perubahan tidak kompatibel |
| Usulan versi berikutnya | MINOR (MAYOR masih 0) |

## Latar Belakang

Hash dan metode ketik ganda ([V-2]) hanya bekerja bila dua transkriptor yang menaati konvensi menghasilkan byte yang sama.
Dua aturan memberi lebih dari satu bentuk yang sah:

1. **[S-13] bertentangan dengan N-3.**
   [S-13] menyatakan baris-baris dalam satu blok penutup "BOLEH ditulis pada baris berurutan dalam satu paragraf".
   N-3 menyatakan "Pergantian baris di dalam satu kalimat atau paragraf WAJIB diganti satu spasi".
   Lampiran A memakai bentuk baris berurutan ("Disahkan di Jakarta" / "pada tanggal 17 Oktober 2022").
   Karena [S-13] memakai BOLEH, `Disahkan di Jakarta pada tanggal 17 Oktober 2022` (satu baris) juga sah.
2. **N-8 memberi dua pilihan.**
   N-8 menyatakan spasi tak terputus, tanda hubung lunak, dan karakter lebar nol "WAJIB dihapus atau diganti spasi biasa" tanpa menyebut mana yang berlaku untuk karakter mana.

## Rumusan Lama

```markdown
[S-13] Penutup tidak diberi heading.
Setiap blok penutup (misalnya tempat dan tanggal pengesahan, jabatan, keterangan "ttd", nama) ditulis sebagai paragraf terpisah.
Baris-baris dalam satu blok, misalnya "Disahkan di Jakarta" dan "pada tanggal …", BOLEH ditulis pada baris berurutan dalam satu paragraf.
```

```markdown
| N-8 | Spasi tak terputus (U+00A0), tanda hubung lunak (U+00AD), dan karakter lebar nol WAJIB dihapus atau diganti spasi biasa. |
```

## Rumusan Baru

[S-13], pilihan A (direkomendasikan; selaras dengan N-3):

```markdown
[S-13] Penutup TIDAK BOLEH diberi heading.
Setiap blok penutup (misalnya tempat dan tanggal pengesahan, jabatan, keterangan "ttd", nama) WAJIB ditulis sebagai paragraf terpisah.
Baris-baris dalam satu blok WAJIB digabung dengan satu spasi menurut N-3, misalnya `Disahkan di Jakarta pada tanggal 17 Oktober 2022`.
```

[S-13], pilihan B (mempertahankan bentuk sumber):

```markdown
Baris-baris dalam satu blok WAJIB ditulis pada baris berurutan dalam satu paragraf, sesuai pemenggalan baris di sumber; ketentuan ini merupakan pengecualian dari N-3.
```

N-8:

```markdown
| N-8 | Spasi tak terputus (U+00A0) WAJIB diganti spasi biasa. Tanda hubung lunak (U+00AD) dan karakter lebar nol (U+200B, U+200C, U+200D, U+2060, U+FEFF) WAJIB dihapus. |
```

Lampiran A disesuaikan dengan pilihan yang diambil.

## Dampak terhadap Berkas Transkripsi

- Pilihan A: berkas yang memakai baris berurutan di penutup menjadi tidak sesuai dan perlu disunting.
- Pilihan B: berkas yang menggabung baris penutup menjadi tidak sesuai.
- N-8: berkas yang mengganti karakter lebar nol dengan spasi menjadi tidak sesuai.
- Alat pemeriksa berkas transkripsi dapat menambah pemeriksaan untuk kedua hal ini.

## Kompatibilitas Versi

Tidak kompatibel; MINOR selama MAYOR bernilai 0 ([R-2]).

## Alternatif yang Dipertimbangkan

- Membiarkan BOLEH, lalu menormalkan dalam alat pembanding ketik ganda: tidak dipilih karena hash berkas tetap bergantung pada pilihan transkriptor.
- U+200C dan U+200D bermakna dalam aksara tertentu (misalnya Arab); bila Lampiran memuat teks beraksara non-Latin, pengecualian perlu ditambahkan.

## Keputusan

2026-10-26, diputuskan oleh Claude atas kuasa Ananda Putra: **diterima**, [S-13] pilihan A dan rumusan N-8 apa adanya.
Pilihan A dipilih karena selaras dengan N-3 dan karena penampil Markdown menampilkan pergantian baris lunak sebagai spasi, sehingga tampilan tidak berubah.
Contoh penutup di Lampiran A disesuaikan.
Pengecualian untuk U+200C dan U+200D pada aksara non-Latin belum diperlukan; bila Lampiran beraksara non-Latin ditemukan, diusulkan tersendiri.

Diterapkan pada draf 0.1.0 tanpa menaikkan versi.
