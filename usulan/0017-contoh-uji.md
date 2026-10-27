# Usulan 0017: Contoh Uji sebagai Lampiran Normatif

| Identitas | Nilai |
|---|---|
| Nomor | 0017 |
| Pengusul | Claude (Anthropic), atas keputusan Ananda Putra |
| Tanggal | 2026-10-27 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | Bagian 12, [V-14] (baru), L-23 (baru), lampiran |
| Jenis perubahan | penambahan |
| Usulan versi berikutnya | MINOR |

## Latar Belakang

Konvensi belum memuat berkas contoh yang dapat dipakai untuk menguji alat pemeriksa berkas transkripsi.
Tanpa contoh bersama, dua alat dapat sama-sama mengaku sesuai konvensi, tetapi memberi hasil berbeda untuk berkas yang sama.

Ananda memutuskan (2026-10-27) bahwa contoh uji, berupa berkas contoh yang sesuai dan yang melanggar, menjadi bagian konvensi.

## Rumusan Baru

1. **Lampiran D (normatif): Contoh Uji**, dimuat di dalam dokumen agar ikut dibekukan dan ter-hash saat rilis:
   - Bagian 17.1: satu berkas dasar rekaan, `uu-2099-99.md` (Undang-Undang fiktif Nomor 99 Tahun 2099), yang memenuhi seluruh aturan dan mencakup frontmatter lengkap, pembukaan, BAB, Bagian, Pasal, ayat, rincian bersarang dengan escape, huruf miring, penutup, Penjelasan, dan keterangan penempatan;
   - Bagian 17.2: daftar kasus dalam YAML; setiap kasus adalah satu penggantian teks pada berkas dasar, dengan `hasil` (`sesuai`, `galat`, `peringatan`), `pemeriksaan` (kode L yang diharapkan), dan `aturan` yang diuji.
   Isinya rekaan agar tidak memuat klaim fakta hukum.
2. **[V-14]** di Bagian 12:

```markdown
[V-14] Alat pemeriksa yang dipakai untuk [V-10] WAJIB tidak menimbulkan temuan pada berkas dasar di Lampiran D dan pada setiap kasus uji berhasil `sesuai`.
Untuk setiap kasus uji lainnya, alat tersebut WAJIB menimbulkan sekurang-kurangnya satu temuan berkode yang tercantum pada isian `pemeriksaan` kasus itu.
```

3. **L-23** (baru): setiap paragraf dan butir daftar ditulis pada satu baris (N-3, [S-13]).
   Ketentuan ini sudah WAJIB sejak usulan 0004, tetapi belum memiliki kode pemeriksaan.
4. Lampiran Referensi dan Riwayat Perubahan bergeser menjadi Lampiran E dan F.

Kasus awal (26 kasus): 3 kasus `sesuai` (penanda keraguan di heading dan paragraf, angka diikuti titik tanpa spasi), 22 kasus `galat` yang mencakup L-01 sampai L-05, L-07, L-08, L-10, L-13, L-19, L-20, L-22, dan L-23, serta 1 kasus `peringatan` (L-11 dan L-12).

## Dampak terhadap Berkas Transkripsi

Tidak ada pada berkas transkripsi.
Alat pemeriksa berkas transkripsi (proyek terpisah) perlu lolos contoh uji ini menurut [V-14], dan perlu menambahkan L-23.

## Kompatibilitas Versi

MINOR (penambahan; MAYOR masih 0), ditampung di draf 0.1.0.

## Alternatif yang Dipertimbangkan

- Contoh uji sebagai berkas-berkas terpisah di folder `contoh-uji/`: tidak dipilih, karena daftar rilis mencatat satu berkas per versi dan berkas terpisah perlu mekanisme hash tersendiri.
- Contoh berdasarkan peraturan nyata: tidak dipilih, karena setiap kutipan harus diverifikasi terhadap naskah sumber dan nilai hash sumbernya harus nyata.

## Keputusan

2026-10-27, Ananda Putra: contoh uji yang sesuai dan yang melanggar menjadi bagian konvensi.
Rincian rumusan diputuskan oleh Claude atas kuasa Ananda.

Diterapkan pada draf 0.1.0 tanpa menaikkan versi.
Alat pemeriksa konvensi kini memverifikasi Lampiran D: berkas dasar lolos, setiap teks `dari` muncul tepat satu kali, setiap kode yang dirujuk didefinisikan dengan tingkat yang sesuai, dan setiap kasus menghasilkan temuan yang ditetapkan sejauh dapat dinilai alat ini (format byte, JSON Schema, [I-4], dan [M-8]).
Pemeriksaan struktur badan teks (misalnya L-07, L-08, L-10) di luar jangkauan alat ini dan menjadi tanggung jawab alat pemeriksa berkas transkripsi.
