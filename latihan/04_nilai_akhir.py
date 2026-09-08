BOBOT_TUGAS = 0.20
BOBOT_UTS = 0.30
BOBOT_UAS = 0.50

nama = "Erlina Putri Febriani"

print(f"=== HITUNG NILAI AKHIR: {nama} ===")

# Kasus 1
tugas1, uts1, uas1 = 80.0, 80.0, 80.0
akhir1 = (tugas1 * BOBOT_TUGAS) + (uts1 * BOBOT_UTS) + (uas1 * BOBOT_UAS)

print("\n[Kasus 1 - Nilai Sama]")
print(f"Tugas: {tugas1}, UTS: {uts1}, UAS: {uas1}")
print(f"Nilai Akhir : {akhir1:.2f}")

# Kasus 2
tugas2, uts2, uas2 = 90.0, 70.0, 80.0
akhir2 = (tugas2 * BOBOT_TUGAS) + (uts2 * BOBOT_UTS) + (uas2 * BOBOT_UAS)

print("\n[Kasus 2 - Nilai Bervariasi]")
print(f"Tugas: {tugas2}, UTS: {uts2}, UAS: {uas2}")
print(f"Nilai Akhir : {akhir2:.2f}")