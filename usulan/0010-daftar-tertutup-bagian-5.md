# Usulan 0010: Melengkapi Daftar Tertutup Bagian 5

| Identitas | Nilai |
|---|---|
| Nomor | 0010 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | [C-1], [C-2], Bagian 5 (paragraf pembuka), `karya.penandatangan` |
| Jenis perubahan | penambahan |
| Usulan versi berikutnya | MINOR |

## Latar Belakang

Bagian 5 menyatakan kedua daftar bersifat tertutup dan unsur yang tidak tercantum wajib dilaporkan.
Unsur berikut tidak tercantum di [C-1] maupun [C-2].
**Seluruh fakta di bawah ini perlu dicocokkan dengan naskah contoh sebelum rumusan ditetapkan** (lihat TODO.md).

1. **Nomor register Peraturan Daerah.**
   Peraturan Daerah memuat keterangan "NOREG PERATURAN DAERAH …" setelah keterangan penempatan dalam Lembaran Daerah, berdasarkan pedoman pembentukan produk hukum daerah dari Kementerian Dalam Negeri (perlu diverifikasi: Permendagri 80/2015 sebagaimana diubah).
   Keterangan ini merupakan bagian naskah, bukan tambahan salinan.
2. **Kalimat pengesahan Undang-Undang yang tidak ditandatangani Presiden.**
   Pasal 73 UU 12/2011 mengatur bahwa RUU yang tidak ditandatangani dalam 30 hari sah menjadi Undang-Undang dengan kalimat pengesahan "Undang-Undang ini dinyatakan sah berdasarkan ketentuan Pasal 20 ayat (5) Undang-Undang Dasar Negara Republik Indonesia Tahun 1945" (nomor ayat dan rumusan perlu diverifikasi; contoh yang perlu diperiksa: UU 2/2018).
   [C-1] butir 9 tidak menyebut kalimat ini, dan `karya.penandatangan` bertanda WAJIB padahal tidak ada pejabat yang mengesahkan.
3. **Tulisan "SALINAN" di halaman pertama salinan resmi.**
   [C-2] butir 1 menyebut kop halaman, dan butir 5 menyebut blok "Salinan sesuai dengan aslinya", tetapi tidak menyebut tulisan "SALINAN" itu sendiri.
4. **Teks tambahan penyedia.**
   Salinan dari situs JDIH dapat memuat alamat situs, keterangan unduhan, atau tanda penyedia di kaki atau kepala halaman.
   [C-2] butir 3 hanya menyebut "kode pada kaki halaman".
5. **Tidak ada aturan peralihan untuk unsur yang belum terdaftar.**
   Selama unsur baru belum diputuskan, transkriptor tidak tahu apakah unsur itu ditranskripsi.

## Rumusan Baru

[C-1], butir baru di akhir daftar agar nomor butir yang ada tidak bergeser (urutan transkripsi tetap mengikuti [C-4]):

```markdown
14. Nomor register peraturan daerah, misalnya "NOREG PERATURAN DAERAH PROVINSI …".
```

[C-1] butir 9, tambahan:

```markdown
9. Penutup: … dan nama pejabat, atau kalimat pengesahan apabila Undang-Undang sah tanpa tanda tangan Presiden.
```

`karya.penandatangan` menjadi "WAJIB bila ada".

[C-2], butir baru:

```markdown
9. Tulisan "SALINAN" yang menandai berkas sebagai salinan.
10. Teks yang ditambahkan oleh penyedia salinan, misalnya alamat situs, keterangan unduhan, atau tanda penyedia.
```

Bagian 5, paragraf pembuka (bersama [C-5] usulan 0005):

```markdown
Selama unsur tersebut belum diputuskan, unsur itu WAJIB ditranskripsi dengan penanda keraguan (Bagian 8.2), sehingga berkas tidak dapat berstatus `verified` ([K-5]).
```

Catatan: rumusan terakhir ini memperluas arti penanda keraguan dari "teks belum pasti" menjadi juga "unsur belum diputuskan".
Pilihan lainnya adalah melarang status `verified` secara langsung, tanpa memakai penanda.

## Dampak terhadap Berkas Transkripsi

Berkas Perda yang tidak memuat Noreg, atau yang memuat tulisan "SALINAN", menjadi tidak sesuai.

## Kompatibilitas Versi

MINOR.

## Keputusan

2026-10-26, diputuskan oleh Claude atas kuasa Ananda Putra: **diterima**, dengan alternatif untuk butir 5.

Verifikasi fakta:

- Kalimat pengesahan: menurut [teks UU 12/2011 di Wikisource](https://id.wikisource.org/wiki/Undang-Undang_Republik_Indonesia_Nomor_12_Tahun_2011), Pasal 73 menetapkan bahwa RUU yang tidak ditandatangani Presiden dalam 30 hari sah menjadi Undang-Undang, dengan kalimat pengesahan "Undang-Undang ini dinyatakan sah berdasarkan ketentuan Pasal 20 ayat (5) Undang-Undang Dasar Negara Republik Indonesia Tahun 1945" yang dibubuhkan pada halaman terakhir.
  Rumusan konvensi hanya merujuk "Pasal 73 UU 12/2011" tanpa nomor ayat, karena perubahan pasal tersebut oleh UU 13/2022 belum diperiksa.
  Contoh naskah (UU 2/2018) tidak diperiksa dan tidak diperlukan oleh rumusan.
- Noreg: [Perda Kabupaten Pohuwato Nomor 2 Tahun 2022](https://pasal.id/peraturan/perda/perda-kab-pohuwato-no-2-tahun-2022) memuat baris "NOREG PERATURAN DAERAH KABUPATEN POHUWATO PROVINSI GORONTALO …" tepat setelah baris Lembaran Daerah; dasar penempatannya adalah Lampiran III Permendagri 80/2015 sebagaimana diubah Permendagri 120/2018 ([JDIH BPK](https://peraturan.bpk.go.id/Details/164459/permendagri-no-80-tahun-2015)).

Penerapan:

- [C-1] butir 9 ditambah kalimat pengesahan; butir 14 (Noreg) ditambahkan di akhir daftar agar nomor butir yang ada tidak bergeser; definisi "Penutup" di Bagian 2.2 ikut menyebut butir 14.
- `karya.penandatangan` menjadi "WAJIB bila ada".
- [C-2] butir 9 dan 10 ditambahkan sesuai rumusan.
- Butir 5: dipilih alternatif tanpa penanda keraguan, agar arti penanda keraguan tetap "teks belum pasti".
  [C-5] ditambah kalimat: unsur yang belum diputuskan SEBAIKNYA ditranskripsi, dan berkasnya TIDAK BOLEH berstatus `verified`.

Diterapkan pada draf 0.1.0 tanpa menaikkan versi.
