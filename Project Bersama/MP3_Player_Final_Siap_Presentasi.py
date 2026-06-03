import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.json")

print("Database:", DATABASE)
print("Lokasi program:", os.getcwd())
print("File ditemukan?", os.path.exists(DATABASE))

playlist = []
favorit = []
riwayat = []  # Stack
play_count = {}

def load_data():
    global playlist, favorit, riwayat, play_count
    if os.path.exists(DATABASE):
        with open(DATABASE, "r", encoding="utf-8") as f:
            data = json.load(f)
            playlist = data.get("playlist", [])
            favorit = data.get("favorit", [])
            riwayat = data.get("riwayat", [])
            play_count = data.get("play_count", {})

def save_data():
    with open(DATABASE, "w", encoding="utf-8") as f:
        json.dump({
            "playlist": playlist,
            "favorit": favorit,
            "riwayat": riwayat,
            "play_count": play_count
        }, f, indent=4, ensure_ascii=False)

def lihat_playlist():
    if not playlist:
        print("Playlist kosong!")
        return
    for i, lagu in enumerate(playlist, 1):
        print(f"{i}. {lagu}")

def tambah_lagu():
    judul = input("Judul lagu: ").strip()
    if judul:
        playlist.append(judul)
        save_data()

def ubah_lagu():
    lihat_playlist()
    try:
        n = int(input("Nomor lagu: "))
        if 1 <= n <= len(playlist):
            playlist[n-1] = input("Judul baru: ")
            save_data()
    except ValueError:
        print("Input harus angka!")

def hapus_lagu():
    lihat_playlist()
    try:
        n = int(input("Nomor lagu: "))
        if 1 <= n <= len(playlist):
            playlist.pop(n-1)
            save_data()
    except ValueError:
        print("Input harus angka!")

def cari_lagu():
    key = input("Kata kunci: ").lower()
    hasil = [x for x in playlist if key in x.lower()]
    if hasil:
        for lagu in hasil:
            print("-", lagu)
    else:
        print("Tidak ditemukan.")

def sort_az():
    playlist.sort()
    save_data()

def sort_za():
    playlist.sort(reverse=True)
    save_data()

def tambah_favorit():
    lihat_playlist()
    try:
        n = int(input("Nomor lagu: "))
        lagu = playlist[n-1]
        if lagu not in favorit:
            favorit.append(lagu)
            save_data()
    except:
        print("Input tidak valid")

def lihat_favorit():
    for i, lagu in enumerate(favorit, 1):
        print(f"{i}. {lagu}")

def putar_lagu():
    lihat_playlist()
    try:
        n = int(input("Pilih lagu: "))
        lagu = playlist[n-1]

        riwayat.append(lagu)
        play_count[lagu] = play_count.get(lagu, 0) + 1

        save_data()
        print(f"Sedang memutar: {lagu}")
    except:
        print("Input tidak valid")

def lihat_riwayat():
    if not riwayat:
        print("Belum ada riwayat.")
        return
    for lagu in reversed(riwayat):
        print("-", lagu)

def statistik():
    if not play_count:
        print("Belum ada statistik.")
        return

    data = sorted(play_count.items(), key=lambda x: x[1], reverse=True)
    for lagu, jumlah in data:
        print(f"{lagu} ({jumlah}x)")

load_data()


while True:
    print("""
===== MP3 PLAYER =====
1. Lihat Playlist
2. Tambah Lagu
3. Ubah Lagu
4. Hapus Lagu
5. Putar Lagu
6. Cari Lagu
7. Urutkan A-Z
8. Urutkan Z-A
9. Tambah Favorit
10. Lihat Favorit
11. Lihat Riwayat
12. Statistik Lagu
0. Keluar
======================
""")

    menu = input("Pilih menu: ")

    if menu == "1":
        lihat_playlist()
    elif menu == "2":
        tambah_lagu()
    elif menu == "3":
        ubah_lagu()
    elif menu == "4":
        hapus_lagu()
    elif menu == "5":
        putar_lagu()
    elif menu == "6":
        cari_lagu()
    elif menu == "7":
        sort_az()
    elif menu == "8":
        sort_za()
    elif menu == "9":
        tambah_favorit()
    elif menu == "10":
        lihat_favorit()
    elif menu == "11":
        lihat_riwayat()
    elif menu == "12":
        statistik()
    elif menu == "0":
        break
    else:
        print("Menu tidak valid")
