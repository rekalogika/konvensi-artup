# TODO

Pekerjaan konvensi yang belum selesai.
Butir yang menyangkut fakta hukum tidak boleh diisi dari ingatan; cocokkan dengan sumber primer dan catat sumbernya.

## Keputusan yang ditunggu

- [ ] Putuskan usulan 0001 sampai 0015 dari tinjauan konsistensi pertama (lihat `usulan/`); 0003 sudah diputuskan.
- [x] Putuskan usulan 0003: diterima 2026-10-26 sebagai [R-6]; revisi ditampung di draf 0.1.0, dan 0.1.0 dirilis setelah usulan penting diterapkan.
- [ ] Putuskan apakah JSON Schema frontmatter berkas transkripsi menjadi lampiran normatif konvensi.
- [ ] Putuskan perlunya contoh uji (berkas contoh yang sesuai dan yang melanggar) sebagai bagian dari konvensi.

## Penyelarasan dengan acuan

- [ ] Selaraskan isian metadata (Bagian 9) dengan unsur metadata dalam lampiran Permenkumham 8/2019.
      Saat ini isian baru dipetakan ke format integrasi Portal JDIHN (Bagian 9.6).
- [ ] Verifikasi nama isian JDIHN di Bagian 9.6 (`singkatanJenis`, `noPeraturan`, `tempatTerbit`, `teuBadan`, `bidangHukum`, `tahun_pengundangan`, dan seterusnya) terhadap dokumentasi resmi format integrasi Portal JDIHN.
- [ ] Validasi pemetaan Akoma Ntoso (Lampiran B) terhadap skema resmi Akoma Ntoso 1.0 (OASIS), termasuk pola IRI manifestasi.
- [ ] Susun daftar kode kementerian/lembaga untuk skema pengenal (Bagian 10.2, [I-2]), termasuk aturan untuk perubahan nomenklatur (usulan 0013).
- [ ] Pastikan rujukan kode wilayah Kemendagri yang berlaku untuk [I-2].

## Fakta yang perlu diverifikasi (dari tinjauan pertama)

- [ ] Cocokkan contoh Bagian 6.5 dan 6.7 dengan naskah UU 27/2022 (Pasal 2 ayat (1) dan penjelasan Pasal 10), serta data UU 27/2022 di Bagian 9.5 dan Lampiran A (tanggal, LN 2022/196, TLN 6820, penandatangan) (usulan 0015).
- [ ] Nomor register Perda (Noreg): dasar hukum dan letaknya dalam naskah (usulan 0010).
- [ ] Kalimat pengesahan UU yang tidak ditandatangani Presiden: pasal dan ayat UU 12/2011 serta contoh naskah, misalnya UU 2/2018 (usulan 0010).
- [ ] Contoh peraturan yang Penjelasan atau Lampirannya diterbitkan sebagai berkas terpisah (usulan 0012).
- [ ] Contoh tabel dan rumus di batang tubuh, misalnya Pasal 17 UU Pajak Penghasilan (usulan 0009).
- [ ] Daftar jenis peraturan dalam Pasal 8 ayat (1) UU 12/2011 (usulan 0013).
- [ ] Perubahan UU 12/2011 untuk Lampiran C (UU 15/2019 dan UU 13/2022) dan versi spesifikasi GFM (usulan 0015).
- [ ] Contoh lampiran nyata yang memuat BAB dan subjudul bertingkat, sebagai dasar rumusan heading Lampiran (usulan 0008).

## Alat

- [ ] Perluas pemeriksa bila usulan 0002 diterima: `id` sama dengan pengenal teknis [R-5].
- [ ] Pertimbangkan pemeriksaan kata kunci normatif tanpa kode aturan (usulan 0005) di `alat/periksa_konvensi.py`.

## Tahap berikutnya

- [ ] Aturan tanda tangan digital dan timestamping bagi entri verifikasi dan register.
- [ ] Teks konsolidasi (pola nama berkas sudah dicadangkan di [I-6]).
- [ ] Seri dokumen standar bergaya RFC: penomoran seri, hubungan antardokumen, dan proses penerbitan.
