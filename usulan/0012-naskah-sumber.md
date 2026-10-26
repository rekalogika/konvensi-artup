# Usulan 0012: Naskah Sumber Lebih dari Satu Berkas dan Pengarsipannya

| Identitas | Nilai |
|---|---|
| Nomor | 0012 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diajukan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | Bagian 9.3 (`sumber.*`), Bagian 11.2, L-17 |
| Jenis perubahan | perubahan tidak kompatibel |
| Usulan versi berikutnya | MINOR (MAYOR masih 0) |

## Latar Belakang

1. **Satu berkas sumber.**
   Isian `sumber` berupa satu objek dengan satu `berkas`, satu `url`, dan satu `sha256`.
   Penjelasan atau Lampiran dapat diterbitkan sebagai berkas PDF terpisah dari batang tubuh (perlu dicontohkan dengan peraturan nyata).
   [P-6] mewajibkan satu berkas transkripsi memuat Penjelasan dan Lampirannya, sehingga berkas tersebut membutuhkan lebih dari satu sumber.
2. **Pengarsipan tidak diwajibkan.**
   Verifikasi pihak ketiga bergantung pada kemampuan mengambil kembali naskah sumber yang hashnya sama dengan `sumber.sha256`.
   URL dapat berubah atau hilang.
   L-17 menyebut "berkas sumber yang diarsipkan", tetapi tidak ada aturan yang mewajibkan pengarsipan.

## Rumusan Baru

`sumber` menjadi daftar; setiap butir memuat isian yang sama seperti sekarang ditambah:

| Isian | Wajib | Tipe | Keterangan |
|---|---|---|---|
| `sumber[].komponen` | WAJIB | daftar | Komponen naskah yang bersumber dari berkas ini: `batang-tubuh`, `penjelasan`, `lampiran` (lihat usulan 0007) |

```markdown
[V-12] Setiap naskah sumber yang tercantum di `sumber` WAJIB diarsipkan oleh pengelola register sedemikian rupa sehingga dapat diambil kembali dan dicocokkan dengan nilai `sha256`-nya selama berkas transkripsi berstatus `verified` atau `superseded`.
```

## Dampak terhadap Berkas Transkripsi

Setiap berkas yang ada perlu mengubah `sumber` dari objek menjadi daftar satu butir.

## Kompatibilitas Versi

MINOR (tidak kompatibel; MAYOR masih 0).

## Alternatif yang Dipertimbangkan

- Mempertahankan `sumber` sebagai objek dan menambah `sumber_tambahan` sebagai daftar: kompatibel, tetapi menghasilkan dua bentuk untuk hal yang sama.
- Menggabungkan PDF sumber menjadi satu berkas sebelum di-hash: tidak dipilih karena hash tidak lagi sama dengan berkas yang dapat diunduh dari penyedia.

## Keputusan
