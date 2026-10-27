# Usulan 0022: Kata Kunci Normatif pada Setiap Ketentuan Berkode

| Identitas | Nilai |
|---|---|
| Nomor | 0022 |
| Pengusul | Claude (Anthropic), atas permintaan Ananda Putra |
| Tanggal | 2026-10-27 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [I-1], [K-3], [R-1], [R-4] |
| Jenis perubahan | redaksional |
| Usulan versi berikutnya | PATCH |

## Latar Belakang

Bagian 2.1 menyatakan bahwa setiap ketentuan normatif diberi kode, dan usulan 0005 sudah menertibkan sebagian besar penyimpangannya.
Pemeriksaan heuristik baru di `alat/periksa_konvensi.py --gaya` (pull request 26) menemukan empat sisa:

- Bagian 10.2: kalimat "Bentuk kedua WAJIB dipakai …" terletak sesudah blok kode [I-1], sehingga terpisah dari paragraf berkodenya;
- [K-3], [R-1], dan [R-4] dirumuskan sebagai pernyataan tanpa kata kunci, sehingga tingkat kewajibannya tidak tampak.

## Rumusan Lama

```markdown
[I-1] Pengenal karya WAJIB berbentuk:

(blok kode dua bentuk pengenal)

Bentuk kedua WAJIB dipakai untuk jenis yang dapat dibentuk oleh lebih dari satu lembaga atau daerah.

[K-3] Penanda keraguan pada sebuah label berlaku untuk seluruh entri yang dimulai oleh label tersebut.

[R-1] Konvensi diberi versi `MAYOR.MINOR.PATCH`.
Berkas transkripsi merujuknya dengan `transkripsi-peraturan/MAYOR.MINOR`.

[R-4] Berkas transkripsi yang telah `verified` tetap sah menurut versi konvensi yang dirujuknya, meskipun versi konvensi yang lebih baru telah terbit.
```

## Rumusan Baru

```markdown
[I-1] Pengenal karya WAJIB berbentuk salah satu dari dua bentuk berikut; bentuk kedua WAJIB dipakai untuk jenis yang dapat dibentuk oleh lebih dari satu lembaga atau daerah:

(blok kode dua bentuk pengenal, tidak berubah)

[K-3] Penanda keraguan pada sebuah label WAJIB diperlakukan sebagai keraguan atas seluruh entri yang dimulai oleh label tersebut.

[R-1] Versi konvensi WAJIB berbentuk `MAYOR.MINOR.PATCH`.
Berkas transkripsi WAJIB merujuk versi konvensi dengan bentuk `transkripsi-peraturan/MAYOR.MINOR`.

[R-4] Berkas transkripsi yang telah `verified` WAJIB dinilai menurut versi konvensi yang dirujuknya.
Terbitnya versi konvensi yang lebih baru tidak membuat berkas tersebut menjadi tidak sesuai.
```

## Dampak terhadap Berkas Transkripsi

Tidak ada.
Isi setiap ketentuan tetap sama; hanya tingkat kewajiban yang sebelumnya tersirat kini dinyatakan.
Bentuk rujukan pada [R-1] sudah diwajibkan oleh pola isian `konvensi` di Lampiran C ([M-9]).

## Kompatibilitas Versi

PATCH: perbaikan redaksional yang tidak mengubah ketentuan ([R-2]), ditampung di draf 0.1.0.

## Alternatif yang Dipertimbangkan

- Mengecualikan ketentuan berupa pernyataan dari pemeriksaan, seperti kelompok P: tidak dipilih, karena [K-3], [R-1], dan [R-4] mengatur perilaku transkriptor, verifikator, atau alat, bukan prinsip.
- Memberi kode baru pada kalimat sesudah blok kode [I-1]: tidak dipilih, karena kalimat itu bagian dari ketentuan yang sama.

## Keputusan

2026-10-27, diputuskan oleh Claude atas kuasa Ananda Putra: diterima.
Diterapkan pada draf 0.1.0 tanpa menaikkan versi.
Setelah penerapan, `alat/periksa_konvensi.py --gaya` tidak lagi menimbulkan temuan `kata-kunci`.
