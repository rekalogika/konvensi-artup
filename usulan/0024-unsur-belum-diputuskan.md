# Usulan 0024: Kontradiksi [P-1] dengan [C-5] tentang Unsur yang Belum Diputuskan

| Identitas | Nilai |
|---|---|
| Nomor | 0024 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi kedua |
| Tanggal | 2026-10-27 |
| Status | diajukan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [P-1] |
| Jenis perubahan | redaksional |
| Usulan versi berikutnya | PATCH |

## Latar Belakang

[P-1] mewajibkan badan teks memuat unsur yang ditranskripsi menurut Bagian 5.1 "dan hanya unsur tersebut".
[C-5], sebagaimana dilengkapi usulan 0010, menyatakan bahwa unsur yang tidak tercantum di [C-1] maupun [C-2] SEBAIKNYA ditranskripsi selama belum diputuskan, dan berkasnya TIDAK BOLEH berstatus `verified`.

Kedua ketentuan ini tidak dapat dipenuhi bersamaan.
Transkriptor yang mengikuti anjuran [C-5] melanggar [P-1].
Transkriptor yang mematuhi [P-1] harus menghilangkan unsur tersebut, padahal [C-5] menganjurkan unsur itu tetap ditranskripsi agar tidak hilang sebelum diputuskan.

Menurut catatan penerapan usulan 0010, yang dimaksud adalah [C-5]: unsur yang belum diputuskan tetap ditranskripsi, dan larangan status `verified` mencegah berkas seperti itu dikunci.

## Rumusan Lama

```markdown
[P-1] Badan teks WAJIB memuat seluruh unsur yang ditranskripsi (Bagian 5.1) dan hanya unsur tersebut, dengan kata, ejaan, huruf kapital, angka, dan tanda baca yang sama dengan naskah sumber, kecuali normalisasi yang diatur dalam Bagian 7.
```

## Rumusan Baru

```markdown
[P-1] Badan teks WAJIB memuat seluruh unsur yang ditranskripsi (Bagian 5.1) dan hanya unsur tersebut, ditambah unsur yang belum diputuskan menurut [C-5], dengan kata, ejaan, huruf kapital, angka, dan tanda baca yang sama dengan naskah sumber, kecuali normalisasi yang diatur dalam Bagian 7.
```

## Dampak terhadap Berkas Transkripsi

Berkas yang memuat unsur yang belum diputuskan tidak lagi melanggar [P-1].
Berkas tersebut tetap tidak dapat berstatus `verified` menurut [C-5].
Berkas yang sesuai menurut rumusan lama tetap sesuai.

## Kompatibilitas Versi

PATCH: menyelaraskan [P-1] dengan maksud [C-5] yang sudah berlaku, tanpa menambah ketentuan baru ([R-2]).

## Alternatif yang Dipertimbangkan

- Mengubah [C-5] menjadi "TIDAK BOLEH ditranskripsi" sampai diputuskan: tidak dipilih, karena unsur itu akan hilang dari berkas dan harus ditranskripsi ulang setelah diputuskan.
- Menandai unsur yang belum diputuskan dengan penanda keraguan: sudah ditolak dalam usulan 0010, agar arti penanda keraguan tetap "teks belum pasti".

## Keputusan

Belum diputuskan.
