# Password Generator

Program sederhana untuk membuat password acak yang kuat, dibuat dengan Python. Dibuat untuk belajar dasar keamanan sambil latihan pemrograman.

## Fitur

- Menu terminal berwarna dengan banner
- Auto Generate: sekali pilih langsung dapat password kuat (16 karakter, semua jenis karakter), cocok kalau malas memilih pengaturan
- Buat Password Custom: pilih panjang password (8 sampai 64 karakter)
- Pilih jenis karakter: huruf besar, angka, simbol
- Setiap jenis karakter yang dipilih pasti muncul di hasil
- Menilai kekuatan password (skor 0 sampai 6 dan level Lemah, Sedang, Kuat)
- Bisa membuat password berkali-kali tanpa mengulang pengaturan
- Menu tips membuat password yang aman
- Memakai SystemRandom, sumber acak dari sistem operasi

## Cara Menjalankan

Pastikan Python 3 sudah terpasang, lalu jalankan:

```
python main.py
```

## Contoh Tampilan

```
[ OK ] Password : k7#Vn2@qLz9!
         Skor     : [######] 6 / 6 KUAT
```

## Struktur Project

```
.
├── main.py                # menu utama
├── ui.py                  # tampilan terminal (warna, kotak, banner)
├── password_generator.py  # pembuat password acak
├── .gitignore
└── README.md
```

## Lisensi

Bebas dipakai untuk belajar.