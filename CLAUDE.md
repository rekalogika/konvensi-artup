@AGENTS.md

## Catatan khusus Claude Code

- Gunakan skill di `.claude/skills/` untuk setiap alur kerja: `usulan-revisi`, `revisi-konvensi`, `tinjau-konsistensi`, `gaya-penulisan-konvensi`, `rilis-konvensi`.
- Setelah menyunting `konvensi/konvensi-artup.md`, selalu jalankan `.venv/bin/python alat/periksa_konvensi.py` dan laporkan hasilnya.
- Setelah mengubah `alat/periksa_konvensi.py`, jalankan uji pemeriksa.
- Jangan commit langsung di `main`; buat branch menurut tabel awalan di AGENTS.md sebelum perubahan pertama.
- Pull request dibuka dengan `gh pr create --base main`; jangan me-merge sendiri.
- Tanyakan dulu sebelum langkah yang tidak dapat dibatalkan: rilis, tag git, `push`, atau menghapus berkas.
