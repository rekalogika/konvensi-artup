# Usulan 0006: Tabel Pemeriksaan Otomatis (Bagian 12)

| Identitas | Nilai |
|---|---|
| Nomor | 0006 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diajukan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | Bagian 11.1, Bagian 12 (L-06, L-11, L-12, L-17) |
| Jenis perubahan | redaksional / penambahan |
| Usulan versi berikutnya | MINOR |

## Latar Belakang

### A. Kewajiban menjalankan pemeriksaan tidak jelas

Paragraf pembuka Bagian 12 menyatakan pemeriksaan "SEBAIKNYA dijalankan", lalu "Pemeriksaan bertanda "verified" hanya wajib lolos sebelum status `verified`" ("wajib" berhuruf kecil).
Bagian 11.1 mendefinisikan `new transcription` sebagai berkas yang "lolos pemeriksaan format".
Jadi tidak jelas apakah lolos pemeriksaan merupakan syarat perubahan status.

### B. Kolom "Ketentuan" yang salah sasaran

| Kode | Masalah |
|---|---|
| L-06 | Merujuk "Bagian 13", bukan kode aturan; arti "dikenal" tidak didefinisikan (lihat usulan 0003). |
| L-11 | "Nomor Pasal berurutan" merujuk [S-1], padahal [S-1] mengatur tingkat heading. Selain itu, menurut [P-1] dan [P-2] transkripsi wajib mengikuti sumber, termasuk bila penomoran di sumber tidak berurutan. Jadi L-11 tidak boleh membuat berkas yang setia menjadi gagal. |
| L-12 | Merujuk [S-14], yang mengatur heading Penjelasan. Dalam peraturan perubahan, penjelasan pasal demi pasal memuat "Pasal I" dan label "Angka 1", sehingga daftarnya memang tidak sama dengan batang tubuh. |
| L-17 | Merujuk [V-3] (hash badan), padahal yang diuji adalah `sumber.sha256` (Bagian 9.3) dan langkah 3 Bagian 11.2. Frasa "berkas sumber yang diarsipkan" juga tidak didukung aturan mana pun (lihat usulan 0012). |

### C. Ketentuan yang dapat diperiksa mesin tetapi belum memiliki kode L

[F-12], [F-13] (sebagian ditangani L-13), [K-4], [M-3], [M-4], [I-3], [I-4] (kecocokan `ekspresi.id` dengan `karya.id`, `ekspresi.bahasa`, dan `ekspresi.tanggal`), [I-7], [S-6], [S-9], dan [S-10].

### D. Tidak ada tingkat temuan

Semua pemeriksaan diperlakukan sama, padahal L-11 dan L-12 seharusnya peringatan yang dikonfirmasi verifikator, bukan kegagalan.

## Rumusan Baru

Paragraf pembuka Bagian 12 (kode sementara):

```markdown
[V-10] Berkas transkripsi WAJIB lolos seluruh pemeriksaan bertingkat "galat" yang tidak bertanda "verified" sebelum berstatus `new transcription`, dan WAJIB lolos seluruh pemeriksaan bertingkat "galat" sebelum berstatus `verified`.

[V-11] Setiap temuan pemeriksaan bertingkat "peringatan" WAJIB diperiksa verifikator terhadap naskah sumber dan, apabila sesuai sumber, dicatat dalam isian `catatan` pada entri verifikasi.
```

Tabel Bagian 12 ditambah kolom "Tingkat" (`galat` atau `peringatan`):

| Kode | Perubahan |
|---|---|
| L-06 | Ketentuan: `R-1` (dan `R-8` bila usulan 0003 diterima) |
| L-11 | Tingkat: peringatan; Ketentuan: `P-1` |
| L-12 | Tingkat: peringatan; Ketentuan: `P-1, S-14` |
| L-17 | Ketentuan: `M-6` (usulan 0005) dan Bagian 11.2 |

Kode baru L-19 dan seterusnya untuk butir C dipilih bersama saat penerapan; kode L tidak dipakai ulang.

## Dampak terhadap Berkas Transkripsi

- Berkas yang sebelumnya gagal L-11 atau L-12 karena setia pada sumber kini cukup diberi catatan verifikator.
- Alat pemeriksa berkas transkripsi perlu mendukung tingkat temuan dan pemeriksaan baru.

## Kompatibilitas Versi

MINOR: [V-10] mengubah anjuran menjadi kewajiban.

## Keputusan
