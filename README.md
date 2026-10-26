# Konvensi Artup

Konvensi Artup adalah dokumen konvensi untuk mentranskripsikan peraturan perundang-undangan Indonesia (UU, PP, Perpres, Permen, Perda, dan lainnya) dari naskah sumber, umumnya PDF salinan resmi, ke berkas Markdown.

Tujuannya adalah berkas transkripsi yang:

- setia 1:1 terhadap isi naskah sumber (nomor, judul, BAB, Pasal, ayat, rincian, tanggal, penandatangan), bukan terhadap tata letaknya;
- mudah dibaca manusia melalui penampil Markdown biasa dan mudah diolah mesin;
- dapat diverifikasi pihak ketiga, misalnya ahli hukum atau asosiasi;
- dapat dikunci dengan hash SHA-256 yang dicatat di register setelah diverifikasi.

## Asal nama

"Artup" adalah kata "putra" yang dibalik, dari nama penggagasnya, Ananda Putra.
Nama ini bukan singkatan dan tidak memiliki kepanjangan.

Berkas transkripsi tidak merujuk nama tersebut, melainkan pengenal teknis `transkripsi-peraturan/MAYOR.MINOR`, misalnya `transkripsi-peraturan/0.1`.

## Status

| Versi | Status | Berkas |
|---|---|---|
| 0.1.0 | Draf | [konvensi/konvensi-artup.md](konvensi/konvensi-artup.md) |

Belum ada versi final.
Daftar rilis dan nilai hash setiap versi final dicatat di [rilis/RILIS.md](rilis/RILIS.md).

## Isi repositori

| Lokasi | Isi |
|---|---|
| [konvensi/](konvensi/) | Dokumen kerja, yaitu draf yang sedang disunting |
| [rilis/](rilis/) | Salinan beku setiap versi final beserta daftar rilis |
| [usulan/](usulan/) | Usulan revisi, satu berkas per usulan |
| [alat/](alat/) | Pemeriksa dokumen konvensi |
| [TODO.md](TODO.md) | Pekerjaan konvensi yang belum selesai |
| [AGENTS.md](AGENTS.md) | Instruksi bagi agen AI yang membantu penyusunan |

## Mengusulkan perubahan

Setiap perubahan masuk melalui pull request di https://github.com/rekalogika/konvensi-artup.

1. Fork repositori ini, atau buat branch bila Anda memiliki akses tulis.
2. Salin [usulan/TEMPLAT.md](usulan/TEMPLAT.md) menjadi `usulan/NNNN-judul-singkat.md` dengan nomor urut berikutnya.
3. Isi latar belakang, aturan yang terdampak, rumusan lama dan baru, dampak terhadap berkas transkripsi yang sudah ada, dan kompatibilitas versi.
4. Buka pull request berjudul `Usulan NNNN: judul singkat`.
   Usulan dibahas di pull request tersebut dan diputuskan oleh penyusun.
5. Usulan yang diterima diterapkan pada dokumen kerja dalam pull request tersendiri dan dicatat dalam riwayat perubahan (Lampiran D).

Usulan dari pihak luar, misalnya ahli hukum atau asosiasi, sangat diharapkan dan mengikuti alur yang sama.
Bila tidak terbiasa dengan pull request, masukan juga dapat disampaikan melalui *issue* GitHub; penyusun akan menuliskannya sebagai usulan.

## Memeriksa dokumen

```sh
python3 -m venv .venv
.venv/bin/pip install -r alat/requirements.txt
.venv/bin/python alat/periksa_konvensi.py konvensi/konvensi-artup.md
```

Pemeriksa mencetak temuan dengan format `berkas:baris: pesan` dan keluar dengan kode bukan nol apabila ada temuan.

## Di luar repositori ini

Repositori ini hanya memuat dokumen konvensi.
Pekerjaan transkripsi peraturan, yaitu berkas transkripsi, PDF sumber, register transkripsi, dan alat pemeriksa berkas transkripsi, dikelola dalam proyek terpisah.

## Penyusun

Penggagas dan penyusun: Ananda Putra.
Draf 0.1.0 ditulis bersama Claude, model AI buatan Anthropic.
