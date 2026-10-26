---
name: revisi-konvensi
description: Menerapkan perubahan yang SUDAH disetujui Ananda ke dokumen kerja konvensi/konvensi-artup.md, yaitu menyunting aturan, memberi kode aturan baru, menandai aturan yang dihapus, memperbarui rujukan silang, daftar isi, tabel pemeriksaan Bagian 12, riwayat perubahan, dan versi. Pakai setelah sebuah usulan berstatus diterima atau Ananda menyetujui perubahan secara eksplisit dalam percakapan.
---

# Revisi konvensi

## Syarat

- Ada persetujuan eksplisit: usulan di `usulan/` berstatus `diterima`, atau Ananda menyetujui rumusan tertentu dalam percakapan.
  Tanpa itu, berhenti dan pakai skill `usulan-revisi`.
- Perbaikan format murni (spasi di akhir baris, baris kosong berganda, NFC) boleh tanpa usulan, tetapi tetap diberitahukan.

## Langkah

1. **Baca konteks.**
   Baca bagian yang diubah dan bagian yang merujuknya.
   Cari semua rujukan kode yang terdampak: `grep -nE '\bS-1[0-9]\b' konvensi/konvensi-artup.md`.
2. **Tentukan versi** (lihat "Versi dokumen kerja" di AGENTS.md).
   - Periksa `rilis/RILIS.md`.
     Bila versi di frontmatter sudah dirilis, naikkan dulu menurut [R-2], set `status: draf`, dan tambahkan baris baru di riwayat perubahan.
   - Bila belum dirilis, perubahan ditambahkan ke baris riwayat versi tersebut.
   - Perubahan MAYOR.MINOR juga mengubah rujukan singkat `transkripsi-peraturan/MAYOR.MINOR` di tabel identitas dan di contoh (Bagian 9.5, 11.5, Lampiran A).
3. **Sunting aturan.**
   - Ikuti skill `gaya-penulisan-konvensi`.
   - Kode baru: nomor terbesar dalam kelompoknya ditambah satu, walaupun letaknya di tengah bagian.
     Urutan kode tidak harus sama dengan urutan tampil.
   - Aturan dihapus: pertahankan baris kodenya, ganti isinya dengan `[X-n] Dihapus dalam versi X.Y.Z.` dan, bila ada, `Lihat [X-m].`
   - Jangan memakai ulang kode lama untuk makna lain, walaupun kodenya sudah dihapus.
4. **Perbarui rujukan silang.**
   - Rujukan kode `[X-n]` dalam teks.
   - Kolom "Ketentuan" tabel Bagian 12, termasuk rentang `X-a s.d. X-b`.
   - Rujukan "Bagian n.n".
     Hindari menomori ulang bagian; tambahkan subbagian baru di akhir induknya bila memungkinkan.
     Bila penomoran ulang tidak terhindarkan, perbarui semua rujukan dan catat di riwayat perubahan.
   - Tabel istilah Bagian 2.2 bila ada istilah baru.
   - Contoh (Bagian 6, 9.5, Lampiran A) agar tetap sesuai aturan baru.
5. **Daftar isi** bila heading tingkat dua berubah.
6. **Identitas dan riwayat.**
   - Frontmatter `versi`, `tanggal` (hari ini), dan tabel identitas di awal dokumen.
   - Lampiran D: satu baris per versi; isi kolom Perubahan dengan ringkasan yang menyebut kode aturan dan nomor usulan, misalnya `Mengubah [S-16] (usulan 0003).`
7. **Periksa.**
   Jalankan `.venv/bin/python alat/periksa_konvensi.py` dan perbaiki sampai bersih.
8. **Tutup usulan.**
   Ubah status usulan menjadi `diterapkan` dan isi versi penerapannya di bagian Keputusan.
9. **Commit.**
   Satu commit per usulan, misalnya `Terapkan usulan 0003: gabungan label penjelasan [S-16]`.

## Jangan

- Jangan menyunting berkas di `rilis/`.
- Jangan "sekalian" memperbaiki aturan lain yang tidak termasuk persetujuan; tulis sebagai usulan baru.
- Jangan menambah fakta hukum yang belum diverifikasi; catat di `TODO.md`.
