# Usulan 0018: Penyelarasan Metadata dengan Permenkumham 8/2019 dan Portal JDIHN

| Identitas | Nilai |
|---|---|
| Nomor | 0018 |
| Pengusul | Claude (Anthropic), atas keputusan Ananda Putra |
| Tanggal | 2026-10-27 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | Bagian 1.4, 9.3 (keterangan `karya.teu_badan` dan `karya.bidang_hukum`), 9.6, lampiran Referensi |
| Jenis perubahan | redaksional |
| Usulan versi berikutnya | PATCH |

## Latar Belakang

Bagian 9.6 hanya memetakan isian ke format integrasi Portal JDIHN, dan menyatakan bahwa penyelarasan dengan unsur metadata Permenkumham 8/2019 ditunda.
Nama isian JDIHN juga belum diverifikasi terhadap sumber resmi (TODO.md).

## Hasil Verifikasi

- **Permenkumham 8/2019** ([JDIH BPK](https://peraturan.bpk.go.id/Details/133122/permenkumham-no-8-tahun-2019); Berita Negara Tahun 2019 Nomor 692; berstatus berlaku dan tidak diubah atau dicabut menurut halaman tersebut).
  Lampiran BAB III huruf A (Standar Metadata Peraturan) memuat 15 unsur: Tipe Dokumen, Judul, T.E.U. Badan/Pengarang, Nomor Peraturan, Jenis/Bentuk Peraturan, Singkatan Jenis/Bentuk Peraturan, Tempat Penetapan, Tanggal-Bulan-Tahun Penetapan/Pengundangan, Sumber, Subjek, Status, Bahasa, Lokasi, Bidang Hukum, dan Lampiran.
  Sumber dicatat sebagai singkatan sumber, tahun dan nomor, serta jumlah halaman, misalnya `LN 2011 (82): 51 hlm.`
  BAB IV (Integrasi JDIHN) tidak menetapkan nama isian; integrasi dilakukan melalui API dan pemetaan basis data.
  Naskah dibaca dari PDF hasil pindaian, sehingga ejaan nama unsur di atas dinormalkan dari teks OCR.
- **Format integrasi Portal JDIHN**: contoh feed resmi BPHN dalam paket aplikasi ILDIS ([bphndigitalservice/ildis](https://github.com/bphndigitalservice/ildis), berkas `feed/dokumen.json`) memuat isian `idData`, `tahun_pengundangan`, `tanggal_penetapan`, `tanggal_pengundangan`, `jenis`, `noPeraturan`, `judul`, `noPanggil`, `singkatanJenis`, `tempatTerbit`, `penerbit`, `deskripsiFisik`, `sumber`, `isbn`, `status`, `bahasa`, `bidangHukum`, `teuBadan`, `nomorIndukBuku`, `abstrak`, `last_updated`, `urlAbstrak`, `urlDetailPeraturan`, `fileDownload`, `urlDownload`, `subjek`, `operasi`, dan `display`.
  Semua nama isian JDIHN yang dipakai di Bagian 9.6 terdapat di sana.

## Rumusan Baru

- Bagian 9.6 menjadi tabel empat kolom: unsur Permenkumham 8/2019, isian konvensi, isian Portal JDIHN, dan catatan, yang mencakup ke-15 unsur dan seluruh isian feed JDIHN.
- Bagian 1.4: sifat acuan metadata menjadi "Diselaraskan: setiap unsur metadata peraturan dipetakan (Bagian 9.6)".
- Keterangan `karya.teu_badan` dan `karya.bidang_hukum` di Bagian 9.3 merujuk pedoman dalam lampiran Permenkumham 8/2019.
- Lampiran Referensi: nomor Berita Negara Permenkumham 8/2019 dan rujukan ke contoh feed ILDIS.

Tidak ada isian frontmatter baru: unsur yang belum berpadanan (Tipe Dokumen, Lokasi, Lampiran) tidak berlaku untuk berkas transkripsi atau diisi oleh portal.

## Dampak terhadap Berkas Transkripsi

Tidak ada.

## Kompatibilitas Versi

PATCH, ditampung di draf 0.1.0.

## Keputusan

2026-10-27, Ananda Putra: laksanakan seluruh usulan penyelarasan dengan acuan.
Rincian diputuskan oleh Claude atas kuasa Ananda.
Diterapkan pada draf 0.1.0 tanpa menaikkan versi.
