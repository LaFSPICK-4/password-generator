import random
import ui

HURUF_KECIL = "abcdefghijklmnopqrstuvwxyz"
HURUF_BESAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ANGKA = "0123456789"
SIMBOL = "!@#$%^&*()-_=+"

# Panjang password untuk menu Auto Generate
PANJANG_AUTO = 16

# SystemRandom memakai sumber acak dari sistem operasi,
# lebih aman dibanding random biasa untuk membuat password
acak = random.SystemRandom()


def buat_password(panjang, pakai_besar, pakai_angka, pakai_simbol):
    """Buat password acak. Tiap jenis karakter yang dipilih pasti muncul."""
    kumpulan = HURUF_KECIL
    password = [acak.choice(HURUF_KECIL)]

    if pakai_besar:
        kumpulan += HURUF_BESAR
        password.append(acak.choice(HURUF_BESAR))

    if pakai_angka:
        kumpulan += ANGKA
        password.append(acak.choice(ANGKA))

    if pakai_simbol:
        kumpulan += SIMBOL
        password.append(acak.choice(SIMBOL))

    while len(password) < panjang:
        password.append(acak.choice(kumpulan))

    acak.shuffle(password)
    return "".join(password)


def hitung_skor(password):
    """Hitung skor kekuatan password (0-6)."""
    ada_besar = False
    ada_kecil = False
    ada_angka = False
    ada_simbol = False

    for karakter in password:
        if karakter.isupper():
            ada_besar = True
        elif karakter.islower():
            ada_kecil = True
        elif karakter.isdigit():
            ada_angka = True
        else:
            ada_simbol = True

    skor = 0
    if len(password) >= 8:
        skor += 1
    if len(password) >= 12:
        skor += 1
    if ada_besar:
        skor += 1
    if ada_kecil:
        skor += 1
    if ada_angka:
        skor += 1
    if ada_simbol:
        skor += 1

    return skor


def level_skor(skor):
    """Ubah skor jadi level dan warna."""
    if skor <= 2:
        return "LEMAH", ui.MERAH
    elif skor <= 4:
        return "SEDANG", ui.KUNING
    else:
        return "KUAT", ui.HIJAU


def tanya_ya_tidak(pertanyaan):
    jawaban = input(pertanyaan + " (y/n): ")
    return jawaban.lower() == "y"


def jalankan():
    ui.bersihkan_layar()
    ui.judul("BUAT PASSWORD BARU")
    print()

    try:
        panjang = int(input("Masukan Panjang Password (8-64): "))
    except ValueError:
        ui.gagal("Panjang harus berupa angka.")
        ui.tunggu()
        return

    if panjang < 8 or panjang > 64:
        ui.gagal("Panjang harus antara 8 sampai 64.")
        ui.tunggu()
        return

    pakai_besar = tanya_ya_tidak("Pakai huruf besar?")
    pakai_angka = tanya_ya_tidak("Pakai angka?")
    pakai_simbol = tanya_ya_tidak("Pakai simbol?")

    while True:
        password = buat_password(panjang, pakai_besar, pakai_angka, pakai_simbol)
        skor = hitung_skor(password)
        level, warna = level_skor(skor)

        print()
        ui.sukses("Password : " + ui.TEBAL + password + ui.RESET)
        print("         Skor     :", ui.bar(skor, 6, warna), skor, "/ 6", warna + level + ui.RESET)
        print()

        if not tanya_ya_tidak("Buat lagi?"):
            break

    ui.tunggu()


def auto_generate():
    """Buat password kuat otomatis tanpa perlu memilih apa-apa."""
    ui.bersihkan_layar()
    ui.judul("AUTO GENERATE")
    print()
    ui.info("Otomatis: 16 karakter, huruf besar, angka, dan simbol.")

    while True:
        password = buat_password(PANJANG_AUTO, True, True, True)
        skor = hitung_skor(password)
        level, warna = level_skor(skor)

        print()
        ui.sukses("Password : " + ui.TEBAL + password + ui.RESET)
        print("         Skor     :", ui.bar(skor, 6, warna), skor, "/ 6", warna + level + ui.RESET)
        print()

        pilihan = input("Enter = buat lagi, 0 = kembali: ")
        if pilihan == "0":
            break


if __name__ == "__main__":
    jalankan()