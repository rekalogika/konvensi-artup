# Usulan 0003: Rujukan Berkas Transkripsi ke Versi Konvensi yang Masih Draf

| Identitas | Nilai |
|---|---|
| Nomor | 0003 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [R-1], [R-3], [R-4], L-06 |
| Jenis perubahan | penambahan |
| Usulan versi berikutnya | MINOR |

## Latar Belakang

[R-1] menetapkan bahwa berkas transkripsi merujuk konvensi dengan `transkripsi-peraturan/MAYOR.MINOR`.
[R-4] menyatakan bahwa berkas `verified` tetap sah menurut versi yang dirujuknya.
Kedua aturan itu mengandaikan bahwa versi yang dirujuk sudah tetap.

Saat ini versi 0.1.0 berstatus draf dan isinya masih dapat berubah.
Berkas transkripsi yang dibuat sekarang dan merujuk `transkripsi-peraturan/0.1` akan merujuk teks yang belum tetap.
Bila sebuah berkas mencapai `verified` sebelum 0.1.0 final, [R-4] tidak dapat menunjukkan aturan mana yang berlaku.

L-06 ("Versi konvensi dikenal") juga tidak menjelaskan arti "dikenal".

Catatan: proyek transkripsi terpisah kemungkinan sudah memakai rujukan `transkripsi-peraturan/0.1`.

## Rumusan Lama

Tidak ada aturan tentang rujukan ke versi draf.

## Rumusan Baru

```markdown
[R-8] Berkas transkripsi BOLEH merujuk versi konvensi yang masih draf selama penyusunan.
Berkas transkripsi TIDAK BOLEH berstatus `verified` sebelum versi konvensi yang dirujuknya final dan tercantum dalam daftar rilis konvensi.
```

L-06: "Versi konvensi tercantum dalam daftar rilis konvensi (verified)"; kolom Ketentuan: `R-1, R-8`.

## Dampak terhadap Berkas Transkripsi

- Berkas yang sudah `verified` dengan rujukan `transkripsi-peraturan/0.1` (bila ada) perlu ditinjau ulang setelah 0.1.0 final.
- Alat pemeriksa berkas transkripsi perlu membaca daftar rilis konvensi untuk L-06.

## Kompatibilitas Versi

MINOR: menambah syarat untuk status `verified`.
Selama MAYOR bernilai 0, perubahan ini diperbolehkan ([R-2]).

## Alternatif yang Dipertimbangkan

- Segera merilis 0.1.0 sebagai final, lalu menampung revisi di 0.2.0.
  Ini cara tercepat untuk mendapatkan rujukan yang tetap, tetapi temuan tinjauan pertama (usulan 0001 sampai 0015) akan menunggu 0.2.0.
- Rujukan draf bertanggal, misalnya `transkripsi-peraturan/0.1-draf-2026-10-26`: lebih tepat, tetapi menambah rumitnya [R-1].

## Keputusan

2026-10-26, Ananda Putra: **diterima**, rumusan utama (bukan alternatif).
Revisi berikutnya ditampung di draf 0.1.0, dan 0.1.0 dirilis setelah usulan penting diterapkan.
Pada tanggal keputusan belum ada berkas transkripsi berstatus `verified`, sehingga butir pertama "Dampak terhadap Berkas Transkripsi" tidak berlaku.

Diterapkan pada draf 0.1.0, tanpa menaikkan versi karena 0.1.0 belum dirilis (AGENTS.md, "Versi dokumen kerja").
Kode aturan menjadi [R-6], bukan [R-8] sebagaimana ditulis sementara di atas, karena kode baru memakai nomor terbesar dalam kelompok ditambah satu.
L-06 diubah sesuai rumusan baru, dengan kolom Ketentuan `R-1, R-6`.
