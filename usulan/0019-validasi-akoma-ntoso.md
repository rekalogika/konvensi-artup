# Usulan 0019: Validasi Pemetaan Akoma Ntoso

| Identitas | Nilai |
|---|---|
| Nomor | 0019 |
| Pengusul | Claude (Anthropic), atas keputusan Ananda Putra |
| Tanggal | 2026-10-27 |
| Status | diterapkan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | Lampiran B (informatif), lampiran Referensi |
| Jenis perubahan | redaksional |
| Usulan versi berikutnya | PATCH |

## Latar Belakang

Lampiran B menyatakan pemetaannya "belum divalidasi terhadap skema Akoma Ntoso 1.0".
Pemetaan Penjelasan dan Lampiran juga masih samar ("`attachment` berisi dokumen penjelasan").

## Hasil Verifikasi

- **Skema XML** `akomantoso30.xsd` dari OASIS (https://docs.oasis-open.org/legaldocml/akn-core/v1.0/os/part2-specs/schemas/akomantoso30.xsd, ruang nama `http://docs.oasis-open.org/legaldocml/ns/akn/3.0`) mendeklarasikan seluruh elemen yang dipakai Lampiran B: `act`, `body`, `preface`, `docTitle`, `preamble`, `recitals`, `recital`, `citations`, `citation`, `formula`, `book`, `chapter`, `section`, `subsection`, `article`, `paragraph`, `list`, `point`, `conclusions`, `attachments`, `attachment`, `doc`, `mod`, dan `quotedStructure`.
- `preamble` boleh memuat `citations`, `recitals`, dan `formula`; jadi konsiderans, dasar hukum, dan diktum dapat berada di dalamnya.
- `attachment` memuat dokumen (antara lain `act` atau `doc`); `doc` mewajibkan atribut `name`.
  Karena itu Penjelasan dan Lampiran dipetakan ke `attachments` / `attachment` / `doc` dengan `name="penjelasan"` atau `name="lampiran"`.
- **Naming Convention 1.0** (https://docs.oasis-open.org/legaldocml/akn-nc/v1.0/akn-nc-v1.0.html): IRI karya `/akn/{negara}/{jenis}[/{subjenis}][/{aktor}]/{tanggal}/{nomor}`, IRI ekspresi menambahkan `/{bahasa}@{versi}`, dan manifestasi menambahkan akhiran format, dengan `.akn` untuk paket.
  Kode negara mengikuti ISO 3166-1, dan kode bahasa ISO 639-2 alpha-3.
  Ilustrasi IRI di Lampiran B sesuai dengan pola ini.

## Rumusan Baru

- Paragraf pembuka Lampiran B menyatakan bahwa pemetaan telah dicocokkan dengan skema dan Naming Convention, dan tetap informatif.
- Baris naskah utama, judul, Penjelasan, dan Lampiran diperjelas sesuai hasil verifikasi.
- Catatan tentang kode negara, kode bahasa (ISO 639-3 konvensi dan ISO 639-2 Akoma Ntoso sama untuk `ind`), dan akhiran `.akn`.
- Lampiran Referensi menyebut Part 1, skema XML, dan Naming Convention.

## Dampak terhadap Berkas Transkripsi

Tidak ada; Lampiran B informatif.

## Kompatibilitas Versi

PATCH, ditampung di draf 0.1.0.

## Keputusan

2026-10-27, Ananda Putra: laksanakan seluruh usulan penyelarasan dengan acuan.
Rincian diputuskan oleh Claude atas kuasa Ananda.
Diterapkan pada draf 0.1.0 tanpa menaikkan versi.
