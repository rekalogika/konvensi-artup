# Usulan 0002: Identitas dan Frontmatter Dokumen Konvensi

| Identitas | Nilai |
|---|---|
| Nomor | 0002 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diajukan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | Frontmatter dokumen, tabel identitas, [R-3], [R-5] |
| Jenis perubahan | redaksional / penambahan |
| Usulan versi berikutnya | PATCH |

## Latar Belakang

Ada tiga masalah pada identitas dokumen konvensi.

1. **Dua pengenal.**
   Frontmatter `id` dan tabel identitas memakai `konvensi/transkripsi-peraturan`.
   Sementara itu, [R-5] menyebut pengenal teknis `transkripsi-peraturan`, dan berkas transkripsi merujuk `transkripsi-peraturan/0.1`.
   Hubungan kedua bentuk ini tidak dijelaskan.
2. **`digantikan_oleh` bertentangan dengan [R-3].**
   Frontmatter memuat `digantikan_oleh: null`.
   Setelah versi final dibekukan, isian ini tidak pernah dapat diisi tanpa melanggar [R-3] ("Versi konvensi yang telah final TIDAK BOLEH diubah").
   Ini masalah yang sama dengan yang diatasi [M-2] untuk berkas transkripsi: informasi yang berubah tidak boleh ada di berkas yang di-hash.
3. **Isian frontmatter dokumen tidak didefinisikan.**
   `id`, `nama`, `judul`, `versi`, `status`, `tanggal`, `bahasa`, `penyusun`, `menggantikan`, dan `digantikan_oleh` tidak dijelaskan di mana pun.
   Demikian pula nilai `status` yang sah (sementara ini alat pemeriksa menganggap `draf` dan `final`).

## Rumusan Lama

Frontmatter:

```yaml
id: konvensi/transkripsi-peraturan
…
menggantikan: null
digantikan_oleh: null
```

[R-5]:

```markdown
[R-5] "Konvensi Artup" adalah nama dokumen ini, sedangkan `transkripsi-peraturan` adalah pengenal teknisnya.
```

## Rumusan Baru

1. Frontmatter: ganti `id` menjadi `transkripsi-peraturan` dan hapus `digantikan_oleh`.
   Tabel identitas mengikuti.
2. Tambahkan subbagian baru di akhir Bagian 13 (Bagian 13.1 bila Bagian 13 dipecah menjadi subbagian; nomor ditetapkan saat penerapan).
   Kode aturan bersifat sementara; semula [R-6] dan [R-7], digeser karena [R-6] telah dipakai oleh usulan 0003:

```markdown
[R-7] Frontmatter dokumen konvensi WAJIB memuat isian `id`, `nama`, `judul`, `versi`, `status`, dan `tanggal`, dan BOLEH memuat `bahasa`, `penyusun`, dan `menggantikan`.
Nilai `id` WAJIB sama dengan pengenal teknis menurut [R-5].
Nilai `status` WAJIB berupa `draf` atau `final`.

[R-8] Relasi "digantikan oleh" antarversi konvensi WAJIB dicatat dalam daftar rilis konvensi, bukan di dalam dokumen konvensi.
```

## Dampak terhadap Berkas Transkripsi

Tidak ada.
Berkas transkripsi tetap merujuk `transkripsi-peraturan/MAYOR.MINOR`.

## Kompatibilitas Versi

PATCH untuk perubahan frontmatter; MINOR bila [R-7] dan [R-8] dianggap penambahan ketentuan.
Selama belum ada rilis final, keduanya dapat masuk ke versi 0.1.0.

## Alternatif yang Dipertimbangkan

- Mempertahankan `konvensi/transkripsi-peraturan` sebagai pengenal seri dokumen ("konvensi/…") untuk visi seri RFC.
  Bila dipilih, [R-5] perlu menjelaskan bahwa awalan `konvensi/` adalah ruang nama seri dan tidak dipakai dalam rujukan berkas transkripsi.

## Keputusan
