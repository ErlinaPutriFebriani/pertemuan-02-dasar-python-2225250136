"""
TUGAS UTAMA: KALKULATOR KOORDINAT DUA TITIK
Mata Kuliah : Algoritma dan Pemrograman
Pertemuan   : 02
Nama        : Erlina Putri Febriani
NIM         : 2225250136
Kelas       : 3B
"""

print("KALKULATOR KOORDINAT DUA TITIK")
print("Mahasiswa: Erlina Putri Febriani (2225250136)\n")

x1 = float(input("x titik A: "))
y1 = float(input("y titik A: "))
x2 = float(input("x titik B: "))
y2 = float(input("y titik B: "))

dx = x2 - x1
dy = y2 - y1

jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

titik_tengah_x = (x1 + x2) / 2
titik_tengah_y = (y1 + y2) / 2

print(f"\nTitik A      : ({x1:.2f}, {y1:.2f})")
print(f"Titik B      : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan    : dx={dx:.2f} dy={dy:.2f}")
print(f"Jarak A ke B : {jarak:.2f}")
print(f"Titik tengah : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")