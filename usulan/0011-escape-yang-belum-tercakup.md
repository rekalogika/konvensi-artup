# Usulan 0011: Escape yang Belum Tercakup dan Rumusan [F-11]

| Identitas | Nilai |
|---|---|
| Nomor | 0011 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diajukan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [F-11], [F-12], [F-13] |
| Jenis perubahan | perubahan tidak kompatibel |
| Usulan versi berikutnya | MINOR (MAYOR masih 0) |

## Latar Belakang

Tujuan Bagian 4.3 adalah agar teks sumber tidak ditafsirkan sebagai markup dan agar setiap teks hanya memiliki satu bentuk byte.
Menurut CommonMark 0.31.2 dan GFM, masih ada karakter yang dapat mengubah tafsir tetapi tidak tercantum:

| Karakter | Masalah |
|---|---|
| `\` | Garis miring terbalik di teks sumber dapat meng-escape karakter berikutnya. |
| `\|` | Di dalam sel tabel GFM, `\|` memisahkan sel. |
| `&` | `&amp;`, `&#…;`, dan sejenisnya ditafsirkan sebagai rujukan entitas. |
| `=` di awal baris | Baris berisi `===` setelah paragraf menjadikan paragraf itu heading Setext. |
| `~` di awal baris | Baris `~~~` membuka blok kode berpagar. |

[F-11] juga terlalu luas.
"Baris yang diawali angka diikuti titik" mencakup `1.5 juta` atau `2022.`, padahal penanda daftar bernomor CommonMark adalah 1–9 digit diikuti `.` atau `)` lalu spasi atau akhir baris.
Karena WAJIB, transkriptor harus menulis `1\.5 juta`; dua transkriptor yang menafsirkan berbeda akan menghasilkan byte berbeda.

## Rumusan Lama

```markdown
[F-11] Baris yang diawali angka diikuti titik atau kurung tutup (misalnya `1.` atau `1)`) WAJIB di-escape menjadi `1\.` atau `1\)`, termasuk di dalam butir daftar dan kutipan.

[F-12] Karakter berikut di awal baris teks WAJIB di-escape bila tidak dimaksudkan sebagai markup: `#`, `>`, `-`, `+`, `*`.

[F-13] Karakter `*`, `_`, `` ` ``, `[`, `]`, `<`, `{`, dan `}` di mana pun dalam teks sumber WAJIB di-escape dengan garis miring terbalik.
```

## Rumusan Baru

```markdown
[F-11] Teks yang diawali satu sampai sembilan digit yang diikuti titik atau kurung tutup, lalu spasi atau akhir baris (misalnya `1.` atau `1)`), WAJIB di-escape menjadi `1\.` atau `1\)`, termasuk di dalam butir daftar dan kutipan.
Titik atau kurung tutup lain setelah angka TIDAK BOLEH di-escape.

[F-12] Karakter berikut di awal baris teks WAJIB di-escape bila tidak dimaksudkan sebagai markup: `#`, `>`, `-`, `+`, `*`, `=`, `~`.

[F-13] Karakter `\`, `*`, `_`, `` ` ``, `[`, `]`, `<`, `&`, `{`, dan `}` di mana pun dalam teks sumber WAJIB di-escape dengan garis miring terbalik.
Karakter `|` di dalam sel tabel GFM WAJIB di-escape dengan garis miring terbalik.
```

Rumusan "TIDAK BOLEH di-escape" diperlukan agar bentuk byte tunggal.
Prinsip yang sama perlu diterapkan pada [F-12] dan [F-13]: karakter yang tidak tercantum TIDAK BOLEH di-escape.

## Dampak terhadap Berkas Transkripsi

- Berkas yang meng-escape `1.5` menjadi `1\.5` menjadi tidak sesuai.
- Berkas yang memuat `\`, `&`, atau `|` dalam sel tabel tanpa escape menjadi tidak sesuai.
- L-08 dan L-13 perlu diperbarui.

## Kompatibilitas Versi

MINOR (tidak kompatibel; MAYOR masih 0).

## Keputusan
