# Usulan 0001: Penerapan Aturan Format pada Dokumen Konvensi

| Identitas | Nilai |
|---|---|
| Nomor | 0001 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | Bagian 1.5, [F-9] sampai [F-14] |
| Jenis perubahan | redaksional |
| Usulan versi berikutnya | PATCH |

## Latar Belakang

Bagian 1.5 menyatakan bahwa dokumen konvensi "tunduk pada aturan format berkas di Bagian 4" dan bahwa "Aturan pada Bagian 5 sampai Bagian 8 berlaku untuk berkas transkripsi, bukan untuk dokumen ini".

Bagian 4 memuat lebih dari aturan byte.
Dokumen konvensi sendiri melanggar sebagian besar aturan Bagian 4.2 dan 4.3:

- [F-10] melarang blok kode, huruf tebal, dan kode sebaris; dokumen memakai ketiganya, misalnya Bagian 9.5 dan Bagian 2.1.
- [F-11] mewajibkan escape `1\.`; daftar isi memakai `1. Pendahuluan` tanpa escape.
- [F-13] mewajibkan escape `[` dan `]` di mana pun; setiap kode aturan seperti `[F-3]` tidak di-escape.

Akibatnya, dokumen konvensi tidak sesuai dengan aturannya sendiri.
Selain itu, Bagian 1.5 tidak menyebut Bagian 9 sampai 12, sehingga tidak jelas apakah frontmatter dokumen ini tunduk pada Bagian 9.

## Rumusan Lama

```markdown
Dokumen konvensi ini sendiri ditulis dalam Markdown dan tunduk pada aturan format berkas di Bagian 4.
Aturan pada Bagian 5 sampai Bagian 8 berlaku untuk berkas transkripsi, bukan untuk dokumen ini.
```

## Rumusan Baru

```markdown
Dokumen konvensi ini sendiri ditulis dalam Markdown dan tunduk pada aturan pengodean dan baris di Bagian 4.1.
Aturan lain dalam konvensi ini, termasuk Bagian 4.2 dan Bagian 4.3, berlaku untuk berkas transkripsi, bukan untuk dokumen ini.
```

## Dampak terhadap Berkas Transkripsi

Tidak ada.
Perubahan hanya memperjelas aturan yang berlaku bagi dokumen konvensi.

## Kompatibilitas Versi

PATCH: tidak ada berkas transkripsi yang berubah status kesesuaiannya.

## Alternatif yang Dipertimbangkan

- Menulis dokumen konvensi sesuai seluruh Bagian 4: tidak dipilih karena dokumen kehilangan blok contoh, kode sebaris, dan tabel kata kunci tebal, sehingga sulit dibaca.
- Menghapus Bagian 1.5: tidak dipilih karena aturan format byte tetap berguna untuk hash rilis ([R-3]).

## Keputusan

2026-10-26, diputuskan oleh Claude atas kuasa Ananda Putra: **diterima** dengan rumusan baru apa adanya.
Diterapkan pada draf 0.1.0 tanpa menaikkan versi, karena 0.1.0 belum dirilis.
