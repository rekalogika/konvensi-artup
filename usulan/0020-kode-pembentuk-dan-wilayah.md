# Usulan 0020: Kode Pembentuk dan Kode Wilayah

| Identitas | Nilai |
|---|---|
| Nomor | 0020 |
| Pengusul | Claude (Anthropic), atas keputusan Ananda Putra |
| Tanggal | 2026-10-27 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [I-1] (kolom pembentuk), [I-2], [I-3], [I-5] (contoh), lampiran Referensi |
| Jenis perubahan | perubahan tidak kompatibel |
| Usulan versi berikutnya | MINOR (MAYOR masih 0) |

## Latar Belakang

[I-2] mewajibkan kode kementerian dan kode lembaga diambil dari "daftar kode yang dikelola bersama register", tetapi daftar itu belum ada, dan register berada di proyek terpisah.
TODO.md meminta daftar itu disusun, termasuk aturan untuk perubahan nomenklatur (usulan 0013).

Penelitian untuk menyusun daftar menunjukkan masalahnya:

- Nomenklatur kementerian sering berubah; Peraturan Presiden Nomor 139 Tahun 2024 menetapkan 48 kementerian Kabinet Merah Putih ([Setkab](https://setkab.go.id/inilah-kementerian-negara-kabinet-merah-putih/)), dan banyak peraturan yang masih berlaku ditetapkan dengan nomenklatur lama (misalnya Permenkumham 8/2019).
- Daftar yang mencakup seluruh nomenklatur historis kementerian dan lembaga besar, rawan salah, dan terus tertinggal; kode singkatan seperti `kemenkeu` tidak memiliki sumber resmi yang seragam.

Untuk kode wilayah, [I-2] hanya menyebut "kode ... yang ditetapkan Kementerian Dalam Negeri" tanpa menyebut keputusan dan waktu yang berlaku.
Keputusan yang berlaku saat ini adalah Keputusan Menteri Dalam Negeri Nomor 300.2.2-2138 Tahun 2025 tentang Pemberian dan Pemutakhiran Kode, Data Wilayah Administrasi Pemerintahan, dan Pulau, sebagaimana diubah dengan Nomor 300.2.2-2430 Tahun 2025 yang ditetapkan 23 Juni 2025 ([Paralegal.id](https://paralegal.id/peraturan/keputusan-menteri-dalam-negeri-nomor-300-2-2-2430-tahun-2025/)); keputusan ini menggantikan Kepmendagri 100.1.1-6117 Tahun 2022 ([ANTARA](https://www.antaranews.com/berita/4837297/kemendagri-luncurkan-kepmen-kode-wilayah-administrasi-2025)).

## Rumusan Lama

```markdown
[I-2] Kode kementerian dan kode lembaga WAJIB diambil dari daftar kode yang dikelola bersama register.
Kode wilayah WAJIB memakai kode wilayah administrasi pemerintahan yang ditetapkan Kementerian Dalam Negeri, dengan titik diganti tanda hubung.
Kode pembentuk WAJIB mengikuti nomenklatur pembentuk pada tanggal penetapan peraturan dan TIDAK BOLEH diubah karena perubahan nomenklatur di kemudian hari.
```

## Rumusan Baru

```markdown
[I-2] Segmen `pembentuk` untuk `permen` dan `perlem` WAJIB dibentuk dari nama pembentuk sebagaimana tertulis dalam judul peraturan, yaitu teks setelah kata "Peraturan" sampai sebelum kata "Nomor", tanpa frasa "Republik Indonesia" dan, untuk `permen`, tanpa kata "Menteri" di awal, lalu dinormalisasi menurut [I-3].
Contoh: "PERATURAN MENTERI KEUANGAN REPUBLIK INDONESIA NOMOR …" menjadi `keuangan`, "PERATURAN BADAN PENGAWAS OBAT DAN MAKANAN NOMOR …" menjadi `badan-pengawas-obat-dan-makanan`, dan "PERATURAN MAHKAMAH AGUNG REPUBLIK INDONESIA NOMOR …" menjadi `mahkamah-agung`.
Kode wilayah WAJIB memakai kode wilayah administrasi pemerintahan menurut keputusan Menteri Dalam Negeri tentang pemberian dan pemutakhiran kode, data wilayah administrasi pemerintahan, dan pulau yang berlaku pada tanggal penetapan peraturan, dengan titik diganti tanda hubung.
Kode pembentuk WAJIB mengikuti nomenklatur pembentuk pada tanggal penetapan peraturan dan TIDAK BOLEH diubah karena perubahan nomenklatur atau wilayah di kemudian hari.
```

[I-3] juga berlaku untuk segmen `pembentuk` tersebut.
Kolom pembentuk pada tabel [I-1] dan contoh pengenal (`permen/keuangan/2023/12`, `permen-keuangan-2023-12.md`) disesuaikan.
Keputusan Mendagri yang berlaku saat ini dicantumkan di lampiran Referensi (informatif).

Kelebihan aturan ini:

- kode dapat diturunkan dan diperiksa oleh siapa pun dari naskah itu sendiri, tanpa daftar terpisah;
- nomenklatur pada tanggal penetapan otomatis terwakili, sehingga perubahan nomenklatur tidak menimbulkan bentrokan;
- tidak ada daftar yang perlu dipelihara atau yang dapat keliru.

Kekurangannya: pengenal menjadi lebih panjang, misalnya `permen/hukum-dan-hak-asasi-manusia/2019/8`, dan pembentuk yang sama dapat memiliki kode berbeda pada masa nomenklatur yang berbeda (yang memang dikehendaki oleh kalimat terakhir [I-2]).

## Dampak terhadap Berkas Transkripsi

Pengenal dan nama berkas Peraturan Menteri dan peraturan lembaga yang memakai kode singkatan (misalnya `permen/kemenkeu/…`) berubah.
Belum ada berkas berstatus `verified`.

## Kompatibilitas Versi

MINOR (tidak kompatibel; MAYOR masih 0), ditampung di draf 0.1.0.

## Alternatif yang Dipertimbangkan

- Daftar kode sebagai lampiran normatif konvensi: tidak dipilih, karena setiap kementerian atau lembaga baru akan memerlukan versi konvensi baru, dan nomenklatur historis harus diteliti satu per satu.
- Daftar kode di register (rumusan lama): tidak dipilih, karena pihak ketiga tidak dapat memverifikasi pengenal tanpa register, dan register berada di luar konvensi.

## Keputusan

2026-10-27, Ananda Putra: laksanakan seluruh usulan penyelarasan dengan acuan, termasuk penyusunan daftar kode kementerian/lembaga.
Claude, atas kuasa Ananda, mengganti daftar tersebut dengan aturan pembentukan kode karena alasan di atas.
Diterapkan pada draf 0.1.0 tanpa menaikkan versi.
