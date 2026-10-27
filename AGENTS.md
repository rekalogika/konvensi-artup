# AGENTS.md

Instruksi untuk semua agen AI yang bekerja di repositori ini.

## Gambaran proyek

Repositori ini menyusun **Konvensi Artup**, yaitu dokumen konvensi untuk mentranskripsikan peraturan perundang-undangan Indonesia dari naskah sumber (umumnya PDF salinan resmi) ke berkas Markdown.
"Artup" adalah kata "putra" yang dibalik; nama ini bukan singkatan.
Penggagas dan penyusun: Ananda Putra.
Bahasa proyek: Bahasa Indonesia, untuk dokumen, pesan commit, dan komunikasi.

## Ruang lingkup

Proyek ini **hanya** untuk menyusun, memperbaiki, mengubah, dan merilis dokumen konvensi.

Pekerjaan transkripsi (berkas transkripsi, PDF sumber, register transkripsi, alat pemeriksa berkas transkripsi) dikerjakan di proyek terpisah dan **tidak** dibuat di sini.
Jika menemukan berkas transkripsi di repositori ini, misalnya `uu-2022-27.md`, jangan ubah berkas itu; tanyakan kepada Ananda apakah berkas itu perlu dipindahkan keluar.

## Peta folder

| Lokasi | Isi |
|---|---|
| `konvensi/konvensi-artup.md` | Dokumen kerja: draf yang sedang disunting; sumber kebenaran |
| `rilis/RILIS.md` | Daftar rilis: versi, tanggal, status, SHA-256, catatan |
| `rilis/konvensi-artup-X.Y.Z.md` | Salinan beku setiap versi final |
| `usulan/TEMPLAT.md` | Templat usulan revisi |
| `usulan/NNNN-judul-singkat.md` | Usulan revisi, satu berkas per usulan, bernomor urut empat digit |
| `alat/periksa_konvensi.py` | Pemeriksa dokumen konvensi |
| `alat/uji/` | Uji untuk pemeriksa itu sendiri |
| `.github/workflows/periksa.yml` | GitHub Actions: menjalankan uji dan pemeriksa pada setiap pull request |
| `TODO.md` | Pekerjaan konvensi yang belum selesai |
| `.claude/skills/` | Skill untuk alur kerja di bawah; dapat dibaca agen lain sebagai prosedur |

## Aturan emas

1. **Jangan mengubah isi normatif konvensi tanpa persetujuan eksplisit Ananda.**
   Isi normatif adalah setiap ketentuan berkode, tabel yang menjadi bagian ketentuan, definisi istilah, dan cakupan.
   Usulan perubahan ditulis dulu di `usulan/`.
   Perbaikan format murni (misalnya spasi di akhir baris) boleh langsung dilakukan dengan pemberitahuan.
2. **Berkas di `rilis/` selain `RILIS.md` tidak boleh diubah sama sekali.**
   Di `RILIS.md` hanya boleh ditambahkan baris baru; baris yang sudah ada tidak diubah.
3. **Kode aturan yang pernah terbit tidak boleh dipakai ulang untuk makna lain.**
   Seluruh kode dalam draf 0.1.0 dianggap sudah terbit, karena draf sudah dapat beredar ke peninjau.
   Aturan yang dihapus tetap dipertahankan kodenya dan ditandai, misalnya `[F-12] Dihapus dalam versi 0.2.0.`, bukan dinomori ulang.
   Kode baru memakai nomor terbesar dalam kelompoknya ditambah satu.
4. **Setiap perubahan normatif wajib tercatat di riwayat perubahan** (lampiran Riwayat Perubahan dokumen konvensi) dan mengikuti aturan versi Bagian 13 (semver, [R-1] sampai [R-3]).
5. **Dokumen konvensi wajib memenuhi aturan format Bagian 4.1:** UTF-8 tanpa BOM, LF, NFC, tanpa tab, tanpa spasi di akhir baris, diakhiri tepat satu LF, tanpa baris kosong berganda.
   Larangan konstruksi Markdown pada Bagian 4.2 dan escape pada Bagian 4.3 ditujukan untuk berkas transkripsi; dokumen konvensi memakai blok kode, huruf tebal, dan kode sebaris (Bagian 1.5).
6. **Jangan mengarang fakta hukum.**
   Ini mencakup nomor dan judul peraturan, isi pasal, tanggal, nama pejabat, nama isian JDIHN, unsur metadata Permenkumham 8/2019, dan nama elemen Akoma Ntoso.
   Jika belum terverifikasi terhadap sumber primer, tandai dengan jelas di teks usulan (misalnya "belum diverifikasi") dan catat di `TODO.md`.

## Keputusan yang sudah diambil

Keputusan berikut tidak boleh diubah tanpa persetujuan Ananda:

1. Tujuan: transkripsi setia 1:1 terhadap isi naskah sumber, mudah dibaca manusia dan AI, diverifikasi pihak ketiga, lalu dikunci dengan hash SHA-256 yang dicatat di register.
2. "1:1" berarti kesetiaan isi, bukan tata letak; nomor halaman, kop, footer, kata sambung antarhalaman, blok "Salinan sesuai dengan aslinya", dan cap tidak ditranskripsi.
3. Hash disimpan di register, bukan di berkas transkripsi; status: `new transcription`, `verification in progress`, `revision required`, `verified`, `superseded`.
4. Verifikator mencantumkan `hash_badan`; hash seluruh berkas dihitung setelah semua entri verifikasi ditambahkan.
5. Frontmatter berkas transkripsi hanya memuat metadata yang tidak berubah; status keberlakuan dan relasi masuk ada di register.
6. Teks yang belum pasti ditandai `{?…?}`.
7. Tanda tangan digital dan timestamping ditunda ke tahap berikutnya.
8. Nama dokumen "Konvensi Artup"; pengenal teknis yang dirujuk berkas transkripsi tetap `transkripsi-peraturan/MAYOR.MINOR` ([R-5]).
9. Acuan: Lampiran II UU 12/2011, Permenkumham 8/2019 dan format Portal JDIHN, ELI, FRBR/Akoma Ntoso, RFC 7322, BCP 14, ISO/IEC Directives Part 2.
10. Visi jangka panjang: seri dokumen standar bergaya RFC.

## Gaya penulisan

Rincian lengkap ada di `.claude/skills/gaya-penulisan-konvensi/SKILL.md`.
Ringkasnya:

- Kata kunci normatif ditulis kapital dan hanya dipakai dengan arti Bagian 2.1: **WAJIB**, **TIDAK BOLEH**, **SEBAIKNYA**, **SEBAIKNYA TIDAK**, **BOLEH**.
- Satu kalimat per baris; paragraf dipisahkan satu baris kosong.
- Setiap ketentuan normatif diberi kode aturan dalam kurung siku di awal, misalnya `[S-16]`.
  Kelompok kode: P (prinsip), F (format), C (cakupan), S (struktur), N (normalisasi), K (notasi konvensi), M (metadata), I (pengenal), V (verifikasi), R (versi konvensi); L-nn untuk pemeriksaan otomatis.
- Bahasa Indonesia baku sesuai KBBI dan EYD; istilah teknis yang dipakai harus didefinisikan di Bagian 2.2 atau dirujuk ke sumbernya.

## Perintah

Siapkan lingkungan sekali:

```sh
python3 -m venv .venv
.venv/bin/pip install -r alat/requirements.txt
```

Periksa dokumen kerja (tanpa argumen, pemeriksa memeriksa `konvensi/konvensi-artup.md`):

```sh
.venv/bin/python alat/periksa_konvensi.py
.venv/bin/python alat/periksa_konvensi.py --gaya   # tambah heuristik satu kalimat per baris
.venv/bin/python alat/periksa_konvensi.py --rilis  # cocokkan hash di rilis/RILIS.md
```

Keluaran berformat `berkas:baris: [kode] pesan`; kode keluar 0 bila bersih, 1 bila ada temuan, 2 bila berkas tidak dapat dibaca.

Uji pemeriksa:

```sh
.venv/bin/python -m unittest discover -s alat/uji -p 'uji_*.py'
```

Format byte berkas Markdown lain (README, usulan, skill, dan seterusnya):

```sh
git ls-files -z '*.md' ':!konvensi/konvensi-artup.md' | xargs -0 -r .venv/bin/python alat/periksa_konvensi.py --hanya-format
```

Ketiga perintah di atas (tanpa `--gaya`) juga dijalankan GitHub Actions pada setiap pull request; jalankan secara lokal sebelum mendorong branch agar pemeriksaan tidak gagal di sana.
`--gaya` juga dijalankan, tetapi temuannya tidak memblokir.

## Alur kerja

Setiap perubahan masuk ke `main` melalui pull request (lihat "Git" di bawah).

1. **Usulan**: tulis di `usulan/NNNN-judul-singkat.md` menurut templat (skill `usulan-revisi`) dan ajukan sebagai pull request.
2. **Diskusi dan persetujuan**: diskusi berlangsung di pull request usulan; Ananda memutuskan, dan status usulan diubah menjadi `diterima` atau `ditolak`.
3. **Penerapan**: dalam pull request tersendiri, sunting dokumen kerja, perbarui rujukan silang, daftar isi, riwayat perubahan, dan versi (skill `revisi-konvensi`).
4. **Pemeriksaan**: jalankan pemeriksa sebelum membuka pull request; tinjau konsistensi bila perubahannya luas (skill `tinjau-konsistensi`).
5. **Rilis** (bila diputuskan): dalam pull request rilis, ubah status, bekukan salinan ke `rilis/`, hitung SHA-256, dan catat di `rilis/RILIS.md`; setelah di-merge, buat tag git di `main` (skill `rilis-konvensi`).
   Langkah ini tidak dapat dibatalkan dan memerlukan persetujuan eksplisit.

### Versi dokumen kerja

Dokumen kerja selalu membawa nomor versi rilis berikutnya yang direncanakan.

- Jika versi di frontmatter belum tercantum di `rilis/RILIS.md`, perubahan dicatat di baris riwayat perubahan versi tersebut, tanpa menaikkan versi.
- Jika versi di frontmatter sudah dirilis, versi WAJIB dinaikkan menurut [R-2] sebelum perubahan pertama, dan status kembali menjadi `draf`.

## Git

Repositori: https://github.com/rekalogika/konvensi-artup (publik).

### Proteksi di GitHub

- `main` hanya dapat diubah melalui pull request; push langsung, force push, dan penghapusan ditolak.
- Pull request di-merge dengan **squash**, sehingga satu pull request menjadi satu commit di `main`, dan riwayat `main` selalu lurus.
- Semua percakapan di pull request harus diselesaikan sebelum merge.
- Pemeriksaan GitHub Actions "Periksa konvensi" harus lolos sebelum merge.
  Nama job ini dipakai di ruleset; jangan menggantinya tanpa memperbarui ruleset.
- Tag `v*` (tag rilis) tidak dapat diubah, dipindahkan, atau dihapus setelah dibuat.

### Branch

Buat branch dari `main` yang mutakhir (`git switch main && git pull --ff-only`), satu branch untuk satu perubahan yang utuh:

| Awalan | Isi | Contoh |
|---|---|---|
| `usulan/` | Satu berkas usulan baru, atau pencatatan keputusan atas usulan | `usulan/0016-tabel-dalam-ayat` |
| `revisi/` | Penerapan satu usulan yang diterima pada dokumen kerja | `revisi/0003-rujukan-versi-draf` |
| `rilis/` | Rilis satu versi final | `rilis/0.1.0` |
| `tinjauan/` | Hasil satu putaran tinjauan konsistensi (beberapa usulan sekaligus) | `tinjauan/2026-11` |
| `alat/` | Perubahan alat pemeriksa dan ujinya | `alat/pemeriksaan-kata-kunci` |
| `proyek/` | Berkas proyek lain: AGENTS.md, skill, README, TODO.md | `proyek/alur-pull-request` |

### Commit dan pull request

- Pesan commit dan judul pull request dalam bahasa Indonesia, ringkas, diawali kata kerja atau nomor usulan, misalnya `Terapkan usulan 0003: rujukan ke versi draf`.
- Judul dan deskripsi pull request menjadi pesan commit squash di `main`, jadi tulislah sebagai catatan perubahan yang utuh.
- Deskripsi pull request memuat: ringkasan, aturan dan usulan terdampak, jenis versi (PATCH, MINOR, MAYOR) bila normatif, dan hasil pemeriksa.
- Commit di dalam branch boleh beberapa; yang tersisa di `main` hanya commit squash.

### Batas tindakan agen

- Jangan push ke `main`, membuat atau mendorong tag, me-merge pull request, atau menulis ulang riwayat yang sudah di-push tanpa diminta.
- Mendorong branch kerja dan membuka pull request hanya bila diminta, misalnya "ajukan sebagai PR".
- Me-merge pull request adalah keputusan Ananda.
