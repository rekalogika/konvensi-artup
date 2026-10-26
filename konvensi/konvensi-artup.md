---
id: transkripsi-peraturan
nama: Konvensi Artup
judul: Konvensi Artup — Konvensi Transkripsi Peraturan Perundang-undangan ke Format Markdown
versi: 0.1.0
status: draf
tanggal: 2026-10-26
bahasa: ind
penyusun:
  - nama: Ananda Putra
    peran: penggagas dan penyusun
  - nama: Claude (Anthropic)
    peran: penulis draf
menggantikan: null
---

# Konvensi Artup

Konvensi Transkripsi Peraturan Perundang-undangan ke Format Markdown

| Identitas | Nilai |
|---|---|
| Nama | Konvensi Artup |
| Pengenal | `transkripsi-peraturan` |
| Versi | 0.1.0 |
| Status | Draf |
| Tanggal | 2026-10-26 |
| Penyusun | Ananda Putra (penggagas dan penyusun); Claude, model AI buatan Anthropic (penulis draf) |
| Menggantikan | — |
| Rujukan singkat dalam berkas transkripsi | `transkripsi-peraturan/0.1` |

## Abstrak

Dokumen ini, yang disebut Konvensi Artup, menetapkan konvensi untuk mentranskripsikan peraturan perundang-undangan Indonesia ke dalam berkas teks berformat Markdown.
Tujuannya adalah menghasilkan berkas yang setia isinya terhadap naskah sumber, dapat dibaca manusia maupun mesin, dapat diverifikasi oleh pihak ketiga, dan dapat dikunci dengan nilai hash setelah diverifikasi.
Konvensi ini mengatur format berkas, pemetaan struktur naskah, metadata, skema pengenal, notasi khusus, daur hidup verifikasi, dan pemeriksaan otomatis.

## Status Dokumen Ini

Dokumen ini berstatus **draf**.
Isinya dapat berubah sebelum ditetapkan sebagai versi final.
Versi final tidak akan diubah lagi; setiap perubahan setelahnya diterbitkan sebagai versi baru (lihat Bagian 13).

## Daftar Isi

1. Pendahuluan
2. Kata Kunci Normatif dan Istilah
3. Prinsip Dasar
4. Format Berkas
5. Cakupan Isi: Unsur yang Ditranskripsi dan Dikecualikan
6. Struktur Naskah dan Pemetaan Markdown
7. Normalisasi Teks
8. Notasi Konvensi
9. Metadata (Frontmatter)
10. Skema Pengenal
11. Daur Hidup, Verifikasi, dan Hash
12. Pemeriksaan Otomatis
13. Pengelolaan Versi Konvensi
14. Lampiran A: Contoh Berkas Minimal
15. Lampiran B: Pemetaan ke Akoma Ntoso (Informatif)
16. Lampiran C: Referensi
17. Lampiran D: Riwayat Perubahan

## 1. Pendahuluan

### 1.1. Tujuan

Naskah resmi peraturan perundang-undangan umumnya tersedia dalam bentuk PDF hasil pindaian.
Bentuk ini sulit diolah mesin dan rawan salah baca ketika dikonversi dengan OCR.
Konvensi ini menetapkan cara menuangkan isi naskah tersebut ke dalam teks Markdown sehingga:

- isinya setia terhadap naskah sumber dan dapat dibuktikan kesetiaannya melalui verifikasi;
- strukturnya (BAB, Pasal, ayat, dan seterusnya) dapat dikenali secara pasti oleh mesin;
- tampilannya tetap nyaman dibaca manusia melalui penampil Markdown biasa;
- setiap berkas yang sudah diverifikasi dapat dikunci dengan nilai hash.

### 1.2. Ruang Lingkup

Konvensi ini berlaku untuk jenis peraturan perundang-undangan sebagaimana dimaksud dalam Pasal 7 dan Pasal 8 Undang-Undang Nomor 12 Tahun 2011 tentang Pembentukan Peraturan Perundang-undangan beserta perubahannya.

Versi 0.1 hanya mengatur transkripsi **teks asli**, yaitu teks sebagaimana ditetapkan dan diundangkan.
Teks konsolidasi (teks yang menggabungkan perubahan-perubahan) berada di luar cakupan versi ini; konvensi hanya mencadangkan pola penamaannya (Bagian 10.5).

### 1.3. Kedudukan Hukum Hasil Transkripsi

Berkas transkripsi bukan naskah resmi.
Naskah yang sah tetap naskah yang dimuat dalam Lembaran Negara, Berita Negara, Lembaran Daerah, atau Berita Daerah.
Verifikasi menurut konvensi ini menyatakan kesesuaian isi berkas terhadap naskah sumber yang disebut dalam metadata, bukan keabsahan hukum berkas tersebut.

### 1.4. Hubungan dengan Acuan Lain

| Aspek | Acuan | Sifat |
|---|---|---|
| Struktur naskah | Lampiran II UU 12/2011 beserta perubahannya | Normatif: konvensi mengikuti struktur yang ditetapkan di sana |
| Isian metadata | Permenkumham 8/2019 dan format integrasi Portal JDIHN | Dipetakan secara informatif (Bagian 9.6); penyelarasan dengan Permenkumham 8/2019 belum dilakukan |
| Skema pengenal | European Legislation Identifier (ELI) | Diilhami: pola, bukan implementasi resmi |
| Model karya, ekspresi, manifestasi | FRBR sebagaimana dipakai Akoma Ntoso | Diilhami: pemisahan tingkat identitas |
| Gaya dokumen ini | RFC 7322, BCP 14, ISO/IEC Directives Part 2 | Diilhami |

### 1.5. Penerapan pada Dokumen Ini

Dokumen konvensi ini sendiri ditulis dalam Markdown dan tunduk pada aturan pengodean dan baris di Bagian 4.1.
Aturan lain dalam konvensi ini, termasuk Bagian 4.2 dan Bagian 4.3, berlaku untuk berkas transkripsi, bukan untuk dokumen ini.

## 2. Kata Kunci Normatif dan Istilah

### 2.1. Kata Kunci Normatif

Kata kunci berikut, apabila ditulis dengan huruf kapital, memiliki arti sebagaimana dijelaskan di bawah ini.
Penggunaannya meniru BCP 14 (RFC 2119 dan RFC 8174).

| Kata kunci | Arti |
|---|---|
| **WAJIB** | Persyaratan mutlak. Berkas yang tidak memenuhinya tidak sesuai konvensi. |
| **TIDAK BOLEH** | Larangan mutlak. |
| **SEBAIKNYA** | Dianjurkan. Penyimpangan dimungkinkan dengan alasan yang sah dan dipahami akibatnya. |
| **SEBAIKNYA TIDAK** | Tidak dianjurkan. Pelaksanaan dimungkinkan dengan alasan yang sah dan dipahami akibatnya. |
| **BOLEH** | Pilihan bebas. |

Kata yang sama yang ditulis dengan huruf kecil memiliki arti sehari-hari.

Setiap ketentuan normatif diberi kode dalam kurung siku, misalnya [F-3].
Kode tersebut dipakai untuk merujuk ketentuan dalam laporan verifikasi dan hasil pemeriksaan otomatis.

### 2.2. Istilah

| Istilah | Definisi |
|---|---|
| Naskah sumber | Berkas atau dokumen yang menjadi acuan transkripsi, misalnya PDF salinan resmi. |
| Berkas transkripsi | Berkas Markdown yang dihasilkan menurut konvensi ini. |
| Frontmatter | Blok metadata YAML di awal berkas transkripsi. |
| Badan teks | Seluruh isi berkas transkripsi setelah frontmatter. |
| Berkas pendamping | Berkas selain berkas transkripsi, misalnya gambar atau diagram, yang dirujuk dengan notasi `{berkas:…}` (Bagian 8.3). |
| Teks asli | Teks peraturan sebagaimana ditetapkan dan diundangkan, tanpa penggabungan perubahan. |
| Teks konsolidasi | Teks yang menggabungkan suatu peraturan dengan perubahan-perubahannya pada suatu titik waktu; berada di luar cakupan versi ini (Bagian 1.2). |
| Peraturan perubahan | Peraturan yang mengubah peraturan lain, umumnya melalui Pasal berangka Romawi (Bagian 6.8). |
| Komponen naskah | Salah satu dari: naskah utama (judul, pembukaan, batang tubuh, dan penutup), Penjelasan, atau Lampiran. Dalam isian `ekspresi.komponen`, naskah utama ditulis `batang-tubuh`. |
| Pembukaan | Bagian naskah antara judul dan batang tubuh: frasa "DENGAN RAHMAT TUHAN YANG MAHA ESA", jabatan pembentuk, konsiderans, dasar hukum, frasa persetujuan bersama, dan diktum ([C-1] butir 2 sampai 7). |
| Konsiderans | Unsur pembukaan yang diawali kata "Menimbang". |
| Dasar hukum | Unsur pembukaan yang diawali kata "Mengingat". |
| Diktum | Unsur pembukaan yang memuat "MEMUTUSKAN:" dan "Menetapkan:" beserta nama peraturan yang ditetapkan. |
| Batang tubuh | Bagian naskah antara pembukaan dan penutup yang memuat Pasal-Pasal beserta pengelompokannya dalam Buku, BAB, Bagian, dan Paragraf. |
| Penutup | Bagian naskah setelah batang tubuh yang memuat unsur [C-1] butir 9 sampai 11 dan butir 14. |
| Unsur struktur | Satuan susunan naskah: Buku, BAB, Bagian, Paragraf, Pasal, ayat, dan rincian. |
| Rincian | Unsur bertanda huruf atau angka di dalam Pasal atau ayat, misalnya `a.`, `1.`, `a)`, `1)`. |
| Label | Penanda unsur sebagaimana tertulis di naskah, misalnya "Pasal 5", "(2)", "a.", atau "Huruf a" dalam penjelasan pasal demi pasal. |
| Notasi konvensi | Tanda yang ditambahkan oleh konvensi dan bukan teks sumber (Bagian 8). |
| Penanda keraguan | Notasi `{?…?}` untuk teks yang belum dipastikan sesuai sumber. |
| Karya | Peraturan sebagai entitas hukum abstrak, misalnya UU 27/2022. |
| Ekspresi | Teks karya pada suatu titik waktu dan bahasa tertentu, misalnya teks asli tanggal pengundangan. |
| Manifestasi | Perwujudan ekspresi dalam format tertentu, misalnya PDF Setneg atau berkas transkripsi ini. |
| Register | Daftar seluruh berkas transkripsi beserta status dan nilai hashnya (Bagian 11.5). |
| Transkriptor | Orang atau proses yang menghasilkan berkas transkripsi. |
| Verifikator | Pihak yang membandingkan berkas transkripsi dengan naskah sumber dan menyatakan kesesuaiannya. |
| Entri verifikasi | Butir dalam isian `verifikasi` yang mencatat satu verifikator dan hasil pemeriksaannya (Bagian 9.4). |
| Ketik ganda | Metode transkripsi berupa dua transkripsi independen yang dibandingkan secara otomatis ([V-2]). |
| Pengenal teknis | Pengenal konvensi yang dirujuk berkas transkripsi, yaitu `transkripsi-peraturan` ([R-5]). |
| Daftar rilis konvensi | Daftar versi final konvensi beserta nilai hashnya, yang dikelola bersama dokumen konvensi ([R-3]). |

Catatan: istilah teknik penyusunan peraturan (pembukaan, konsiderans, dasar hukum, diktum, batang tubuh, penutup) dipakai dengan arti yang sama seperti dalam Lampiran II UU 12/2011; definisi di atas hanya merangkum letaknya dalam naskah.

Catatan: "Bagian" dan "Paragraf" berhuruf awal kapital yang diikuti bilangan tingkat (misalnya "Bagian Kesatu", "Paragraf 1") merujuk unsur struktur peraturan.
"Bagian" yang diikuti nomor angka (misalnya "Bagian 6.5") merujuk bagian dokumen ini.
"paragraf" berhuruf kecil merujuk paragraf Markdown.

## 3. Prinsip Dasar

### 3.1. Kesetiaan Isi

[P-1] Badan teks WAJIB memuat seluruh unsur yang ditranskripsi (Bagian 5.1) dan hanya unsur tersebut, dengan kata, ejaan, huruf kapital, angka, dan tanda baca yang sama dengan naskah sumber, kecuali normalisasi yang diatur dalam Bagian 7.

[P-2] Salah ketik dalam naskah sumber WAJIB disalin apa adanya.
Transkriptor TIDAK BOLEH membetulkannya dan TIDAK BOLEH menandainya di badan teks (misalnya dengan "[sic]").
Catatan tentang salah ketik BOLEH dimuat dalam isian `catatan` pada entri verifikasi.

[P-3] Kesetiaan yang dimaksud adalah kesetiaan isi, bukan tata letak.
Pemenggalan baris, pemenggalan halaman, perataan, jenis huruf, ukuran huruf, dan indentasi bukan isi.

### 3.2. Tidak Menambah Teks

[P-4] Badan teks TIDAK BOLEH memuat teks yang tidak terdapat dalam naskah sumber, kecuali notasi konvensi yang diatur dalam Bagian 8.
Termasuk dalam larangan ini: judul bagian buatan (misalnya "Pembukaan" atau "Penutup" bila kata tersebut tidak tertulis di naskah), daftar isi, catatan transkriptor, garis pemisah, dan komentar HTML.

[P-5] Markup Markdown hanya memberi struktur pada teks sumber.
Tingkat heading menunjukkan hierarki; jenis unsur ditentukan oleh labelnya, misalnya kata "BAB" atau "Pasal".

### 3.3. Satu Berkas Satu Ekspresi

[P-6] Satu berkas transkripsi WAJIB memuat tepat satu ekspresi dari satu karya, termasuk Penjelasan dan Lampirannya.

### 3.4. Markdown sebagai Sumber Kanonik

[P-7] Berkas Markdown adalah bentuk kanonik.
Bentuk lain (HTML, PDF, XML) BOLEH dihasilkan darinya, tetapi yang diverifikasi dan di-hash adalah berkas Markdown.

## 4. Format Berkas

### 4.1. Pengodean dan Baris

- [F-1] Berkas WAJIB berupa teks UTF-8 tanpa BOM.
- [F-2] Akhir baris WAJIB berupa LF (U+000A).
  CR (U+000D) TIDAK BOLEH ada.
- [F-3] Seluruh teks WAJIB dalam bentuk normalisasi Unicode NFC.
- [F-4] Karakter tab TIDAK BOLEH ada.
- [F-5] Baris TIDAK BOLEH diakhiri spasi.
- [F-6] Berkas WAJIB diakhiri tepat satu karakter LF.
- [F-7] Baris kosong berturut-turut TIDAK BOLEH lebih dari satu.

[F-16] Repositori yang menyimpan berkas transkripsi SEBAIKNYA mencegah pengubahan akhir baris secara otomatis, misalnya dengan entri `*.md -text` dalam berkas `.gitattributes`.

### 4.2. Dialek Markdown

[F-8] Badan teks WAJIB ditafsirkan menurut CommonMark versi 0.31.2 dengan ekstensi tabel GitHub Flavored Markdown (GFM).
Ekstensi lain TIDAK BOLEH diandalkan.

[F-9] Berkas transkripsi hanya BOLEH memakai konstruksi berikut:

| Konstruksi | Pemakaian |
|---|---|
| Heading ATX (`#` sampai `#####`) | Judul dokumen dan unsur struktur (Bagian 6.2) |
| Paragraf | Teks biasa, ayat, label Penjelasan |
| Daftar berpoin `-` | Rincian dengan label asli (Bagian 6.5) |
| Kutipan `>` | Teks yang dikutip dalam peraturan perubahan (Bagian 6.8) |
| Huruf miring `*…*` | Teks yang dicetak miring di sumber (Bagian 7.3) |
| Tabel GFM | Tabel sederhana (Bagian 6.10) |
| HTML `<table>` terbatas | Tabel kompleks (Bagian 6.10) |
| Escape garis miring terbalik | Mencegah salah tafsir (Bagian 4.3) |

[F-10] Konstruksi berikut TIDAK BOLEH dipakai di berkas transkripsi: heading Setext, huruf tebal, tautan, gambar Markdown, blok kode, kode sebaris, garis horizontal, catatan kaki, komentar HTML, dan HTML selain yang diizinkan pada Bagian 6.10.

### 4.3. Escape

[F-11] Teks yang diawali satu sampai sembilan digit yang diikuti titik atau kurung tutup, lalu spasi atau akhir baris (misalnya `1.` atau `1)`), WAJIB di-escape menjadi `1\.` atau `1\)`, termasuk di dalam butir daftar dan kutipan.
Tanpa escape, penampil Markdown menafsirkannya sebagai daftar bernomor dan dapat menomori ulang.

[F-12] Karakter berikut di awal baris teks WAJIB di-escape bila tidak dimaksudkan sebagai markup: `#`, `>`, `-`, `+`, `*`, `=`, `~`.

[F-13] Karakter `\`, `*`, `_`, `` ` ``, `[`, `]`, `<`, `&`, `{`, dan `}` di mana pun dalam teks sumber WAJIB di-escape dengan garis miring terbalik.
Karakter `|` di dalam sel tabel GFM WAJIB di-escape dengan garis miring terbalik.
Kurung kurawal dicadangkan untuk notasi konvensi (Bagian 8).

[F-14] Indentasi TIDAK BOLEH dipakai kecuali untuk penyarangan daftar dan kutipan menurut Bagian 6.5 dan Bagian 6.8.
Indentasi empat spasi atau lebih di luar konteks tersebut dapat ditafsirkan sebagai blok kode.

[F-15] Garis miring terbalik TIDAK BOLEH dipakai sebagai escape selain menurut [F-11], [F-12], dan [F-13], sehingga setiap teks hanya memiliki satu bentuk.

## 5. Cakupan Isi: Unsur yang Ditranskripsi dan Dikecualikan

Kedua daftar dalam bagian ini bersifat tertutup.

[C-5] Unsur yang tidak tercantum dalam salah satu daftar WAJIB dilaporkan dan diputuskan dalam revisi konvensi.
Selama unsur tersebut belum diputuskan, unsur itu SEBAIKNYA ditranskripsi, dan berkas yang memuatnya TIDAK BOLEH berstatus `verified`.

### 5.1. Unsur yang Ditranskripsi

[C-1] Unsur berikut WAJIB ditranskripsi apabila terdapat dalam naskah sumber:

1. Judul: jenis, nomor, tahun, dan nama peraturan.
2. Frasa "DENGAN RAHMAT TUHAN YANG MAHA ESA".
3. Jabatan pembentuk dalam pembukaan, misalnya "PRESIDEN REPUBLIK INDONESIA,".
4. Konsiderans ("Menimbang") beserta seluruh rinciannya.
5. Dasar hukum ("Mengingat") beserta seluruh rinciannya.
6. Frasa persetujuan bersama, apabila ada.
7. Diktum ("MEMUTUSKAN:", "Menetapkan:") beserta nama peraturan yang ditetapkan.
8. Seluruh batang tubuh: label dan judul Buku, BAB, Bagian, Paragraf, serta Pasal, ayat, dan rincian, termasuk tabel, rumus, dan gambar di dalamnya (Bagian 6.10).
9. Penutup: rumusan perintah pengundangan, tempat dan tanggal pengesahan atau penetapan, jabatan, keterangan "ttd" sebagaimana tertulis, dan nama pejabat, atau kalimat pengesahan apabila Undang-Undang sah tanpa tanda tangan Presiden (Pasal 73 UU 12/2011).
10. Tempat dan tanggal pengundangan, jabatan, keterangan "ttd", dan nama pejabat yang mengundangkan.
11. Keterangan penempatan, misalnya "LEMBARAN NEGARA REPUBLIK INDONESIA TAHUN 2022 NOMOR 196".
12. Penjelasan: judul, penjelasan umum, penjelasan pasal demi pasal, dan keterangan tambahan lembaran, misalnya "TAMBAHAN LEMBARAN NEGARA REPUBLIK INDONESIA NOMOR 6820".
13. Lampiran: identitas lampiran, seluruh isi termasuk tabel, rumus, dan gambar (Bagian 6.9 dan Bagian 6.10), serta penutup lampiran beserta jabatan dan nama pejabat.
14. Nomor register peraturan daerah, misalnya "NOREG PERATURAN DAERAH KABUPATEN …".

### 5.2. Unsur yang Dikecualikan

[C-2] Unsur berikut TIDAK BOLEH ditranskripsi:

1. Kop halaman, termasuk lambang negara dan tulisan jabatan yang dicetak di kepala halaman, baik pada halaman pertama maupun halaman berikutnya.
2. Nomor halaman, misalnya "- 2 -".
3. Kode pada kaki halaman, misalnya "SK No 016999 A".
4. Kata sambung di akhir halaman yang mengulang awal halaman berikutnya, misalnya "Pasal 5 . . .".
5. Blok pengesahan salinan, misalnya "Salinan sesuai dengan aslinya" beserta jabatan, nama, dan nomor induk pejabat pengesah salinan.
6. Cap, stempel, tanda tangan grafis, paraf, dan tanda air.
7. Keterangan dan kode tanda tangan elektronik, kode QR, dan kode batang yang ditambahkan pada salinan.
8. Anotasi atau coretan yang bukan bagian dari naskah yang diundangkan.
9. Tulisan "SALINAN" yang menandai berkas sebagai salinan.
10. Teks yang ditambahkan oleh penyedia salinan, misalnya alamat situs, keterangan unduhan, atau tanda penyedia.

[C-3] Informasi yang berguna dari unsur yang dikecualikan, misalnya kode salinan pada kaki halaman, BOLEH dicatat dalam metadata sumber (Bagian 9.3).

### 5.3. Urutan

[C-4] Unsur WAJIB ditranskripsi menurut urutan kemunculannya dalam naskah sumber.

## 6. Struktur Naskah dan Pemetaan Markdown

### 6.1. Prinsip Pemetaan

[S-1] Di dalam batang tubuh dan Penjelasan, setiap jenis unsur struktur WAJIB selalu dipetakan ke tingkat heading yang sama.
Tingkat heading BOLEH melompat, misalnya dari `##` langsung ke `#####` apabila BAB tidak memiliki Bagian.
Konsistensi tingkat lebih diutamakan daripada kelaziman penulisan Markdown.

### 6.2. Tabel Pemetaan Heading

| Unsur | Heading | Contoh |
|---|---|---|
| Judul peraturan | `#` | `# UNDANG-UNDANG REPUBLIK INDONESIA NOMOR 27 TAHUN 2022 TENTANG PELINDUNGAN DATA PRIBADI` |
| Buku | `#` | `# BUKU KESATU — ATURAN UMUM` |
| Judul Penjelasan | `#` | `# PENJELASAN ATAS UNDANG-UNDANG …` |
| Identitas Lampiran | `#` | `# LAMPIRAN UNDANG-UNDANG …` |
| BAB | `##` | `## BAB I — KETENTUAN UMUM` |
| Bagian utama Penjelasan | `##` | `## I. UMUM`, `## II. PASAL DEMI PASAL` |
| Bagian | `###` | `### Bagian Kesatu — Umum` |
| Paragraf | `####` | `#### Paragraf 1 — Persyaratan` |
| Pasal | `#####` | `##### Pasal 5`, `##### Pasal 28A`, `##### Pasal I` |

[S-2] Teks heading WAJIB memuat label dan judul unsur persis seperti sumber, termasuk huruf kapitalnya.
Apabila label dan judul tertulis pada baris terpisah di sumber, keduanya WAJIB digabung dengan notasi pemisah ` — ` (Bagian 8.1).
Apabila judul tertulis dalam beberapa baris, baris-barisnya WAJIB digabung dengan satu spasi.
Ketentuan pemisah ` — ` tidak berlaku untuk judul peraturan, judul Penjelasan, dan identitas Lampiran; baris-baris judul tersebut WAJIB digabung dengan satu spasi.

[S-3] Heading Pasal WAJIB hanya berisi label Pasal.
Pasal tidak memiliki judul dalam naskah Indonesia; teks apa pun selain label TIDAK BOLEH ditambahkan.

[S-4] Heading `######` TIDAK BOLEH dipakai dalam versi ini.

[S-25] Notasi konvensi menurut Bagian 8 BOLEH dipakai di dalam heading, termasuk heading Pasal ([S-3]).

Catatan: Buku dipetakan ke `#` karena Markdown hanya menyediakan enam tingkat heading.
Pembeda antara judul peraturan, Buku, Penjelasan, dan Lampiran adalah labelnya (Prinsip [P-5]).

### 6.3. Pembukaan

[S-5] Pembukaan TIDAK BOLEH diberi heading.
Unsur-unsurnya WAJIB ditulis berurutan setelah judul peraturan, sebagai paragraf atau daftar menurut [S-6] dan [S-7].

[S-6] Kata "Menimbang" dan "Mengingat" WAJIB ditulis sebagai awal paragraf diikuti titik dua tanpa spasi di depannya, misalnya `Menimbang:`.
Apabila konsiderans atau dasar hukum terdiri atas beberapa rincian, kata tersebut berdiri sebagai paragraf sendiri dan rinciannya ditulis sebagai daftar menurut Bagian 6.5.
Apabila hanya terdiri atas satu rumusan tanpa label, rumusannya ditulis langsung setelah titik dua dalam paragraf yang sama.

[S-7] Frasa diktum WAJIB ditulis sebagai paragraf terpisah: `MEMUTUSKAN:` dan `Menetapkan: …`.

### 6.4. Pasal dan Ayat

[S-8] Isi Pasal yang tidak terbagi atas ayat WAJIB ditulis sebagai satu atau beberapa paragraf setelah heading Pasal, beserta rinciannya menurut Bagian 6.5.

[S-9] Setiap ayat WAJIB ditulis sebagai paragraf tersendiri yang diawali labelnya persis seperti sumber, misalnya `(1) …`.

### 6.5. Rincian

[S-10] Setiap rincian WAJIB ditulis sebagai butir daftar berpoin `-` yang diikuti label asli rincian sebagai teks, misalnya `- a. …` atau `- 1\. …`.
Tanda `-` adalah markup; label rincian adalah teks sumber.

[S-11] Rincian dari rincian WAJIB disarangkan dengan indentasi dua spasi per tingkat, sehingga butir anak sejajar dengan awal teks butir induknya.

[S-12] Kalimat yang menyambung setelah daftar rincian, yang di sumber tidak lagi menjorok sebagai bagian rincian terakhir, WAJIB ditulis sebagai paragraf baru setelah daftar.

Contoh (Pasal 2 ayat (1) UU 27/2022):

```markdown
(1) Undang-Undang ini berlaku untuk Setiap Orang, Badan Publik, dan Organisasi Internasional yang melakukan perbuatan hukum sebagaimana diatur dalam Undang-Undang ini:

- a. yang berada di wilayah hukum Negara Republik Indonesia; dan
- b. di luar wilayah hukum Negara Republik Indonesia, yang memiliki akibat hukum:
  - 1\. di wilayah hukum Negara Republik Indonesia; dan/atau
  - 2\. bagi Subjek Data Pribadi warga negara Indonesia di luar wilayah hukum Negara Republik Indonesia.
```

### 6.6. Penutup

[S-13] Penutup TIDAK BOLEH diberi heading.
Setiap blok penutup (misalnya tempat dan tanggal pengesahan, jabatan, keterangan "ttd", nama) WAJIB ditulis sebagai paragraf terpisah.
Baris-baris dalam satu blok WAJIB digabung dengan satu spasi menurut N-3, misalnya `Disahkan di Jakarta pada tanggal 17 Oktober 2022`.

### 6.7. Penjelasan

[S-14] Penjelasan WAJIB diawali heading `#` berisi judul Penjelasan sebagaimana tertulis di sumber.
Bagian utama Penjelasan memakai heading `##`, dan Pasal dalam penjelasan pasal demi pasal memakai heading `#####`.

[S-15] Label dalam penjelasan pasal demi pasal, misalnya "Ayat (1)", "Huruf a", "Angka 3", WAJIB ditulis sebagai paragraf tersendiri, diikuti teks penjelasannya sebagai paragraf berikutnya.

[S-16] Setiap label WAJIB ditulis sebagai entri tersendiri.
Transkriptor TIDAK BOLEH menggabungkan beberapa label menjadi satu entri, misalnya "Huruf a, b, c — Cukup jelas.", kecuali penggabungan itu memang tertulis demikian di sumber.

Contoh (rekaan; tanda `…` menggantikan teks):

```markdown
##### Pasal 10

Ayat (1)

Yang dimaksud dengan "…" adalah …

Ayat (2)

Cukup jelas.
```

### 6.8. Peraturan Perubahan

Peraturan perubahan memuat Pasal berangka Romawi (Pasal I, Pasal II) yang berisi perintah perubahan dan kutipan rumusan baru.

[S-17] Pasal berangka Romawi WAJIB dipetakan ke heading `#####` seperti Pasal lainnya.

[S-18] Rumusan yang dikutip sebagai rumusan baru (misalnya setelah frasa "sehingga berbunyi sebagai berikut:") WAJIB ditulis sebagai kutipan `>`.
Apabila perintah perubahan ditulis sebagai butir rincian, kutipan WAJIB disarangkan di bawah butir tersebut dengan indentasi dua spasi.
Apabila perintah perubahan ditulis sebagai paragraf, kutipan WAJIB ditulis tanpa indentasi setelah paragraf tersebut.

[S-19] Label unsur struktur di dalam kutipan, misalnya "BAB IIA" atau "Pasal 5", TIDAK BOLEH ditulis sebagai heading.
Label tersebut ditulis sebagai paragraf biasa di dalam kutipan.
Ayat dan rincian di dalam kutipan mengikuti Bagian 6.4 dan Bagian 6.5.

[S-24] Dalam penjelasan pasal demi pasal peraturan perubahan, Pasal berangka Romawi WAJIB ditulis sebagai heading `#####`.
Label lain, termasuk label angka perubahan (misalnya "Angka 1") dan label Pasal yang diubah, WAJIB ditulis sebagai paragraf tersendiri menurut [S-15], tidak sebagai heading.

Contoh:

```markdown
##### Pasal I

Beberapa ketentuan dalam Undang-Undang Nomor … diubah sebagai berikut:

- 1\. Ketentuan Pasal 5 diubah sehingga berbunyi sebagai berikut:

  > Pasal 5
  >
  > (1) …
  >
  > (2) … meliputi:
  >
  > - a. …; dan
  > - b. ….
```

### 6.9. Lampiran

[S-20] Setiap Lampiran WAJIB diawali heading `#` berisi baris-baris identitas lampiran yang digabung dengan spasi, misalnya `# LAMPIRAN I PERATURAN PEMERINTAH REPUBLIK INDONESIA NOMOR … TAHUN … TENTANG …`.
Heading di dalam Lampiran mengikuti label yang tertulis, dengan tingkat `##` sampai `####` menurut hierarkinya.
Tabel, rumus, dan gambar di dalam Lampiran mengikuti Bagian 6.10.

### 6.10. Tabel, Rumus, dan Gambar

Ketentuan dalam subbagian ini berlaku di seluruh badan teks: batang tubuh, Penjelasan, dan Lampiran.

[S-21] Tabel tanpa sel gabungan WAJIB ditulis sebagai tabel GFM.

[S-22] Tabel dengan sel gabungan BOLEH ditulis sebagai HTML terbatas.
Elemen yang diizinkan hanya `table`, `thead`, `tbody`, `tr`, `th`, `td`, dan `br`, dengan atribut `rowspan` dan `colspan` saja.

[S-23] Rumus SEBAIKNYA ditulis secara linear dengan karakter Unicode.
Gambar, diagram, formulir, peta, dan rumus yang tidak dapat ditulis secara linear WAJIB disimpan sebagai berkas pendamping dan dirujuk dengan notasi `{berkas:…}` (Bagian 8.3).

[S-26] Tabel yang terletak di dalam rincian WAJIB disarangkan dengan indentasi butir rinciannya.

## 7. Normalisasi Teks

[N-1] Hanya normalisasi dalam bagian ini yang BOLEH dilakukan terhadap teks sumber.

- [N-2] Pemenggalan kata di akhir baris karena tata letak WAJIB disambung kembali.
  Tanda hubung yang merupakan bagian kata, misalnya "perundang-undangan", WAJIB dipertahankan.
- [N-3] Pergantian baris di dalam satu kalimat atau paragraf WAJIB diganti satu spasi.
- [N-4] Spasi berganda WAJIB diganti satu spasi.
- [N-5] Spasi sebelum titik dua, titik koma, koma, dan titik WAJIB dihapus.
- [N-6] Tanda petik lengkung (“ ” ‘ ’) WAJIB diganti tanda petik lurus (" ').
- [N-7] Ligatur tipografis (misalnya ﬁ, ﬂ) WAJIB diurai menjadi huruf biasa.
- [N-8] Spasi tak terputus (U+00A0) WAJIB diganti spasi biasa.
  Tanda hubung lunak (U+00AD) dan karakter lebar nol (U+200B, U+200C, U+200D, U+2060, U+FEFF) WAJIB dihapus.
- [N-9] Tanda pisah panjang dan pendek (— –) WAJIB dipertahankan sebagaimana di sumber.

### 7.1. Huruf Kapital dan Angka

[N-10] Huruf kapital, angka, pemisah ribuan, pemisah desimal, dan penulisan mata uang WAJIB dipertahankan persis, misalnya "Rp5.000.000.000,00".

### 7.2. Huruf Tebal dan Garis Bawah

[N-11] Cetak tebal dan garis bawah di sumber TIDAK BOLEH ditranskripsi sebagai markup.

### 7.3. Huruf Miring

[N-12] Teks yang dicetak miring di sumber, misalnya istilah asing atau istilah daerah, WAJIB ditandai `*…*`.
Cetak miring dipertahankan karena dalam teknik penyusunan peraturan cetak miring menandai istilah asing.

## 8. Notasi Konvensi

Notasi konvensi adalah satu-satunya teks dalam badan teks yang bukan berasal dari naskah sumber.
Kurung kurawal dicadangkan khusus untuk notasi konvensi.

### 8.1. Pemisah Label dan Judul

[K-1] Notasi ` — ` (spasi, tanda pisah panjang U+2014, spasi) WAJIB dipakai dalam heading untuk memisahkan label unsur dan judulnya menurut [S-2], misalnya `## BAB II — ASAS`.
Notasi ini bukan teks sumber.

### 8.2. Penanda Keraguan

[K-2] Teks yang belum dapat dipastikan sesuai naskah sumber WAJIB diapit penanda `{?` dan `?}`, misalnya `{?pelindungan?}`.
Contoh keadaan yang memerlukannya: kata yang tidak terbaca pada pindaian, kata yang dipulihkan dari konteks, atau label yang direkonstruksi.

[K-3] Penanda keraguan pada sebuah label berlaku untuk seluruh entri yang dimulai oleh label tersebut.

[K-4] Penanda keraguan TIDAK BOLEH bersarang dan TIDAK BOLEH melintasi batas paragraf.

[K-5] Berkas yang masih memuat penanda keraguan TIDAK BOLEH berstatus `verified`.
Verifikator WAJIB menghapus penanda apabila teksnya benar, atau mengganti teksnya apabila salah.

### 8.3. Rujukan Berkas Pendamping

[K-6] Notasi `{berkas:nama-berkas}` pada satu baris tersendiri menandai letak gambar, diagram, formulir, atau rumus yang disimpan sebagai berkas pendamping.
Nama berkas WAJIB tercantum dalam isian `berkas_pendamping` pada frontmatter beserta nilai hashnya.

[K-7] Teks yang tertulis di dalam gambar, misalnya judul tabel atau keterangan gambar, SEBAIKNYA tetap ditranskripsi sebagai teks di dekat notasi tersebut apabila teks itu terpisah dari gambarnya di sumber.

### 8.4. Notasi Lain

[K-8] Notasi selain yang diatur dalam Bagian 8 TIDAK BOLEH dipakai.

## 9. Metadata (Frontmatter)

### 9.1. Ketentuan Umum

[M-1] Berkas transkripsi WAJIB diawali frontmatter YAML 1.2 yang dibuka dan ditutup oleh baris `---`.

[M-2] Frontmatter hanya BOLEH memuat informasi yang tidak berubah sepanjang umur berkas yang telah diverifikasi.
Informasi yang dapat berubah, terutama status keberlakuan peraturan dan relasi masuk ("diubah oleh", "dicabut oleh"), WAJIB disimpan di register, bukan di frontmatter.

[M-3] Nama isian WAJIB menggunakan huruf kecil dan garis bawah (*snake_case*) dalam bahasa Indonesia.

[M-4] Tanggal WAJIB ditulis dalam format ISO 8601 `YYYY-MM-DD`.
Nomor peraturan WAJIB ditulis sebagai string.

[M-5] Baris yang hanya berisi `---` TIDAK BOLEH muncul di dalam frontmatter.

### 9.2. Kelompok Isian

Frontmatter disusun menurut tingkat identitas FRBR:

| Kelompok | Isi |
|---|---|
| `konvensi` | Versi konvensi yang dipakai |
| `karya` | Identitas peraturan sebagai karya hukum |
| `ekspresi` | Identitas teks yang ditranskripsi |
| `sumber` | Daftar naskah sumber yang menjadi acuan |
| `transkripsi` | Identitas manifestasi: proses dan versi berkas ini |
| `berkas_pendamping` | Berkas gambar dan sejenisnya beserta hashnya |
| `verifikasi` | Entri verifikasi |

### 9.3. Daftar Isian

[M-6] Frontmatter WAJIB memuat setiap isian yang bertanda WAJIB pada tabel di bawah, dan setiap isian bertanda "WAJIB bila ada" apabila informasinya terdapat dalam naskah sumber.
Isian yang tidak tercantum pada tabel TIDAK BOLEH dipakai.
Nilai setiap isian WAJIB sesuai dengan kolom Tipe, dengan arti sebagai berikut:

- string: skalar YAML yang dibaca sebagai string; nilai yang dapat terbaca sebagai bilangan, tanggal, atau nilai logika WAJIB diberi tanda kutip, misalnya `nomor: "27"`;
- bilangan: bilangan bulat YAML tanpa tanda kutip;
- tanggal: tanggal berformat `YYYY-MM-DD` menurut [M-4], ditulis tanpa tanda kutip;
- objek: pemetaan YAML yang memuat isian sebagaimana disebut di kolom Keterangan;
- daftar: urutan YAML yang butirnya sebagaimana disebut di kolom Keterangan.

Nama isian berbentuk `a[].b` berarti isian `b` pada setiap butir daftar `a`.

| Isian | Wajib | Tipe | Keterangan |
|---|---|---|---|
| `konvensi` | WAJIB | string | Rujukan versi konvensi, misalnya `transkripsi-peraturan/0.1` |
| `karya.id` | WAJIB | string | Pengenal karya (Bagian 10.2) |
| `karya.jenis` | WAJIB | string | Jenis peraturan, misalnya `Undang-Undang` |
| `karya.singkatan_jenis` | WAJIB | string | Misalnya `UU`, `PP`, `Perpres` |
| `karya.nomor` | WAJIB | string | Nomor sebagaimana tertulis |
| `karya.tahun` | WAJIB | bilangan | Tahun dalam penomoran peraturan |
| `karya.judul` | WAJIB | string | Nama peraturan setelah kata "tentang" |
| `karya.judul_lengkap` | WAJIB | string | Jenis, nomor, tahun, dan nama peraturan |
| `karya.singkatan` | BOLEH | string | Nama populer, misalnya `UU PDP` |
| `karya.pembentuk` | WAJIB | string | Lembaga atau jabatan pembentuk |
| `karya.pemrakarsa` | BOLEH | string | Instansi pemrakarsa |
| `karya.teu_badan` | BOLEH | string | Tajuk Entri Utama badan menurut pedoman JDIHN |
| `karya.tempat_penetapan` | WAJIB | string | Tempat pengesahan atau penetapan |
| `karya.tanggal_penetapan` | WAJIB | tanggal | Tanggal pengesahan atau penetapan |
| `karya.penandatangan` | WAJIB bila ada | objek | `jabatan` dan `nama` pejabat yang mengesahkan atau menetapkan; tidak ada bila Undang-Undang sah tanpa tanda tangan Presiden |
| `karya.tanggal_pengundangan` | WAJIB bila ada | tanggal | Tanggal pengundangan |
| `karya.pengundang` | WAJIB bila ada | objek | `jabatan` dan `nama` pejabat yang mengundangkan |
| `karya.penempatan` | WAJIB bila ada | objek | `media` (misalnya `Lembaran Negara Republik Indonesia`), `tahun`, `nomor` |
| `karya.tambahan_penempatan` | WAJIB bila ada | objek | `media` dan `nomor`, misalnya Tambahan Lembaran Negara |
| `karya.mulai_berlaku` | BOLEH | string | Ketentuan saat mulai berlaku, berupa tanggal atau rumusan |
| `karya.mengubah` | BOLEH | daftar | Pengenal karya yang diubah oleh peraturan ini |
| `karya.mencabut` | BOLEH | daftar | Pengenal karya yang dicabut oleh peraturan ini |
| `karya.bidang_hukum` | BOLEH | string | Menurut klasifikasi JDIHN |
| `karya.subjek` | BOLEH | daftar | Kata kunci subjek |
| `ekspresi.id` | WAJIB | string | Pengenal ekspresi (Bagian 10.3) |
| `ekspresi.jenis_teks` | WAJIB | string | `asli` (versi 0.1 hanya mengenal nilai ini) |
| `ekspresi.bahasa` | WAJIB | string | Kode ISO 639-3, misalnya `ind` |
| `ekspresi.tanggal` | WAJIB | tanggal | Untuk teks asli: tanggal pengundangan, atau tanggal penetapan bila tidak diundangkan |
| `ekspresi.komponen` | WAJIB | daftar | Komponen naskah yang dimuat: `batang-tubuh`, `penjelasan`, `lampiran` |
| `sumber` | WAJIB | daftar | Satu butir untuk setiap berkas naskah sumber, dengan isian `sumber[].…` di bawah |
| `sumber[].jenis` | WAJIB | string | Misalnya `Salinan resmi Kementerian Sekretariat Negara` |
| `sumber[].diperoleh_dari` | WAJIB | string | Nama situs atau instansi penyedia |
| `sumber[].url` | WAJIB | string | URL berkas sumber |
| `sumber[].berkas` | WAJIB | string | Nama berkas sumber |
| `sumber[].sha256` | WAJIB | string | Hash SHA-256 berkas sumber, heksadesimal huruf kecil |
| `sumber[].diakses` | WAJIB | tanggal | Tanggal berkas sumber diunduh |
| `sumber[].kode_salinan` | BOLEH | string | Kode yang tercetak pada salinan |
| `sumber[].komponen` | WAJIB | daftar | Komponen naskah yang bersumber dari berkas ini: `batang-tubuh`, `penjelasan`, `lampiran` |
| `transkripsi.versi` | WAJIB | string | Versi berkas transkripsi menurut Bagian 11.6 |
| `transkripsi.metode` | WAJIB | string | Misalnya `ketik ganda`, `OCR dengan koreksi manual` |
| `transkripsi.transkriptor` | WAJIB | daftar | Nama orang atau proses |
| `transkripsi.tanggal` | WAJIB | tanggal | Tanggal transkripsi selesai |
| `berkas_pendamping` | WAJIB | daftar | Setiap butir berisi `berkas` dan `sha256`; daftar kosong bila tidak ada |
| `verifikasi` | WAJIB | daftar | Entri menurut Bagian 9.4; daftar kosong sebelum verifikasi |

[M-8] Gabungan nilai `komponen` pada seluruh butir `sumber` WAJIB sama dengan nilai `ekspresi.komponen`.

### 9.4. Entri Verifikasi

[M-7] Setiap entri dalam `verifikasi` WAJIB memuat isian yang bertanda WAJIB pada tabel berikut dan TIDAK BOLEH memuat isian yang tidak tercantum di dalamnya:

| Isian | Wajib | Keterangan |
|---|---|---|
| `nama` | WAJIB | Nama verifikator |
| `afiliasi` | WAJIB | Lembaga atau asosiasi |
| `peran` | WAJIB | Misalnya `ahli hukum`, `pemeriksa naskah` |
| `tanggal` | WAJIB | Tanggal verifikasi selesai |
| `cakupan` | WAJIB | `seluruh` atau daftar komponen naskah yang diperiksa |
| `hash_badan` | WAJIB | Hash SHA-256 badan teks yang diperiksa (Bagian 11.3) |
| `catatan` | BOLEH | Catatan, misalnya salah ketik pada sumber |
| `tanda_tangan` | BOLEH | Rujukan berkas tanda tangan digital, apabila sudah diterapkan |

### 9.5. Contoh Frontmatter

```yaml
---
konvensi: transkripsi-peraturan/0.1
karya:
  id: uu/2022/27
  jenis: Undang-Undang
  singkatan_jenis: UU
  nomor: "27"
  tahun: 2022
  judul: Pelindungan Data Pribadi
  judul_lengkap: Undang-Undang Republik Indonesia Nomor 27 Tahun 2022 tentang Pelindungan Data Pribadi
  singkatan: UU PDP
  pembentuk: Presiden Republik Indonesia dengan persetujuan bersama Dewan Perwakilan Rakyat Republik Indonesia
  tempat_penetapan: Jakarta
  tanggal_penetapan: 2022-10-17
  penandatangan:
    jabatan: Presiden Republik Indonesia
    nama: Joko Widodo
  tanggal_pengundangan: 2022-10-17
  pengundang:
    jabatan: Menteri Sekretaris Negara Republik Indonesia
    nama: Pratikno
  penempatan:
    media: Lembaran Negara Republik Indonesia
    tahun: 2022
    nomor: "196"
  tambahan_penempatan:
    media: Tambahan Lembaran Negara Republik Indonesia
    nomor: "6820"
  mulai_berlaku: pada tanggal diundangkan
ekspresi:
  id: uu/2022/27/ind@2022-10-17
  jenis_teks: asli
  bahasa: ind
  tanggal: 2022-10-17
  komponen: [batang-tubuh, penjelasan]
sumber:
  - jenis: Salinan resmi Kementerian Sekretariat Negara
    diperoleh_dari: JDIH Kementerian Keuangan
    url: "https://…"
    berkas: "…pdf"
    sha256: "…"
    diakses: 2026-10-21
    kode_salinan: "SK No 016999 A s.d. 155338 A"
    komponen: [batang-tubuh, penjelasan]
transkripsi:
  versi: 1.0.0
  metode: OCR dengan koreksi manual
  transkriptor: ["…"]
  tanggal: 2026-10-21
berkas_pendamping: []
verifikasi:
  - nama: "…"
    afiliasi: "…"
    peran: ahli hukum
    tanggal: 2026-11-10
    cakupan: seluruh
    hash_badan: "…"
---
```

### 9.6. Pemetaan ke Isian Portal JDIHN

Tabel berikut memetakan isian frontmatter dan register ke nama isian dalam format integrasi Portal JDIHN.
Pemetaan ini informatif; penyelarasan akhir dengan unsur metadata dalam lampiran Permenkumham 8/2019 dilakukan pada revisi konvensi berikutnya.

| Isian konvensi | Isian JDIHN | Catatan |
|---|---|---|
| `karya.jenis` | `jenis` | |
| `karya.singkatan_jenis` | `singkatanJenis` | |
| `karya.nomor` | `noPeraturan` | |
| `karya.judul_lengkap` | `judul` | |
| `karya.tanggal_penetapan` | `tanggal_penetapan` | |
| `karya.tanggal_pengundangan` | `tanggal_pengundangan` | Tahunnya menjadi `tahun_pengundangan` |
| `karya.tempat_penetapan` | `tempatTerbit` | |
| `karya.penempatan`, `karya.tambahan_penempatan` | `sumber` | Digabung menurut pedoman penulisan sumber JDIHN |
| `karya.teu_badan` | `teuBadan` | |
| `karya.bidang_hukum` | `bidangHukum` | |
| `karya.subjek` | `subjek` | |
| `ekspresi.bahasa` | `bahasa` | Kode `ind` dikonversi menjadi nama bahasa |
| Register: status keberlakuan | `status` | Tidak disimpan di frontmatter ([M-2]) |
| — | `noPanggil`, `isbn`, `nomorIndukBuku`, `penerbit`, `deskripsiFisik` | Untuk monografi; tidak dipakai |

## 10. Skema Pengenal

### 10.1. Prinsip

Skema pengenal diilhami templat URI ELI dan model FRBR.
Pengenal bersifat menjelaskan dirinya sendiri, stabil, dan tidak bergantung pada lokasi penyimpanan.
[I-10] Apabila diterbitkan di web, pengenal BOLEH diawali URI dasar, misalnya `https://contoh.id/eli/`.

### 10.2. Pengenal Karya

[I-1] Pengenal karya WAJIB berbentuk:

```text
{jenis}/{tahun}/{nomor}
{jenis}/{pembentuk}/{tahun}/{nomor}
```

Bentuk kedua WAJIB dipakai untuk jenis yang dapat dibentuk oleh lebih dari satu lembaga atau daerah.

| Kode `jenis` | Jenis peraturan | Segmen `pembentuk` |
|---|---|---|
| `uud` | Undang-Undang Dasar | Tidak ada; pengenal `uud/1945` |
| `tap-mpr` | Ketetapan MPR | Tidak ada |
| `uu` | Undang-Undang | Tidak ada |
| `perppu` | Peraturan Pemerintah Pengganti Undang-Undang | Tidak ada |
| `pp` | Peraturan Pemerintah | Tidak ada |
| `perpres` | Peraturan Presiden | Tidak ada |
| `permen` | Peraturan Menteri | Kode kementerian |
| `perlem` | Peraturan lembaga negara, badan, lembaga, atau komisi menurut Pasal 8 ayat (1) UU 12/2011, misalnya MPR, DPR, DPD, Mahkamah Agung, Mahkamah Konstitusi, Badan Pemeriksa Keuangan, Komisi Yudisial, dan Bank Indonesia | Kode lembaga |
| `perda-prov` | Peraturan Daerah Provinsi | Kode wilayah |
| `perda-kabkota` | Peraturan Daerah Kabupaten/Kota | Kode wilayah |
| `perdprd-prov` | Peraturan DPRD Provinsi | Kode wilayah |
| `perdprd-kabkota` | Peraturan DPRD Kabupaten/Kota | Kode wilayah |
| `pergub` | Peraturan Gubernur | Kode wilayah |
| `perbup` | Peraturan Bupati | Kode wilayah |
| `perwali` | Peraturan Wali Kota | Kode wilayah |
| `perdes` | Peraturan Desa | Kode wilayah |
| `perkades` | Peraturan Kepala Desa | Kode wilayah |

[I-2] Kode kementerian dan kode lembaga WAJIB diambil dari daftar kode yang dikelola bersama register.
Kode wilayah WAJIB memakai kode wilayah administrasi pemerintahan yang ditetapkan Kementerian Dalam Negeri, dengan titik diganti tanda hubung.
Kode pembentuk WAJIB mengikuti nomenklatur pembentuk pada tanggal penetapan peraturan dan TIDAK BOLEH diubah karena perubahan nomenklatur di kemudian hari.

[I-3] Segmen `nomor` WAJIB dinormalisasi: huruf kecil, dan setiap rangkaian karakter selain `a`–`z` dan `0`–`9` diganti satu tanda hubung, tanpa tanda hubung di awal atau akhir.
Contoh: nomor "12/PMK.03/2020" menjadi `12-pmk-03-2020`.

Contoh pengenal karya:

```text
uu/2022/27
pp/2021/35
permen/kemenkeu/2023/12
perda-prov/32/2020/5
```

### 10.3. Pengenal Ekspresi

[I-4] Pengenal ekspresi WAJIB berbentuk `{pengenal karya}/{bahasa}@{tanggal}`, dengan `bahasa` berupa kode ISO 639-3 dan `tanggal` sama dengan `ekspresi.tanggal`.

Contoh: `uu/2022/27/ind@2022-10-17`.

### 10.4. Identitas Manifestasi

Manifestasi adalah berkas transkripsi itu sendiri.
Identitasnya adalah pasangan pengenal ekspresi dan `transkripsi.versi`, sedangkan sidik jarinya adalah nilai hash berkas di register.

### 10.5. Nama Berkas

[I-5] Nama berkas transkripsi teks asli WAJIB berupa pengenal karya dengan `/` diganti `-`, diikuti `.md`.
Contoh: `uu-2022-27.md`, `permen-kemenkeu-2023-12.md`.

[I-6] Pola `{nama berkas teks asli tanpa .md}@{YYYY-MM-DD}.md` dicadangkan untuk teks konsolidasi dan TIDAK BOLEH dipakai dalam versi ini.

[I-7] Berkas pendamping WAJIB dinamai dengan awalan nama berkas transkripsinya, misalnya `uu-2022-27.lampiran-1.gambar-1.png`.

### 10.6. Rujukan Fragmen

[I-8] Rujukan ke bagian dari suatu peraturan WAJIB berbentuk pengenal karya atau ekspresi diikuti `#` dan fragmen.
Fragmen dihitung dari struktur badan teks dan TIDAK BOLEH ditulis sebagai jangkar di dalam berkas.

| Unsur | Pola fragmen | Contoh |
|---|---|---|
| Buku | `buku-{urutan}` | `#buku-2` |
| BAB | `bab-{romawi}` | `#bab-ii` |
| Bagian | `bab-{romawi}-bagian-{urutan}` | `#bab-ii-bagian-1` |
| Paragraf | `bab-{romawi}-bagian-{urutan}-paragraf-{nomor}` | `#bab-ii-bagian-1-paragraf-2` |
| Pasal | `pasal-{nomor}` | `#pasal-28a` |
| Ayat | `pasal-{nomor}-ayat-{nomor}` | `#pasal-5-ayat-2` |
| Rincian | `…-huruf-{huruf}`, `…-angka-{angka}` | `#pasal-2-ayat-1-huruf-b-angka-1` |
| Konsiderans | `menimbang-huruf-{huruf}` | `#menimbang-huruf-a` |
| Dasar hukum | `mengingat-angka-{angka}` | `#mengingat-angka-1` |
| Penjelasan umum | `penjelasan-umum` | `#penjelasan-umum` |
| Penjelasan Pasal | `penjelasan-pasal-{nomor}…` | `#penjelasan-pasal-4-ayat-2-huruf-b` |
| Lampiran | `lampiran-{romawi atau angka}` | `#lampiran-i` |

[I-9] Seluruh fragmen WAJIB berhuruf kecil, termasuk angka Romawi.
Nomor Pasal bersifat unik dalam satu peraturan, sehingga rujukan Pasal tidak memerlukan BAB.
Rincian bertingkat `a)` dan `1)` dirujuk dengan kata yang sama (`huruf`, `angka`) secara berurutan menurut tingkatnya.
Segmen `urutan` adalah bilangan dari kata bilangan bertingkat, misalnya "Buku Kedua" menjadi `buku-2` dan "Bagian Kesatu" menjadi `bagian-1`.
Apabila peraturan memiliki Buku, fragmen BAB, Bagian, dan Paragraf WAJIB diawali fragmen Bukunya, misalnya `#buku-2-bab-i`, karena penomoran BAB dapat dimulai ulang pada setiap Buku.

Contoh rujukan lengkap: `uu/2022/27/ind@2022-10-17#pasal-46-ayat-1-huruf-a`.

## 11. Daur Hidup, Verifikasi, dan Hash

### 11.1. Status

Status berkas transkripsi dicatat di register, bukan di berkas.

[V-9] Status berkas transkripsi di register WAJIB berupa salah satu nilai pada tabel berikut.

| Status | Arti |
|---|---|
| `new transcription` | Transkripsi selesai dibuat dan lolos pemeriksaan otomatis menurut [V-10], belum diserahkan ke verifikator |
| `verification in progress` | Sedang diperiksa verifikator |
| `revision required` | Verifikator menemukan ketidaksesuaian; berkas dikembalikan ke transkriptor |
| `verified` | Seluruh verifikator yang disyaratkan menyatakan sesuai; nilai hash dicatat |
| `superseded` | Digantikan oleh versi transkripsi yang lebih baru |

### 11.2. Alur

1. Transkriptor membuat berkas dan menjalankan pemeriksaan otomatis (Bagian 12).
2. Berkas diserahkan ke verifikator dan statusnya menjadi `verification in progress`.
3. Verifikator membandingkan badan teks dengan setiap naskah sumber yang hashnya tercantum di `sumber`, lalu menyelesaikan seluruh penanda keraguan.
4. Apabila ditemukan ketidaksesuaian, status menjadi `revision required` dan alur kembali ke langkah 1.
5. Setelah badan teks dibekukan, setiap verifikator menambahkan entri verifikasi yang memuat `hash_badan`.
6. Berkas final di-hash dan nilai hashnya dicatat di register dengan status `verified`.

[V-1] Badan teks TIDAK BOLEH diubah setelah entri verifikasi pertama ditambahkan.
Perubahan badan teks membatalkan seluruh entri verifikasi dan mengembalikan berkas ke langkah 1.

[V-2] Metode transkripsi SEBAIKNYA berupa ketik ganda: dua transkripsi independen dibandingkan secara otomatis sebelum diserahkan ke verifikator.

### 11.3. Hash Badan Teks

[V-3] `hash_badan` WAJIB dihitung dengan SHA-256 atas seluruh byte berkas yang terletak setelah karakter LF yang mengakhiri baris `---` penutup frontmatter, dan ditulis dalam heksadesimal huruf kecil.

Karena hanya mencakup badan teks, nilai ini tidak berubah ketika entri verifikasi ditambahkan ke frontmatter.
Dengan demikian setiap verifikator dapat menyatakan secara tepat teks mana yang ia periksa.

Contoh perhitungan:

```sh
python3 -c "import sys,hashlib; b=open(sys.argv[1],'rb').read(); i=b.index(b'\n---\n',3)+5; print(hashlib.sha256(b[i:]).hexdigest())" uu-2022-27.md
```

### 11.4. Hash Berkas

[V-4] Nilai hash di register WAJIB dihitung dengan SHA-256 atas seluruh byte berkas, setelah seluruh entri verifikasi ditambahkan.

```sh
sha256sum uu-2022-27.md
```

[V-5] Berkas berstatus `verified` TIDAK BOLEH diubah.
Perbaikan apa pun WAJIB diterbitkan sebagai versi transkripsi baru, dan versi lama berstatus `superseded`.

### 11.5. Register

[V-6] Register WAJIB memuat sekurang-kurangnya isian berikut untuk setiap berkas:

| Isian | Keterangan |
|---|---|
| Pengenal ekspresi | Misalnya `uu/2022/27/ind@2022-10-17` |
| Nama berkas | Misalnya `uu-2022-27.md` |
| Versi transkripsi | Misalnya `1.0.0` |
| Versi konvensi | Misalnya `transkripsi-peraturan/0.1` |
| Status | Menurut Bagian 11.1 |
| Tanggal status | Tanggal status terakhir berubah |
| Sumber | URL dan hash SHA-256 setiap naskah sumber |
| SHA-256 berkas | Diisi hanya untuk status `verified` dan `superseded` |
| Digantikan oleh | Versi pengganti, untuk status `superseded` |
| Status keberlakuan peraturan | Misalnya berlaku, diubah, dicabut |
| Diubah oleh, dicabut oleh | Pengenal karya peraturan lain |

[V-8] Register SEBAIKNYA disimpan sebagai berkas data terstruktur (misalnya CSV atau YAML) dalam repositori berversi, dan BOLEH ditampilkan sebagai tabel Markdown.

[V-12] Setiap naskah sumber yang tercantum di `sumber` WAJIB diarsipkan oleh pengelola register sedemikian rupa sehingga dapat diambil kembali dan dicocokkan dengan nilai `sha256`-nya selama berkas transkripsi berstatus `verified` atau `superseded`.

### 11.6. Versi Berkas Transkripsi

[V-7] `transkripsi.versi` WAJIB mengikuti pola `MAYOR.MINOR.PATCH`:

- `0.x.y` untuk berkas yang belum pernah berstatus `verified`; MINOR dinaikkan untuk setiap perubahan badan teks dan PATCH untuk perubahan frontmatter saja;
- `1.0.0` ditetapkan setelah entri verifikasi terakhir ditambahkan dan sebelum hash berkas dihitung ([V-4]);
- naik MAYOR untuk perubahan badan teks setelah `verified`;
- naik MINOR untuk perubahan frontmatter yang tidak mengubah badan teks setelah `verified`.

[V-13] Setiap versi berkas transkripsi yang pernah berstatus `verified` WAJIB tetap dapat diambil kembali dengan isi byte yang sama, misalnya melalui riwayat repositori berversi, selama hashnya tercatat di register.

## 12. Pemeriksaan Otomatis

Pemeriksaan berikut dijalankan dengan alat pemeriksa (*linter*).
Setiap pemeriksaan memiliki tingkat `galat` atau `peringatan`.
Pemeriksaan bertanda "(verified)" hanya berlaku sejak berkas akan berstatus `verified`.

[V-10] Berkas transkripsi WAJIB lolos seluruh pemeriksaan bertingkat `galat` yang tidak bertanda "(verified)" sebelum berstatus `new transcription`, dan WAJIB lolos seluruh pemeriksaan bertingkat `galat` sebelum berstatus `verified`.

[V-11] Setiap temuan pemeriksaan bertingkat `peringatan` WAJIB diperiksa verifikator terhadap naskah sumber.
Apabila teks yang menimbulkan temuan sesuai dengan naskah sumber, verifikator WAJIB mencatatnya dalam isian `catatan` pada entri verifikasi.

| Kode | Pemeriksaan | Tingkat | Ketentuan |
|---|---|---|---|
| L-01 | UTF-8 valid tanpa BOM | galat | F-1 |
| L-02 | Tidak ada CR | galat | F-2 |
| L-03 | Teks dalam bentuk NFC | galat | F-3 |
| L-04 | Tidak ada tab, spasi di akhir baris, atau baris kosong berganda; diakhiri satu LF | galat | F-4 s.d. F-7 |
| L-05 | Frontmatter YAML valid dan memuat seluruh isian WAJIB dengan tipe yang benar | galat | M-1 s.d. M-7 |
| L-06 | Versi konvensi tercantum dalam daftar rilis konvensi (verified) | galat | R-1, R-6 |
| L-07 | Hanya konstruksi Markdown yang diizinkan | galat | F-9, F-10 |
| L-08 | Penanda daftar bernomor di awal teks di-escape, dan tidak ada escape selain yang diwajibkan | galat | F-11 s.d. F-13, F-15 |
| L-09 | Tidak ada blok kode akibat indentasi | galat | F-14 |
| L-10 | Setiap heading sesuai tabel pemetaan; heading `#####` hanya berisi label Pasal | galat | S-1 s.d. S-4, S-24, S-25 |
| L-11 | Nomor Pasal berurutan, dengan Pasal sisipan (misalnya 28A) diperbolehkan | peringatan | P-1 |
| L-12 | Daftar Pasal dalam penjelasan pasal demi pasal sama dengan daftar Pasal batang tubuh | peringatan | P-1, S-14 |
| L-13 | Kurung kurawal hanya muncul sebagai notasi konvensi yang sah | galat | F-13, K-8 |
| L-14 | Setiap `{berkas:…}` tercantum di `berkas_pendamping` dan hashnya cocok | galat | K-6 |
| L-15 | Nama berkas sesuai pengenal karya | galat | I-5 |
| L-16 | Tidak ada penanda keraguan (verified) | galat | K-5 |
| L-17 | Setiap `sumber[].sha256` cocok dengan naskah sumber yang diarsipkan (verified) | galat | M-6, V-12, Bagian 11.2 |
| L-18 | Setiap `hash_badan` sama dengan hash badan teks hasil perhitungan (verified) | galat | V-3 |
| L-19 | `ekspresi.id` sesuai dengan `karya.id`, `ekspresi.bahasa`, dan `ekspresi.tanggal` | galat | I-4 |
| L-20 | Penanda keraguan tidak bersarang dan tidak melintasi batas paragraf | galat | K-4 |
| L-21 | Nama setiap berkas pendamping diawali nama berkas transkripsinya | galat | I-7 |

## 13. Pengelolaan Versi Konvensi

[R-1] Konvensi diberi versi `MAYOR.MINOR.PATCH`.
Berkas transkripsi merujuknya dengan `transkripsi-peraturan/MAYOR.MINOR`.

[R-2] PATCH dipakai untuk perbaikan redaksional yang tidak mengubah ketentuan.
MINOR dipakai untuk penambahan yang tidak membuat berkas yang sesuai versi sebelumnya menjadi tidak sesuai.
MAYOR dipakai untuk perubahan yang dapat membuat berkas yang sesuai versi sebelumnya menjadi tidak sesuai.
Selama versi MAYOR bernilai 0, perubahan MINOR BOLEH tidak kompatibel.

[R-3] Versi konvensi yang telah final TIDAK BOLEH diubah.
Nilai hash setiap versi final WAJIB dicatat dalam daftar rilis konvensi yang dikelola bersama dokumen konvensi.

[R-4] Berkas transkripsi yang telah `verified` tetap sah menurut versi konvensi yang dirujuknya, meskipun versi konvensi yang lebih baru telah terbit.

[R-5] "Konvensi Artup" adalah nama dokumen ini, sedangkan `transkripsi-peraturan` adalah pengenal teknisnya.
Berkas transkripsi WAJIB merujuk pengenal teknis, sehingga perubahan nama di kemudian hari tidak mengharuskan perubahan berkas yang telah di-hash.

[R-6] Berkas transkripsi BOLEH merujuk versi konvensi yang masih draf selama penyusunan.
Berkas transkripsi TIDAK BOLEH berstatus `verified` sebelum versi konvensi yang dirujuknya final dan tercantum dalam daftar rilis konvensi.

[R-7] Frontmatter dokumen konvensi WAJIB memuat isian `id`, `nama`, `judul`, `versi`, `status`, dan `tanggal`, dan BOLEH memuat `bahasa`, `penyusun`, dan `menggantikan`.
Nilai `id` WAJIB sama dengan pengenal teknis menurut [R-5].
Nilai `status` WAJIB berupa `draf` atau `final`.

[R-8] Dokumen konvensi TIDAK BOLEH memuat informasi tentang versi yang menggantikannya.
Hubungan antarversi konvensi ditentukan dari daftar rilis konvensi menurut [R-3].

## 14. Lampiran A: Contoh Berkas Minimal

Contoh berikut dipersingkat; tanda `…` menggantikan teks yang dihilangkan dan bukan bagian dari berkas yang sebenarnya.

```markdown
---
konvensi: transkripsi-peraturan/0.1
karya:
  id: uu/2022/27
  …
---

# UNDANG-UNDANG REPUBLIK INDONESIA NOMOR 27 TAHUN 2022 TENTANG PELINDUNGAN DATA PRIBADI

DENGAN RAHMAT TUHAN YANG MAHA ESA

PRESIDEN REPUBLIK INDONESIA,

Menimbang:

- a. bahwa pelindungan data pribadi merupakan …;
- b. bahwa …;

Mengingat: Pasal 5 ayat (1), Pasal 20, … Undang-Undang Dasar Negara Republik Indonesia Tahun 1945;

Dengan Persetujuan Bersama

DEWAN PERWAKILAN RAKYAT REPUBLIK INDONESIA

dan

PRESIDEN REPUBLIK INDONESIA

MEMUTUSKAN:

Menetapkan: UNDANG-UNDANG TENTANG PELINDUNGAN DATA PRIBADI.

## BAB I — KETENTUAN UMUM

##### Pasal 1

Dalam Undang-Undang ini yang dimaksud dengan:

- 1\. Data Pribadi adalah …
- 2\. Pelindungan Data Pribadi adalah …

## BAB II — ASAS

##### Pasal 3

Undang-Undang ini berasaskan:

- a. {?pelindungan?};
- b. kepastian hukum;

…

Disahkan di Jakarta pada tanggal 17 Oktober 2022

PRESIDEN REPUBLIK INDONESIA,

ttd

JOKO WIDODO

…

LEMBARAN NEGARA REPUBLIK INDONESIA TAHUN 2022 NOMOR 196

# PENJELASAN ATAS UNDANG-UNDANG REPUBLIK INDONESIA NOMOR 27 TAHUN 2022 TENTANG PELINDUNGAN DATA PRIBADI

## I. UMUM

Perkembangan teknologi informasi dan komunikasi …

## II. PASAL DEMI PASAL

##### Pasal 1

Cukup jelas.

…

TAMBAHAN LEMBARAN NEGARA REPUBLIK INDONESIA NOMOR 6820
```

## 15. Lampiran B: Pemetaan ke Akoma Ntoso (Informatif)

Pemetaan ini disediakan untuk memudahkan konversi ke Akoma Ntoso di kemudian hari.
Pemetaan belum divalidasi terhadap skema Akoma Ntoso 1.0 dan dapat berubah.

| Unsur konvensi | Elemen Akoma Ntoso |
|---|---|
| Berkas transkripsi (batang tubuh) | `act` |
| Judul peraturan | `preface` / `docTitle` |
| Konsiderans | `preamble` / `recitals` / `recital` |
| Dasar hukum | `preamble` / `citations` / `citation` |
| Diktum | `preamble` / `formula` |
| Buku | `book` |
| BAB | `chapter` |
| Bagian | `section` |
| Paragraf | `subsection` |
| Pasal | `article` |
| Ayat | `paragraph` |
| Rincian | `list` / `point` |
| Penutup | `conclusions` |
| Penjelasan | `attachment` berisi dokumen penjelasan |
| Lampiran | `attachment` |
| Kutipan rumusan perubahan | `mod` / `quotedStructure` |

Pengenal FRBR konvensi ini dapat dipetakan ke pola IRI Akoma Ntoso sebagai berikut:

| Tingkat | Konvensi ini | Ilustrasi IRI Akoma Ntoso |
|---|---|---|
| Karya | `uu/2022/27` | `/akn/id/act/uu/2022-10-17/27` |
| Ekspresi | `uu/2022/27/ind@2022-10-17` | `/akn/id/act/uu/2022-10-17/27/ind@2022-10-17` |
| Manifestasi | `uu-2022-27.md` versi 1.0.0 | `/akn/id/act/uu/2022-10-17/27/ind@2022-10-17.akn` |

## 16. Lampiran C: Referensi

### 16.1. Referensi Normatif

- Undang-Undang Nomor 12 Tahun 2011 tentang Pembentukan Peraturan Perundang-undangan beserta perubahannya, yaitu Undang-Undang Nomor 15 Tahun 2019, Undang-Undang Nomor 13 Tahun 2022, dan Undang-Undang Nomor 1 Tahun 2026 tentang Penyesuaian Pidana (sepanjang mengubah Pasal 15), khususnya Lampiran II tentang Teknik Penyusunan Peraturan Perundang-undangan.
- CommonMark Spec, versi 0.31.2.
- GitHub Flavored Markdown Spec, versi 0.29-gfm (2019-04-06), ekstensi tabel.
- YAML Ain't Markup Language (YAML) versi 1.2.
- The Unicode Standard, Unicode Standard Annex #15: Unicode Normalization Forms.
- FIPS 180-4, Secure Hash Standard (SHA-256).
- ISO 8601, format tanggal dan waktu.
- ISO 639-3, kode bahasa.

### 16.2. Referensi Informatif

- Peraturan Presiden Nomor 33 Tahun 2012 tentang Jaringan Dokumentasi dan Informasi Hukum Nasional.
- Peraturan Menteri Hukum dan Hak Asasi Manusia Nomor 8 Tahun 2019 tentang Standar Pengelolaan Dokumen dan Informasi Hukum.
- Format integrasi data Portal JDIHN, Badan Pembinaan Hukum Nasional.
- Council conclusions inviting the introduction of the European Legislation Identifier (ELI), Dewan Uni Eropa, 2012.
- Akoma Ntoso Version 1.0, OASIS Standard, OASIS LegalDocML Technical Committee.
- IFLA, Functional Requirements for Bibliographic Records (FRBR).
- RFC 7322, RFC Style Guide.
- BCP 14 (RFC 2119 dan RFC 8174), kata kunci untuk menyatakan tingkat persyaratan.
- ISO/IEC Directives, Part 2: Principles and rules for the structure and drafting of ISO and IEC documents.

## 17. Lampiran D: Riwayat Perubahan

| Versi | Tanggal | Perubahan |
|---|---|---|
| 0.1.0 | 2026-10-26 | Draf pertama, dengan nama Konvensi Artup. Menambah [R-6] tentang rujukan ke versi draf dan mengubah L-06 (usulan 0003). Membatasi penerapan aturan format pada dokumen ini ke Bagian 4.1 (usulan 0001). Menyeragamkan pengenal dokumen menjadi `transkripsi-peraturan`, menghapus isian `digantikan_oleh`, dan menambah [R-7] dan [R-8] (usulan 0002). Mewajibkan penggabungan baris dalam blok penutup [S-13] dan memastikan satu hasil untuk N-8 (usulan 0004). Mempersempit [F-11], memperluas [F-12] dan [F-13], dan menambah [F-15] (usulan 0011). Memberi kode pada ketentuan yang belum berkode ([F-16], [C-5], [I-10], [V-8]), menambah [M-6], [M-7], dan [V-9], mengubah tabel Bagian 7 menjadi daftar berkode, dan menambahkan kata kunci normatif pada [S-2], [S-5], [S-8], [N-9], [N-11], [K-1], [K-5], dan [I-8] (usulan 0005). Menambah tingkat pemeriksaan, [V-10], [V-11], dan L-19 sampai L-21, serta membetulkan rujukan L-11, L-12, dan L-17 (usulan 0006). Menambah istilah dan catatan homonim di Bagian 2.2, membetulkan contoh Label, dan mengganti nama isian `ekspresi.bagian` menjadi `ekspresi.komponen` (usulan 0007). Membatasi [S-1] pada batang tubuh dan Penjelasan, memperjelas [S-2] dan [S-18], dan menambah [S-24] dan [S-25] (usulan 0008). Memindahkan [S-21] sampai [S-23] ke Bagian 6.10 agar berlaku di seluruh badan teks dan menambah [S-26] (usulan 0009). Mengubah isian `sumber` menjadi daftar dengan `sumber[].komponen`, menambah [M-8] dan [V-12], dan menyesuaikan L-17 (usulan 0012). Melengkapi [V-7] untuk versi sebelum `verified` dan penetapan `1.0.0`, dan menambah [V-13] (usulan 0014). Perbaikan redaksional: sifat acuan metadata di Bagian 1.4, langkah 2 Bagian 11.2, contoh Bagian 6.5 dan 6.7, serta referensi di Lampiran C (usulan 0015). Melengkapi daftar [C-1] dan [C-2], memperjelas [C-5], dan menjadikan `karya.penandatangan` "WAJIB bila ada" (usulan 0010). Melengkapi kode jenis [I-1] menurut Pasal 8 ayat (1) UU 12/2011 dan memecah `perkada`, menambah aturan nomenklatur pada [I-2], dan menambah fragmen Buku, Bagian, dan Paragraf (usulan 0013). |
