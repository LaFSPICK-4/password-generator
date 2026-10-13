import os

# Trik kecil supaya warna ANSI jalan di terminal Windows
os.system("")

MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
CYAN = "\033[96m"
TEBAL = "\033[1m"
RESET = "\033[0m"

LEBAR = 46


def bersihkan_layar():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def banner():
    print(CYAN + TEBAL)
    print(r" ____                     ____            ")
    print(r"|  _ \ __ _ ___ ___   / ___| ___ _ __  ")
    print(r"| |_) / _` / __/ __| | |  _ / _ \ '_ \ ")
    print(r"|  __/ (_| \__ \__ \ | |_| |  __/ | | |")
    print(r"|_|   \__,_|___/___/  \____|\___|_| |_|")
    print("    P A S S W O R D   G E N E R A T O R")
    print(RESET)


def garis():
    print(CYAN + "+" + "-" * (LEBAR - 2) + "+" + RESET)


def judul(teks):
    garis()
    print(CYAN + "|" + RESET + TEBAL + teks.center(LEBAR - 2) + RESET + CYAN + "|" + RESET)
    garis()


def baris(teks):
    sisa = LEBAR - 4 - len(teks)
    print(CYAN + "|" + RESET + " " + teks + " " * sisa + " " + CYAN + "|" + RESET)


def bar(nilai, maksimal, warna):
    isi = "#" * nilai
    kosong = "-" * (maksimal - nilai)
    return warna + "[" + isi + kosong + "]" + RESET


def sukses(teks):
    print(HIJAU + "[ OK ] " + RESET + teks)


def gagal(teks):
    print(MERAH + "[ XX ] " + RESET + teks)


def info(teks):
    print(KUNING + "[ !! ] " + RESET + teks)


def tunggu():
    print()
    input("Tekan Enter untuk lanjut...")