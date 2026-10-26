# Usulan 0013: Kelengkapan dan Konsistensi Skema Pengenal

| Identitas | Nilai |
|---|---|
| Nomor | 0013 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [I-1], [I-2], [I-8], [I-9], Bagian 1.2 |
| Jenis perubahan | penambahan; mungkin tidak kompatibel (butir 2) |
| Usulan versi berikutnya | MINOR |

## Latar Belakang

1. **Tabel jenis [I-1] lebih sempit daripada ruang lingkup Bagian 1.2.**
   Bagian 1.2 mencakup jenis peraturan menurut Pasal 7 dan Pasal 8 UU 12/2011.
   Pasal 8 ayat (1) menyebut antara lain peraturan yang ditetapkan oleh MPR, DPR, DPD, Mahkamah Agung, Mahkamah Konstitusi, BPK, Komisi Yudisial, Bank Indonesia, menteri, badan, lembaga, atau komisi yang setingkat, DPRD, gubernur, bupati/wali kota, dan kepala desa atau yang setingkat (daftar perlu dicocokkan dengan naskah Pasal 8).
   Tabel [I-1] tidak memuat kode untuk peraturan DPRD dan peraturan kepala desa.
   Tidak jelas pula apakah peraturan MPR, DPR, DPD, MA, MK, BPK, KY, dan BI termasuk `perlem`.
2. **Pembedaan tingkat daerah tidak konsisten.**
   Perda dibedakan menjadi `perda-prov` dan `perda-kabkota`, sedangkan `perkada` menggabungkan peraturan gubernur, bupati, dan wali kota.
   Kode wilayah sudah membedakan provinsi (dua digit) dari kabupaten/kota (empat digit).
3. **Kestabilan kode kementerian.**
   Nomenklatur kementerian dapat berubah, misalnya ketika kementerian dipecah atau digabung.
   [I-2] tidak menyatakan bahwa kode pembentuk mengikuti nomenklatur pada saat peraturan ditetapkan dan tidak berubah sesudahnya.
4. **Fragmen belum lengkap.**
   [I-8] tidak memuat pola untuk Buku, Bagian, Paragraf, ayat dalam Pasal yang dikutip di peraturan perubahan, atau unsur di dalam Lampiran.

## Rumusan Baru

1. Tambahkan baris tabel [I-1]: `perdprd-prov`, `perdprd-kabkota` (peraturan DPRD), `perkades` (peraturan kepala desa atau yang setingkat), dan perjelas `perlem` sebagai "Peraturan lembaga negara, badan, lembaga, atau komisi menurut Pasal 8 ayat (1) UU 12/2011".
   Kode akhir dipilih bersama penyusunan daftar kode (TODO.md).
2. Pilih salah satu: (a) satukan `perda-prov` dan `perda-kabkota` menjadi `perda`; atau (b) pecah `perkada` menjadi `pergub`, `perbup`, dan `perwali`.
   Pilihan (b) lebih mudah dibaca manusia dan tidak mengubah pengenal Perda yang sudah ada.
3. Tambahkan pada [I-2]:

```markdown
Kode pembentuk WAJIB mengikuti nomenklatur pembentuk pada tanggal penetapan peraturan dan TIDAK BOLEH diubah karena perubahan nomenklatur di kemudian hari.
```

4. Tambahkan pola fragmen `buku-{urutan}`, `bab-{romawi}-bagian-{urutan}`, `…-paragraf-{nomor}`, dengan `urutan` berupa bilangan (misalnya "Bagian Kesatu" menjadi `bagian-1`).

## Dampak terhadap Berkas Transkripsi

- Butir 1, 3, 4: tidak ada.
- Butir 2 pilihan (a) atau (b): pengenal dan nama berkas untuk jenis yang terdampak berubah.

## Kompatibilitas Versi

MINOR.

## Keputusan

2026-10-26, diputuskan oleh Claude atas kuasa Ananda Putra: **diterima**, butir 2 dengan pilihan (b).

Verifikasi fakta:

- Pasal 8 ayat (1) UU 12/2011 menyebut peraturan yang ditetapkan oleh MPR, DPR, DPD, Mahkamah Agung, Mahkamah Konstitusi, Badan Pemeriksa Keuangan, Komisi Yudisial, Bank Indonesia, Menteri, badan, lembaga, atau komisi yang setingkat, DPRD Provinsi, Gubernur, DPRD Kabupaten/Kota, Bupati/Walikota, dan Kepala Desa atau yang setingkat ([Wikisource](https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_12_Tahun_2011)).
- Pasal 69 ayat (1) UU 6/2014 mengenal Peraturan Desa, peraturan bersama Kepala Desa, dan peraturan Kepala Desa ([Wikisource](https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_6_Tahun_2014)).

Penerapan:

- Butir 1: ditambahkan `perdprd-prov`, `perdprd-kabkota`, `perdes`, dan `perkades`; `perlem` diperjelas dengan menyebut lembaga dalam Pasal 8 ayat (1).
  Peraturan bersama (misalnya peraturan bersama Kepala Desa atau peraturan bersama menteri) belum diberi kode dan dicatat di TODO.md.
- Butir 2 pilihan (b): `perkada` diganti `pergub`, `perbup`, dan `perwali`; pengenal Perda tidak berubah.
- Butir 3 diterapkan sesuai rumusan.
- Butir 4: fragmen Buku, Bagian, dan Paragraf ditambahkan.
  Tambahan: bila peraturan memiliki Buku, fragmen BAB, Bagian, dan Paragraf diawali fragmen Bukunya, karena penomoran BAB dapat dimulai ulang pada setiap Buku.

Diterapkan pada draf 0.1.0 tanpa menaikkan versi.
