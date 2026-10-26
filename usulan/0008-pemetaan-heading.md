# Usulan 0008: Pemetaan Heading di Luar Batang Tubuh

| Identitas | Nilai |
|---|---|
| Nomor | 0008 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diajukan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [S-1], [S-2], [S-3], [S-14], [S-18], [S-19], [S-20], L-10 |
| Jenis perubahan | redaksional / penambahan |
| Usulan versi berikutnya | MINOR |

## Latar Belakang

1. **[S-1] bertentangan dengan [S-19] dan [S-20].**
   [S-1] mewajibkan setiap jenis unsur struktur dipetakan ke tingkat heading yang sama "di mana pun ia muncul".
   [S-19] melarang heading untuk label di dalam kutipan, dan [S-20] memetakan heading di dalam Lampiran ke `##` sampai `####` "menurut hierarkinya".
   Lampiran yang memuat BAB (lazim pada lampiran pedoman) tidak jelas memakai tabel 6.2 atau hierarki sendiri, dan L-10 akan menolaknya.
2. **[S-2] dan judul peraturan.**
   Judul peraturan di sumber umumnya tertulis pada beberapa baris: jenis dan nomor, kata "TENTANG", lalu nama.
   [S-2] mewajibkan label dan judul pada baris terpisah digabung dengan ` — `, sedangkan contoh di tabel 6.2 menggabungnya dengan spasi.
   Tidak jelas apakah judul peraturan, judul Penjelasan, dan identitas Lampiran termasuk "label dan judul unsur".
3. **[S-18] untuk perubahan tunggal.**
   [S-18] mewajibkan kutipan disarangkan "di bawah butir perintah perubahannya".
   Peraturan perubahan yang hanya memuat satu perubahan menulis perintahnya sebagai paragraf, bukan butir, sehingga tidak ada butir induk.
4. **Penjelasan peraturan perubahan.**
   Penjelasan pasal demi pasal peraturan perubahan memuat "Pasal I", lalu "Angka 1", lalu "Pasal 5" (Pasal yang diubah).
   [S-14] memetakan Pasal di penjelasan ke `#####`, sehingga "Pasal 5" di sini dapat dibaca sebagai heading juga.
5. **Penanda keraguan pada heading.**
   [S-3] menyatakan heading Pasal hanya berisi label.
   Tidak jelas apakah `##### Pasal {?28A?}` diperbolehkan.

## Rumusan Baru

```markdown
[S-1] Di dalam batang tubuh dan Penjelasan, setiap jenis unsur struktur WAJIB selalu dipetakan ke tingkat heading yang sama.
…

[S-2] … (kalimat baru di akhir)
Ketentuan pemisah ` — ` tidak berlaku untuk judul peraturan, judul Penjelasan, dan identitas Lampiran; baris-baris judul tersebut WAJIB digabung dengan satu spasi.

[S-18] … (kalimat kedua diganti)
Apabila perintah perubahan ditulis sebagai butir rincian, kutipan WAJIB disarangkan di bawah butir tersebut dengan indentasi dua spasi; apabila perintah perubahan ditulis sebagai paragraf, kutipan WAJIB ditulis tanpa indentasi setelah paragraf tersebut.

[S-24] Dalam penjelasan pasal demi pasal peraturan perubahan, hanya Pasal berangka Romawi yang WAJIB ditulis sebagai heading `#####`.
Label lain, termasuk label Pasal yang diubah, WAJIB ditulis sebagai paragraf tersendiri menurut [S-15].

[S-25] Notasi konvensi menurut Bagian 8 BOLEH dipakai di dalam heading; [S-3] tidak melarangnya.
```

Untuk Lampiran, [S-20] diperinci: BAB di dalam Lampiran WAJIB memakai `##`, sedangkan unsur bertingkat di bawahnya (misalnya "A.", "1.") ditulis sebagai heading `###` dan `####` hanya apabila di sumber berupa judul yang berdiri sendiri, dan sebagai paragraf atau daftar dalam hal lain.
Rumusan pasti untuk Lampiran sebaiknya disusun setelah melihat beberapa contoh lampiran nyata (lihat TODO.md).

## Dampak terhadap Berkas Transkripsi

- Berkas peraturan perubahan yang memakai heading untuk "Pasal 5" di penjelasan menjadi tidak sesuai.
- L-10 perlu diperbarui untuk Lampiran dan penjelasan peraturan perubahan.

## Kompatibilitas Versi

MINOR.

## Keputusan
