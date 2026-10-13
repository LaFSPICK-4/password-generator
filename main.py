import ui
import password_generator


def tampilkan_tips():
    ui.bersihkan_layar()
    ui.judul("TIPS PASSWORD AMAN")
    print()
    ui.info("Pakai minimal 12 karakter.")
    ui.info("Campur huruf besar, huruf kecil, angka, dan simbol.")
    ui.info("Jangan pakai nama, tanggal lahir, atau kata umum.")
    ui.info("Pakai password berbeda untuk tiap akun.")
    ui.info("Simpan di password manager, jangan di catatan biasa.")
    ui.tunggu()


def menu():
    while True:
        ui.bersihkan_layar()
        ui.banner()
        ui.garis()
        ui.baris("[1] Auto Generate (Cepat)")
        ui.baris("[2] Buat Password Custom")
        ui.baris("[3] Tips Password Aman")
        ui.baris("[0] Keluar")
        ui.garis()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            password_generator.auto_generate()
        elif pilihan == "2":
            password_generator.jalankan()
        elif pilihan == "3":
            tampilkan_tips()
        elif pilihan == "0":
            print()
            ui.sukses("Sampai jumpa!")
            break
        else:
            ui.gagal("Pilihan tidak valid.")
            ui.tunggu()


if __name__ == "__main__":
    menu()