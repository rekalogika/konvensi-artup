---
name: rilis-konvensi
description: Merilis versi final Konvensi Artup, yaitu mengubah status dokumen menjadi final, membekukan salinan ke rilis/, menghitung SHA-256, mencatatnya di rilis/RILIS.md, dan membuat tag git. Pakai hanya bila Ananda secara eksplisit meminta merilis versi tertentu. Langkah ini tidak dapat dibatalkan; versi final tidak pernah diubah lagi.
---

# Rilis konvensi

Rilis bersifat permanen ([R-3]).
Minta konfirmasi Ananda atas nomor versi dan tanggal sebelum langkah 4, dan sekali lagi sebelum membuat tag.

## Langkah

1. **Prasyarat.**
   - Pohon kerja git bersih (`git status`).
   - `.venv/bin/python alat/periksa_konvensi.py --gaya` bersih, atau sisa temuan `--gaya` sudah diterima Ananda.
   - `.venv/bin/python alat/periksa_konvensi.py --rilis` bersih.
   - Tidak ada usulan berstatus `diterima` yang belum `diterapkan`.
   - Tinjau `TODO.md`: butir yang memblokir rilis sudah selesai atau secara sadar ditunda.
   - Disarankan: satu putaran skill `tinjau-konsistensi`.
2. **Tentukan versi** `X.Y.Z` dari frontmatter.
   Versi tersebut WAJIB belum ada di `rilis/RILIS.md` dan berkas `rilis/konvensi-artup-X.Y.Z.md` belum ada.
3. **Finalkan dokumen kerja** `konvensi/konvensi-artup.md`:
   - frontmatter: `status: final`, `tanggal:` tanggal rilis;
   - tabel identitas: Versi, Status `Final`, Tanggal, dan rujukan singkat `transkripsi-peraturan/X.Y`;
   - "Status Dokumen Ini": ganti menjadi
     "Dokumen ini berstatus **final**." dan "Isinya tidak akan diubah lagi; setiap perubahan diterbitkan sebagai versi baru (lihat Bagian 13)."
   - Lampiran D: pastikan baris versi `X.Y.Z` lengkap dan bertanggal rilis.
4. **Periksa ulang** dengan pemeriksa sampai bersih.
5. **Bekukan salinan** dengan menyalin byte demi byte, tanpa penyuntingan:
   ```sh
   cp konvensi/konvensi-artup.md rilis/konvensi-artup-X.Y.Z.md
   cmp konvensi/konvensi-artup.md rilis/konvensi-artup-X.Y.Z.md
   ```
6. **Hitung hash**:
   ```sh
   sha256sum rilis/konvensi-artup-X.Y.Z.md
   ```
7. **Catat di `rilis/RILIS.md`**: tambahkan satu baris di akhir tabel; hapus kalimat "Belum ada versi final." pada rilis pertama.
   ```markdown
   | X.Y.Z | YYYY-MM-DD | final | <sha256 heksadesimal huruf kecil> | Ringkasan |
   ```
   Hash tidak pernah dituliskan di dalam salinan beku itu sendiri.
8. **Verifikasi**: `.venv/bin/python alat/periksa_konvensi.py --rilis`.
9. **Commit**: `Rilis Konvensi Artup X.Y.Z`.
10. **Tag** (setelah konfirmasi): `git tag -a vX.Y.Z -m "Konvensi Artup X.Y.Z"`.
    Jangan `push` kecuali diminta.

## Setelah rilis

- Dokumen kerja dibiarkan identik dengan salinan beku sampai ada perubahan berikutnya.
  Perubahan pertama setelah rilis menaikkan versi dan mengembalikan status ke `draf` (skill `revisi-konvensi`).
- Bila ditemukan kesalahan dalam versi final, jangan menyunting salinan beku; terbitkan versi PATCH baru.
