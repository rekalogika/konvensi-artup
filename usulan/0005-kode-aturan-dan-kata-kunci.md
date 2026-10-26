# Usulan 0005: Ketentuan Tanpa Kode dan Kode Tanpa Kata Kunci

| Identitas | Nilai |
|---|---|
| Nomor | 0005 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diajukan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | Bagian 2.1, 4.1, 5, 7, 9.3, 9.4, 10.1, 11.1, 11.5; [S-2], [S-5], [S-8], [S-13], [N-11], [K-1], [K-5], [I-8] |
| Jenis perubahan | redaksional / penambahan |
| Usulan versi berikutnya | PATCH, kecuali M-6, M-7, dan V-8 (MINOR) |

## Latar Belakang

Bagian 2.1 menyatakan "Setiap ketentuan normatif diberi kode dalam kurung siku".
Ada tiga jenis penyimpangan.

### A. Format kode tidak seragam

N-2 sampai N-9 hanya ditulis di kolom "Kode" sebuah tabel, tanpa kurung siku, sedangkan N-1 dan N-10 sampai N-12 ditulis di prosa.

### B. Ketentuan berkata kunci tanpa kode

| Letak | Ketentuan |
|---|---|
| Bagian 4.1, paragraf terakhir | Repositori … SEBAIKNYA mencegah pengubahan akhir baris … |
| Bagian 5, paragraf pembuka | Unsur yang tidak tercantum … WAJIB dilaporkan dan diputuskan … |
| Bagian 10.1 | … pengenal BOLEH diawali URI dasar … |
| Bagian 11.5, paragraf terakhir | Register SEBAIKNYA disimpan sebagai berkas data terstruktur … |
| Bagian 12, paragraf pembuka | Pemeriksaan … SEBAIKNYA dijalankan …; "hanya wajib lolos" (huruf kecil); lihat usulan 0006 |

Tabel normatif juga tidak ditambatkan ke kode mana pun:

- tabel isian Bagian 9.3 (kolom "Wajib" dan "Tipe");
- tabel entri verifikasi Bagian 9.4;
- tabel status Bagian 11.1.

L-05 menguji "seluruh isian WAJIB dengan tipe yang benar" dan merujuk M-1 s.d. M-5, padahal tidak satu pun dari kelima aturan itu mewajibkan isian tabel 9.3.

### C. Ketentuan berkode tanpa kata kunci

[S-5] ("Pembukaan tidak diberi heading"), [S-8] ("ditulis"), kalimat ketiga [S-2] ("digabung"), kalimat pertama [S-13], N-9 ("dipertahankan"), [N-11] ("tidak ditranskripsi"), [K-1] (deskriptif), kalimat kedua [K-5] ("Verifikator menghapus"), dan kalimat pertama [I-8] ("dirujuk").
Tanpa kata kunci, tingkat kewajibannya tidak dapat dipastikan.

## Rumusan Baru

A. Ubah tabel Bagian 7 menjadi daftar butir seperti Bagian 4.1:

```markdown
- [N-2] Pemenggalan kata di akhir baris karena tata letak WAJIB disambung kembali.
  Tanda hubung yang merupakan bagian kata, misalnya "perundang-undangan", WAJIB dipertahankan.
- [N-3] …
```

B. Beri kode baru (nomor sementara, ditetapkan saat penerapan):

```markdown
[F-15] Repositori yang menyimpan berkas transkripsi SEBAIKNYA mencegah pengubahan akhir baris secara otomatis, misalnya dengan entri `*.md -text` dalam berkas `.gitattributes`.

[C-5] Unsur yang tidak tercantum dalam salah satu daftar WAJIB dilaporkan dan diputuskan dalam revisi konvensi.

[I-10] Apabila diterbitkan di web, pengenal BOLEH diawali URI dasar, misalnya `https://contoh.id/eli/`.

[V-8] Register SEBAIKNYA disimpan sebagai berkas data terstruktur (misalnya CSV atau YAML) dalam repositori berversi, dan BOLEH ditampilkan sebagai tabel Markdown.

[M-6] Frontmatter WAJIB memuat setiap isian yang bertanda WAJIB pada tabel Bagian 9.3, dan setiap isian bertanda "WAJIB bila ada" apabila informasinya terdapat dalam naskah sumber.
Nilai setiap isian WAJIB sesuai dengan kolom Tipe.
Isian yang tidak tercantum pada tabel Bagian 9.3 TIDAK BOLEH dipakai.

[M-7] Setiap entri verifikasi WAJIB memuat isian yang bertanda WAJIB pada tabel Bagian 9.4.

[V-9] Status berkas transkripsi di register WAJIB berupa salah satu nilai pada tabel Bagian 11.1.
```

Arti setiap tipe pada tabel Bagian 9.3 (string, bilangan, tanggal, objek, daftar) perlu didefinisikan bersama [M-6].
Untuk tipe tanggal perlu dinyatakan apakah ditulis sebagai string berkutip atau tanpa kutip, karena skema inti YAML 1.2 tidak mengenal tipe tanggal.
L-05 lalu merujuk `M-1 s.d. M-7`.

C. Rumusan ulang tanpa mengubah makna, misalnya:

```markdown
[S-5] Pembukaan TIDAK BOLEH diberi heading.
[S-8] Isi Pasal yang tidak terbagi atas ayat WAJIB ditulis sebagai satu atau beberapa paragraf setelah heading Pasal.
[N-11] Cetak tebal dan garis bawah di sumber TIDAK BOLEH ditranskripsi sebagai markup.
```

## Dampak terhadap Berkas Transkripsi

- A dan C: tidak ada.
- [M-6]: kalimat "Isian yang tidak tercantum … TIDAK BOLEH dipakai" dapat membuat berkas dengan isian tambahan menjadi tidak sesuai.
  Bila tidak dikehendaki, kalimat ini dapat dihapus.

## Kompatibilitas Versi

A, C, dan kode baru untuk ketentuan yang sudah ada: PATCH.
[M-6] (kalimat ketiga), [M-7], dan [V-9]: MINOR.

## Keputusan
