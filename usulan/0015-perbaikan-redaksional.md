# Usulan 0015: Perbaikan Redaksional Kecil

| Identitas | Nilai |
|---|---|
| Nomor | 0015 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diajukan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | Bagian 1.4, 6.5, 6.7, 11.2, 16 |
| Jenis perubahan | redaksional |
| Usulan versi berikutnya | PATCH |

## Latar Belakang dan Rumusan Baru

Setiap butir dapat diterima atau ditolak sendiri-sendiri.

1. **Bagian 1.4: sifat acuan metadata.**
   Tabel menyebut Permenkumham 8/2019 dan Portal JDIHN "Diselaraskan", sedangkan Bagian 9.6 menyatakan pemetaannya informatif dan penyelarasan akhir belum dilakukan.
   Usul: "Dipetakan secara informatif (Bagian 9.6); penyelarasan dengan Permenkumham 8/2019 belum dilakukan".
2. **Bagian 11.2 langkah 2: kalimat taksa.**
   "Berkas diserahkan ke verifikator berstatus `verification in progress`" dapat dibaca sebagai verifikator yang berstatus.
   Usul: "Berkas diserahkan ke verifikator dan statusnya menjadi `verification in progress`."
3. **Contoh yang menyerupai teks peraturan nyata.**
   Contoh Bagian 6.5 menyerupai Pasal 2 ayat (1) UU 27/2022, dan contoh Bagian 6.7 menyerupai penjelasan Pasal 10 UU 27/2022, tetapi tampaknya diringkas tanpa tanda `…`.
   Bila contoh tidak sama persis dengan naskah, pembaca dapat mengira contoh tersebut kutipan yang setia.
   Usul: cocokkan dengan naskah (TODO.md), lalu salin persis dengan `…` untuk bagian yang dihilangkan, atau nyatakan sebagai contoh rekaan.
4. **Bagian 16.1: versi GFM.**
   CommonMark disebut dengan versi (0.31.2), tetapi GitHub Flavored Markdown Spec tidak.
   Usul: sebut versi spesifikasi GFM yang dipakai (perlu dipastikan; versi terbit terakhir yang dikenal adalah 0.29-gfm).
5. **Bagian 16.1: perubahan UU 12/2011.**
   "beserta perubahannya" sebaiknya menyebut perubahan secara eksplisit (perlu diverifikasi: UU 15/2019 dan UU 13/2022).
6. **Bagian 16.2: referensi yang tidak dirujuk.**
   ISO 14721 (OAIS) tidak dirujuk di mana pun dalam teks.
   Usul: hapus, atau rujuk dari Bagian 11 bila model arsip OAIS memang dijadikan acuan.
7. **Daftar isi dan lampiran.**
   Lampiran diberi nomor bagian sekaligus huruf ("14. Lampiran A").
   Gaya RFC hanya memakai huruf untuk lampiran.
   Usul (opsional): "Lampiran A. Contoh Berkas Minimal" tanpa nomor 14, dengan subbagian A.1 dan seterusnya.

## Dampak terhadap Berkas Transkripsi

Tidak ada.

## Kompatibilitas Versi

PATCH.

## Keputusan
