KELVIN_OFFSET = 273.15

print("=== KONVERSI SUHU CELSIUS ===")

# Kasus 1
c1 = 0.0
f1 = (9 / 5) * c1 + 32
k1 = c1 + KELVIN_OFFSET

print("\n[Kasus 1]")
print(f"Suhu Celsius : {c1} °C")
print(f"Fahrenheit   : {f1:.2f} °F")
print(f"Kelvin       : {k1:.2f} K")

# Kasus 2
c2 = 100.0
f2 = (9 / 5) * c2 + 32
k2 = c2 + KELVIN_OFFSET

print("\n[Kasus 2]")
print(f"Suhu Celsius : {c2} °C")
print(f"Fahrenheit   : {f2:.2f} °F")
print(f"Kelvin       : {k2:.2f} K")