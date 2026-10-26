---
name: tinjau-konsistensi
description: Meninjau dokumen Konvensi Artup secara menyeluruh untuk mencari kode aturan ganda, rujukan ke kode atau bagian yang tidak ada, kontradiksi antaraturan, istilah yang tidak didefinisikan, contoh yang melanggar aturan konvensi sendiri, dan daftar unsur tertutup Bagian 5 yang belum lengkap. Pakai sebelum rilis, setelah revisi besar, atau bila diminta meninjau konvensi. Hasilnya laporan dan usulan, bukan suntingan normatif.
---

# Tinjau konsistensi

## Langkah

1. **Pemeriksaan mesin.**
   Jalankan `.venv/bin/python alat/periksa_konvensi.py --gaya` dan catat temuannya.
   Pemeriksa sudah menangani format Bagian 4.1, frontmatter, kode ganda, rujukan kode dan bagian, daftar isi, dan blok kode; jangan mengulang pemeriksaan itu secara manual.
2. **Baca seluruh dokumen** dari awal sampai akhir, lalu periksa daftar di bawah.
3. **Laporkan** temuan, dikelompokkan menurut daftar periksa, masing-masing dengan nomor baris, kode aturan, penjelasan singkat, dan usulan penanganan.
4. **Tangani** di satu branch `tinjauan/YYYY-MM` (dibuat dari `main` yang mutakhir), yang diajukan sebagai satu pull request untuk seluruh putaran tinjauan.
   - Format murni: perbaiki langsung dan beritahukan.
   - Normatif: tulis sebagai usulan di `usulan/` menurut isi skill `usulan-revisi`; satu usulan per masalah atau per kelompok masalah yang saling terkait.
     **Pengecualian:** dalam tinjauan, langkah branch dan pull request skill `usulan-revisi` tidak dijalankan.
     Semua usulan hasil tinjauan dibuat dan di-commit di branch `tinjauan/YYYY-MM` yang sama; penomorannya tetap diperiksa terhadap pull request yang masih terbuka.
     Keputusan atas usulan-usulan itu dicatat kemudian, setelah pull request tinjauan di-merge, menurut alur biasa.
   - Fakta hukum yang meragukan: catat di `TODO.md`.

## Daftar periksa

### A. Kode aturan

- Kode ganda atau lompatan penomoran (pemeriksa).
- Ketentuan normatif (memuat WAJIB, TIDAK BOLEH, SEBAIKNYA, BOLEH) yang tidak berkode.
- Satu kode yang memuat beberapa ketentuan yang sebaiknya dipisah.
- Format kode yang tidak seragam, misalnya kode di tabel tanpa kurung siku.
- Kolom "Ketentuan" di Bagian 12: apakah setiap kode L benar-benar menguji ketentuan yang dirujuknya, dan apakah ada ketentuan yang dapat diperiksa mesin tetapi belum punya kode L.

### B. Rujukan

- Rujukan kode atau "Bagian n.n" yang tidak ada (pemeriksa).
- Rujukan yang ada tetapi salah sasaran, misalnya merujuk Bagian 9.3 untuk hal yang diatur di Bagian 9.4.

### C. Kontradiksi

- Dua aturan yang tidak dapat dipenuhi bersamaan.
- Pernyataan cakupan yang bertentangan dengan isi, misalnya Bagian 1.5 menyatakan seluruh Bagian 4 berlaku bagi dokumen konvensi sedangkan dokumen memakai konstruksi yang dilarang [F-10].
- Perbedaan tingkat kewajiban untuk hal yang sama di dua tempat.

### D. Istilah

- Istilah yang dipakai dengan arti khusus tetapi tidak ada di Bagian 2.2.
- Istilah di Bagian 2.2 yang tidak pernah dipakai.
- Satu konsep dengan dua nama, atau satu nama untuk dua konsep (misalnya "Bagian" sebagai unsur struktur peraturan dan "Bagian" sebagai bagian dokumen ini).

### E. Contoh

Setiap contoh, baik blok kode maupun contoh sebaris, wajib mematuhi aturan yang berlaku bagi berkas transkripsi.
Periksa setidaknya: escape [F-11] sampai [F-13], heading [S-1] sampai [S-4], rincian [S-10] sampai [S-12], kutipan [S-18] dan [S-19], frontmatter terhadap tabel Bagian 9.3 (isian WAJIB, tipe), pengenal [I-1] sampai [I-9], dan perhitungan hash [V-3].

### F. Daftar tertutup Bagian 5

- Bandingkan [C-1] dan [C-2] dengan unsur yang lazim ada di naskah menurut Lampiran II UU 12/2011 dan salinan resmi, misalnya: nomor register Perda (Noreg), tulisan "SALINAN" di halaman pertama, catatan tambahan di bawah Penjelasan, ralat, dan halaman kosong.
- Unsur yang tidak termasuk kedua daftar ditulis sebagai usulan, sebagaimana diminta Bagian 5.
- Jangan menyebut suatu unsur ada di naskah resmi tanpa contoh peraturan yang dapat dirujuk; bila belum pasti, catat di `TODO.md`.

### G. Kelengkapan dan gaya

- Isian yang dirujuk tetapi tidak didefinisikan, misalnya isian di frontmatter dokumen konvensi sendiri.
- Kata kunci normatif berhuruf kecil yang seharusnya normatif, atau sebaliknya.
- Lebih dari satu kalimat per baris (pemeriksa `--gaya`, lalu tinjau manual karena heuristik).
