# Usulan 0007: Istilah yang Belum Didefinisikan dan Istilah Bermakna Ganda

| Identitas | Nilai |
|---|---|
| Nomor | 0007 |
| Pengusul | Claude (Anthropic), tinjauan konsistensi pertama |
| Tanggal | 2026-10-26 |
| Status | diajukan |
| Versi konvensi acuan | 0.1.0 |
| Aturan terdampak | Bagian 2.2; isian `ekspresi.bagian` |
| Jenis perubahan | redaksional; perubahan tidak kompatibel bila `ekspresi.bagian` diganti nama |
| Usulan versi berikutnya | PATCH, atau MINOR bila isian diganti nama |

## Latar Belakang

### A. Istilah yang dipakai dengan arti khusus tetapi tidak ada di Bagian 2.2

| Istilah | Dipakai di |
|---|---|
| batang tubuh | [C-1] butir 8, `ekspresi.bagian` |
| pembukaan, penutup, konsiderans, dasar hukum, diktum | Bagian 5.1, 6.3, 6.6 |
| teks asli, teks konsolidasi | Bagian 1.2 (didefinisikan di dalam kalimat), `ekspresi.jenis_teks`, [I-6] |
| peraturan perubahan | Bagian 6.8 |
| berkas pendamping | Bagian 8.3, [I-7], `berkas_pendamping` |
| entri verifikasi | Bagian 9.4, [V-1] |
| ketik ganda | [V-2] (didefinisikan di dalam kalimat), `transkripsi.metode` |
| pengenal teknis | [R-5] |
| daftar rilis konvensi | [R-3] |
| sidik jari | Bagian 10.4 |

Istilah dari teknik penyusunan peraturan cukup didefinisikan dengan merujuk Lampiran II UU 12/2011.

### B. Contoh pada definisi "Label"

Contoh `"huruf a."` tidak tertulis demikian di naskah.
Label rincian di batang tubuh adalah `a.`, sedangkan label di penjelasan pasal demi pasal adalah `Huruf a` ([S-15]).

### C. Homonim

- **Bagian** memiliki tiga arti: (1) unsur struktur peraturan ("Bagian Kesatu", [S-1] "apabila BAB tidak memiliki Bagian"); (2) bagian dokumen konvensi ("Bagian 6.5"); dan (3) komponen naskah dalam isian `ekspresi.bagian` (`batang-tubuh`, `penjelasan`, `lampiran`).
- **Paragraf** memiliki dua arti: (1) unsur struktur peraturan ("Paragraf 1"); dan (2) paragraf Markdown ([S-8], [S-9], "paragraf tersendiri").

## Rumusan Baru

1. Tambahkan istilah butir A ke tabel Bagian 2.2.
2. Ganti contoh Label: `misalnya "Pasal 5", "(2)", "a.", "Huruf a"`.
3. Tambahkan catatan di Bagian 2.2:

```markdown
Catatan: "Bagian" dan "Paragraf" berhuruf awal kapital yang diikuti bilangan tingkat (misalnya "Bagian Kesatu", "Paragraf 1") merujuk unsur struktur peraturan.
"Bagian" yang diikuti nomor angka (misalnya "Bagian 6.5") merujuk bagian dokumen ini.
"paragraf" berhuruf kecil merujuk paragraf Markdown.
```

4. Ganti nama isian `ekspresi.bagian` menjadi `ekspresi.komponen`, dengan istilah "komponen naskah" di Bagian 2.2: batang tubuh, penjelasan, atau lampiran.

## Dampak terhadap Berkas Transkripsi

Butir 1–3: tidak ada.
Butir 4: setiap berkas transkripsi yang ada harus mengganti nama isian; [M-6] (usulan 0005) membuat isian lama tidak sah.

## Kompatibilitas Versi

PATCH untuk butir 1–3; MINOR (tidak kompatibel, MAYOR masih 0) untuk butir 4.

## Alternatif yang Dipertimbangkan

Butir 4 dapat ditunda bila jumlah berkas transkripsi yang sudah ada besar; catatan butir 3 sudah menghilangkan sebagian besar keraguan.

## Keputusan
