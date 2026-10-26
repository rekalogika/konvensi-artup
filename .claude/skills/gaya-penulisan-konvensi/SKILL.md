---
name: gaya-penulisan-konvensi
description: Pedoman gaya menulis teks Konvensi Artup, yaitu kata kunci normatif, satu kalimat per baris, format kode aturan, struktur bagian bergaya RFC, dan bahasa Indonesia baku. Pakai setiap kali menulis atau merumuskan teks untuk dokumen konvensi atau rumusan baru dalam usulan.
---

# Gaya penulisan konvensi

Acuan: RFC 7322 (gaya RFC), BCP 14 (kata kunci), ISO/IEC Directives Part 2 (perumusan ketentuan), KBBI dan EYD (bahasa).

## Kata kunci normatif

| Kata kunci | Pakai untuk |
|---|---|
| WAJIB | Persyaratan mutlak |
| TIDAK BOLEH | Larangan mutlak |
| SEBAIKNYA | Anjuran; penyimpangan dimungkinkan dengan alasan sah |
| SEBAIKNYA TIDAK | Anjuran untuk tidak melakukan |
| BOLEH | Pilihan bebas |

- Kata kunci selalu ditulis kapital dan hanya dengan arti Bagian 2.1.
- Dalam kalimat yang bukan ketentuan, pakai huruf kecil atau kata lain ("harus", "perlu", "dapat") agar tidak terbaca sebagai ketentuan.
- Jangan memakai sinonim normatif lain seperti "HARUS", "DILARANG", atau "DAPAT" berhuruf kapital.
- Satu ketentuan, satu kata kunci utama.
  Pecah kalimat yang mencampur WAJIB dan BOLEH bila keduanya bukan satu kesatuan.
- Subjek ketentuan jelas: "Badan teks WAJIB …", "Transkriptor TIDAK BOLEH …", "Verifikator …".

## Kode aturan

- Format: kurung siku, huruf kelompok, tanda hubung, nomor tanpa nol di depan: `[F-11]`.
  Kode pemeriksaan memakai dua digit: `L-07`.
- Kode diletakkan di awal paragraf ketentuan (`[S-9] Setiap ayat WAJIB …`) atau di awal butir daftar (`- [F-1] Berkas WAJIB …`).
- Kalimat lanjutan tanpa kode dalam paragraf yang sama termasuk ketentuan berkode tersebut.
- Rujukan dalam teks: `[S-9]`, atau rentang `[F-4] sampai [F-7]`; di kolom tabel Bagian 12 boleh tanpa kurung: `F-4 s.d. F-7`.
- Kelompok: P prinsip, F format, C cakupan, S struktur, N normalisasi, K notasi konvensi, M metadata, I pengenal, V verifikasi, R versi konvensi, L pemeriksaan otomatis.
  Kelompok baru hanya dengan persetujuan Ananda.
- Kode baru: nomor terbesar dalam kelompok ditambah satu.
  Kode tidak pernah dipakai ulang; aturan dihapus ditandai `[X-n] Dihapus dalam versi X.Y.Z.`

## Baris dan paragraf

- Satu kalimat per baris.
  Kalimat panjang tetap satu baris; jangan dipotong manual.
- Paragraf dipisahkan tepat satu baris kosong.
- Daftar diawali kalimat pengantar yang diakhiri titik dua.
  Butir diakhiri titik koma, butir terakhir diakhiri titik; atau semua butir berupa kalimat lengkap yang diakhiri titik.
- Sel tabel boleh berisi lebih dari satu kalimat bila tidak dapat dihindari.

## Struktur bagian (bergaya RFC)

Urutan dokumen: frontmatter, judul, tabel identitas, Abstrak, Status Dokumen Ini, Daftar Isi, bagian bernomor, lalu lampiran bernomor.

- Heading bagian bernomor: `## 6. Judul`, subbagian `### 6.5. Judul`, sub-subbagian `#### 6.5.1. Judul`.
  Nomor diakhiri titik.
- Judul bagian memakai huruf kapital di awal setiap kata kecuali kata tugas ("dan", "ke", "atas", "yang").
- Bagian pendahuluan berisi tujuan, ruang lingkup, dan hubungan dengan acuan; bagian istilah sebelum ketentuan.
- Lampiran diberi huruf (Lampiran A, B, …) dan ditandai "(Informatif)" bila tidak normatif.
- Tandai catatan nonnormatif dengan "Catatan:" di awal paragraf.
- Contoh ditandai "Contoh:" dan, bila berupa berkas transkripsi, ditulis dalam blok kode `markdown`.
  Contoh WAJIB mematuhi aturan konvensi sendiri.

## Bahasa

- Bahasa Indonesia baku sesuai KBBI dan EYD: "berkas" (bukan "file"), "pengenal" (bukan "ID"), "tautan", "unduh", "baris kosong".
- Istilah asing yang belum memiliki padanan baku ditulis miring pada kemunculan pertama, misalnya *linter*, *snake_case*.
  Nama standar, elemen XML, dan nilai isian ditulis sebagai kode sebaris.
- Istilah peraturan mengikuti Lampiran II UU 12/2011: "Pasal", "ayat", "huruf", "angka", "BAB", "Bagian", "Paragraf", "Penjelasan", "Lampiran".
- Istilah khusus konvensi didefinisikan di Bagian 2.2 dan dipakai konsisten; jangan memperkenalkan sinonim.
- Nilai status berkas transkripsi tetap dalam bahasa Inggris sebagaimana ditetapkan (`verified`, `superseded`, dan seterusnya).
- Tanggal dalam teks: format ISO `YYYY-MM-DD` untuk data, "26 Oktober 2026" untuk prosa.
- Hindari kata ganti orang pertama ("kami", "kita") dalam ketentuan.

## Format berkas

Dokumen konvensi wajib memenuhi Bagian 4.1: UTF-8 tanpa BOM, LF, NFC, tanpa tab, tanpa spasi di akhir baris, diakhiri satu LF, tanpa baris kosong berganda.
Pakai tanda pisah panjang `—` (U+2014) dan elipsis `…` (U+2026) sebagai satu karakter.
