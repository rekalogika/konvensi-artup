# Usulan 0014: Versi Berkas Transkripsi

| Identitas | Nilai |
|---|---|
| Nomor | 0014 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diajukan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [V-5], [V-7], Bagian 9.5, [I-5] |
| Jenis perubahan | penambahan |
| Usulan versi berikutnya | MINOR |

## Latar Belakang

1. **Kapan versi 1.0.0 diberikan tidak diatur.**
   [V-7] menyatakan `0.x.y` untuk berkas yang belum pernah `verified`, tetapi tidak menyatakan kapan dan oleh siapa versi menjadi `1.0.0`.
   Contoh frontmatter Bagian 9.5 memakai `versi: 1.0.0` bersama entri verifikasi; bila versi dinaikkan setelah entri verifikasi ditambahkan, hal itu sah ([V-1] hanya membekukan badan teks), tetapi urutannya perlu dinyatakan.
2. **PATCH dan perubahan sebelum `verified` tidak diatur.**
   [V-7] hanya mengatur MAYOR dan MINOR setelah `verified`.
3. **Versi lama dan nama berkas yang sama.**
   [I-5] menetapkan nama berkas dari pengenal karya, sehingga semua versi transkripsi suatu karya memiliki nama berkas yang sama.
   [V-5] menyatakan versi lama berstatus `superseded`, tetapi tidak mewajibkan versi lama tetap dapat diambil kembali, padahal hashnya tetap tercatat di register.

## Rumusan Baru

```markdown
[V-7] `transkripsi.versi` WAJIB mengikuti pola `MAYOR.MINOR.PATCH`:

- `0.x.y` untuk berkas yang belum pernah berstatus `verified`; MINOR dinaikkan untuk setiap perubahan badan teks dan PATCH untuk perubahan frontmatter saja;
- `1.0.0` ditetapkan setelah entri verifikasi terakhir ditambahkan dan sebelum hash berkas dihitung ([V-4]);
- naik MAYOR untuk perubahan badan teks setelah `verified`;
- naik MINOR untuk perubahan frontmatter yang tidak mengubah badan teks setelah `verified`.

[V-13] Setiap versi berkas transkripsi yang pernah berstatus `verified` WAJIB tetap dapat diambil kembali dengan isi byte yang sama, misalnya melalui riwayat repositori berversi, selama hashnya tercatat di register.
```

## Dampak terhadap Berkas Transkripsi

Berkas `verified` yang sudah ada tidak terdampak.
Berkas yang sedang dalam verifikasi mengikuti urutan baru.

## Kompatibilitas Versi

MINOR.

## Keputusan
