# Usulan 0023: Kata Kunci pada Kalimat Lanjutan dan Perbaikan Redaksional Lain

| Identitas | Nilai |
|---|---|
| Nomor | 0023 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi kedua |
| Tanggal | 2026-10-27 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [S-6], [S-13], [S-14], [S-19], [S-20], [K-6], [I-9], [I-10], [V-14] |
| Jenis perubahan | redaksional |
| Usulan versi berikutnya | PATCH |

## Latar Belakang

Tinjauan konsistensi kedua, sebelum rilis 0.1.0, menemukan tiga jenis masalah redaksional.

### A. Kalimat lanjutan yang mengatur tanpa kata kunci

Ketentuan berikut memuat kata kunci pada kalimat pertamanya, tetapi kalimat lanjutannya juga mengatur, dan ditulis tanpa kata kunci.
Usulan 0005 sudah menangani kasus serupa, misalnya kalimat ketiga [S-2].
Pemeriksa `--gaya` tidak menangkapnya, karena paragrafnya sudah memuat kata kunci.

| Letak | Kalimat |
|---|---|
| [S-6], kalimat kedua dan ketiga | "kata tersebut berdiri sebagai paragraf sendiri dan rinciannya ditulis sebagai daftar …"; "rumusannya ditulis langsung setelah titik dua …" |
| [S-14], kalimat kedua | "Bagian utama Penjelasan memakai heading `##`, dan Pasal … memakai heading `#####`." |
| [S-19], kalimat kedua dan ketiga | "Label tersebut ditulis sebagai paragraf biasa …"; "Ayat dan rincian di dalam kutipan mengikuti Bagian 6.4 dan Bagian 6.5." |
| [S-20], kalimat kedua | "Heading di dalam Lampiran mengikuti label yang tertulis, dengan tingkat `##` sampai `####` …" |
| [K-6], kalimat pertama | "Notasi `{berkas:nama-berkas}` pada satu baris tersendiri menandai letak …" (syarat "satu baris tersendiri" hanya tersirat) |
| [I-9], kalimat ketiga | "Rincian bertingkat `a)` dan `1)` dirujuk dengan kata yang sama …" |

### B. Rumusan [V-14]

- "WAJIB tidak menimbulkan" bertentangan dengan pedoman gaya; bentuk yang benar adalah "TIDAK BOLEH menimbulkan".
- "kasus uji berhasil `sesuai`" dapat terbaca sebagai "kasus uji yang berhasil", padahal yang dimaksud adalah kasus uji yang isian `hasil`-nya `sesuai` (Bagian 17.2).

### C. Letak dan rujukan

- [I-10] terletak di tengah paragraf pembuka Bagian 10.1, padahal kode aturan diletakkan di awal paragraf (Bagian 2.1, pedoman gaya).
- [S-13] merujuk "menurut N-3" tanpa kurung siku, berbeda dengan bentuk rujukan di prosa lainnya.

## Rumusan Lama

```markdown
[S-6] … Apabila konsiderans atau dasar hukum terdiri atas beberapa rincian, kata tersebut berdiri sebagai paragraf sendiri dan rinciannya ditulis sebagai daftar menurut Bagian 6.5.
Apabila hanya terdiri atas satu rumusan tanpa label, rumusannya ditulis langsung setelah titik dua dalam paragraf yang sama.

[S-13] … Baris-baris dalam satu blok WAJIB digabung dengan satu spasi menurut N-3, misalnya …

[S-14] … Bagian utama Penjelasan memakai heading `##`, dan Pasal dalam penjelasan pasal demi pasal memakai heading `#####`.

[S-19] … Label tersebut ditulis sebagai paragraf biasa di dalam kutipan.
Ayat dan rincian di dalam kutipan mengikuti Bagian 6.4 dan Bagian 6.5.

[S-20] … Heading di dalam Lampiran mengikuti label yang tertulis, dengan tingkat `##` sampai `####` menurut hierarkinya.

[K-6] Notasi `{berkas:nama-berkas}` pada satu baris tersendiri menandai letak gambar, diagram, formulir, atau rumus yang disimpan sebagai berkas pendamping.

[I-9] … Rincian bertingkat `a)` dan `1)` dirujuk dengan kata yang sama (`huruf`, `angka`) secara berurutan menurut tingkatnya.

Skema pengenal diilhami templat URI ELI dan model FRBR.
Pengenal bersifat menjelaskan dirinya sendiri, stabil, dan tidak bergantung pada lokasi penyimpanan.
[I-10] Apabila diterbitkan di web, …

[V-14] Alat pemeriksa yang dipakai untuk [V-10] WAJIB tidak menimbulkan temuan pada berkas dasar di Lampiran D dan pada setiap kasus uji berhasil `sesuai`.
```

## Rumusan Baru

```markdown
[S-6] … Apabila konsiderans atau dasar hukum terdiri atas beberapa rincian, kata tersebut WAJIB berdiri sebagai paragraf sendiri dan rinciannya WAJIB ditulis sebagai daftar menurut Bagian 6.5.
Apabila hanya terdiri atas satu rumusan tanpa label, rumusannya WAJIB ditulis langsung setelah titik dua dalam paragraf yang sama.

[S-13] … Baris-baris dalam satu blok WAJIB digabung dengan satu spasi menurut [N-3], misalnya …

[S-14] … Bagian utama Penjelasan WAJIB memakai heading `##`, dan Pasal dalam penjelasan pasal demi pasal WAJIB memakai heading `#####`.

[S-19] … Label tersebut WAJIB ditulis sebagai paragraf biasa di dalam kutipan.
Ayat dan rincian di dalam kutipan WAJIB ditulis menurut Bagian 6.4 dan Bagian 6.5.

[S-20] … Heading di dalam Lampiran WAJIB mengikuti label yang tertulis, dengan tingkat `##` sampai `####` menurut hierarkinya.

[K-6] Letak gambar, diagram, formulir, atau rumus yang disimpan sebagai berkas pendamping WAJIB ditandai dengan notasi `{berkas:nama-berkas}` pada satu baris tersendiri.

[I-9] … Rincian bertingkat `a)` dan `1)` WAJIB dirujuk dengan kata yang sama (`huruf`, `angka`) secara berurutan menurut tingkatnya.

Skema pengenal diilhami templat URI ELI dan model FRBR.
Pengenal bersifat menjelaskan dirinya sendiri, stabil, dan tidak bergantung pada lokasi penyimpanan.

[I-10] Apabila diterbitkan di web, …

[V-14] Alat pemeriksa yang dipakai untuk [V-10] TIDAK BOLEH menimbulkan temuan pada berkas dasar di Lampiran D dan pada setiap kasus uji yang isian `hasil`-nya `sesuai`.
```

Bagian lain dari ketentuan-ketentuan tersebut tidak berubah.

## Dampak terhadap Berkas Transkripsi

Tidak ada.
Isi ketentuannya tetap sama; tingkat kewajiban yang selama ini tersirat kini dinyatakan dengan kata kunci.

## Kompatibilitas Versi

PATCH: perbaikan redaksional yang tidak mengubah ketentuan ([R-2]).

## Alternatif yang Dipertimbangkan

- Memperluas pemeriksa `--gaya` agar memeriksa setiap kalimat dalam ketentuan berkode: tidak dipilih, karena banyak kalimat lanjutan memang hanya menerangkan, misalnya kalimat kedua [S-10] dan [V-1], sehingga temuan keliru akan terlalu banyak.
- [S-20] kalimat ketiga ("Tabel, rumus, dan gambar di dalam Lampiran mengikuti Bagian 6.10.") tidak diubah, karena hanya menunjuk Bagian 6.10, yang sudah menyatakan berlaku di seluruh badan teks.

## Keputusan

2026-10-27, diputuskan oleh Claude atas kuasa Ananda Putra: diterima, sebagai bagian persiapan rilis 0.1.0.
Diterapkan pada draf 0.1.0 tanpa menaikkan versi.
