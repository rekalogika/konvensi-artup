# TODO

Pekerjaan konvensi yang belum selesai.
Butir yang menyangkut fakta hukum tidak boleh diisi dari ingatan; cocokkan dengan sumber primer dan catat sumbernya.
Butir yang sudah selesai dihapus dari daftar ini; jejaknya ada di `usulan/` dan riwayat git.

## Keputusan yang ditunggu

- [ ] Ananda: apakah repositori ini nantinya juga akan memuat konvensi lain selain konvensi transkripsi peraturan?
  Bila ya, nama "Konvensi Artup" dapat menjadi nama seri, dan dokumen kerja `konvensi/konvensi-artup.md` sebaiknya dinamai menurut `id`-nya, yaitu `konvensi/transkripsi-peraturan.md`.
  Hal yang perlu ikut dipertimbangkan:
  - [R-5] menyebut "Konvensi Artup" sebagai nama dokumen ini;
  - salinan beku `rilis/konvensi-artup-0.1.0.md` tidak dapat diganti namanya ([R-3]);
  - pola nama salinan beku, pemeriksa (`alat/periksa_konvensi.py`), AGENTS.md, dan skill perlu disesuaikan.
  Berkaitan dengan butir seri dokumen standar di "Tahap berikutnya".

## Fakta yang perlu diverifikasi

- [ ] Cari contoh naskah UU yang sah tanpa tanda tangan Presiden untuk Lampiran A atau contoh uji.
- [ ] Contoh peraturan yang Penjelasan atau Lampirannya diterbitkan sebagai berkas terpisah (usulan 0012).
- [ ] Contoh tabel dan rumus di batang tubuh, misalnya Pasal 17 UU Pajak Penghasilan (usulan 0009).
- [ ] Kode jenis untuk peraturan bersama (misalnya peraturan bersama Kepala Desa, peraturan bersama menteri) pada [I-1].
- [ ] Contoh lampiran nyata yang memuat BAB dan subjudul bertingkat, sebagai dasar rumusan heading Lampiran (usulan 0008).

## Tahap berikutnya

- [ ] Aturan tanda tangan digital dan timestamping bagi entri verifikasi dan register.
- [ ] Teks konsolidasi (pola nama berkas sudah dicadangkan di [I-6]).
- [ ] Seri dokumen standar bergaya RFC: penomoran seri, hubungan antardokumen, dan proses penerbitan.
- [ ] Tingkat mutu berkas transkripsi, misalnya berkas berstatus `new transcription` bermutu terendah dan berkas berstatus `verified` bermutu tertinggi.
  Status `verified` haruslah hasil verifikasi oleh manusia.
  Saat ini definisi Verifikator di Bagian 2.2 hanya menyebut "pihak", sedangkan Transkriptor dapat berupa "orang atau proses".
  Perlu dipertimbangkan apakah tingkat mutu cukup diturunkan dari status di register (Bagian 11.1) atau memerlukan isian tersendiri, misalnya untuk membedakan berkas hasil ketik ganda dan berkas hasil OCR yang belum diverifikasi.
