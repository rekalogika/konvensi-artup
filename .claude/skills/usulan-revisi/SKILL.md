---
name: usulan-revisi
description: Menuliskan usulan perubahan Konvensi Artup sebagai berkas baru di usulan/. Pakai setiap kali ada gagasan, temuan, atau masukan (termasuk dari ahli hukum, asosiasi, atau pihak luar lain) yang akan mengubah isi normatif konvensi, sebelum dokumen kerja disunting. Jangan dipakai untuk perbaikan format murni.
---

# Usulan revisi

Usulan adalah satu-satunya jalan masuk perubahan normatif.
Skill ini **tidak** menyunting `konvensi/konvensi-artup.md`.

## Langkah

1. **Tentukan nomor.**
   Lihat `usulan/` dan ambil nomor empat digit terbesar ditambah satu (mulai dari `0001`).
   Nama berkas: `usulan/NNNN-judul-singkat.md`, judul singkat huruf kecil dengan tanda hubung.
2. **Salin `usulan/TEMPLAT.md`** dan isi seluruh bagiannya.
   Status awal: `diajukan`.
3. **Latar belakang.**
   Kutip rumusan yang bermasalah beserta kode aturan dan nomor bagiannya.
   Sertakan contoh konkret: kutipan naskah sumber, potongan berkas transkripsi, atau kasus yang tidak tertangani.
4. **Aturan terdampak.**
   Cari semua rujukan ke aturan tersebut di dokumen kerja, misalnya `grep -n 'S-16' konvensi/konvensi-artup.md`, termasuk kolom "Ketentuan" di tabel Bagian 12 dan rentang "s.d.".
   Daftarkan semuanya.
5. **Rumusan lama dan baru.**
   Kutip rumusan lama persis.
   Tulis rumusan baru sesuai skill `gaya-penulisan-konvensi`.
   Kode baru: nomor terbesar dalam kelompok ditambah satu.
   Aturan yang dihapus tetap memakai kodenya dengan tanda "Dihapus dalam versi X.Y.Z."
6. **Dampak terhadap berkas transkripsi.**
   Jawab: apakah berkas yang sesuai versi sebelumnya menjadi tidak sesuai, apakah berkas `verified` terdampak ([R-4]), dan apakah alat pemeriksa berkas transkripsi (proyek terpisah) perlu diubah.
7. **Kompatibilitas versi.**
   Pilih PATCH, MINOR, atau MAYOR menurut [R-2] dan beri alasan.
   Ingat: selama MAYOR bernilai 0, MINOR boleh tidak kompatibel, tetapi ketidakcocokannya tetap harus dinyatakan.
8. **Alternatif** yang dipertimbangkan beserta alasan tidak dipilih.
9. Biarkan bagian **Keputusan** kosong; itu diisi Ananda.

## Usulan dari pihak luar

- Tulis nama dan afiliasi pengusul di kolom Pengusul, misalnya `Nama (Asosiasi X), dituliskan oleh Claude`.
- Kutip masukan aslinya apa adanya di Latar Belakang, ditandai sebagai kutipan `>`, terpisah dari analisis.
- Bila masukan menyangkut fakta hukum (isi pasal, nomor peraturan, unsur metadata JDIHN), jangan menambahkan fakta yang tidak diberikan pengusul dan tidak dapat diverifikasi; catat sebagai hal yang perlu diverifikasi.

## Satu usulan, satu masalah

Pecah masukan yang berisi beberapa masalah independen menjadi beberapa usulan, agar setiap usulan dapat diterima atau ditolak sendiri-sendiri.
Masalah yang saling terkait boleh digabung dengan menjelaskan kaitannya.

## Setelah selesai

Laporkan kepada Ananda: nomor dan judul usulan, aturan terdampak, dan usulan jenis versi.
Commit berkas usulan dengan pesan, misalnya `Usulan 0003: ...`, bila diminta.
