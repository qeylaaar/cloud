gravitasi_bumi = 1.0
gravitasi_bulan = 0.166
gravitasi_planet = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]

berat_bus = 12650 # dalam kilogram, di bumi

print("Berat bus di bumi adalah", berat_bus, "kg")
print("Berat bus di planet merkurius adalah", berat_bus * gravitasi_planet[0], "kg")

# Output
# Berat bus di bumi adalah 12650 kg
# Berat bus di planet merkurius adalah 4787.3 kg

# menggunakan min dan max untuk mencari nilai terkecil dan terbesar dalam daftar
berat_bus = 12650 # in kilograms, on Earth

print("Berat bus di bumi adalah", berat_bus, "kg")
print("Berat bus terkecil di sistem tata surya kita adalah", berat_bus * min(berat_bus), "kg")
print("Berat bus terbesar di sistem tata surya kita adalah", berat_bus * max(berat_bus), "kg")

# Output
# Berat bus di bumi adalah 12650 kg
# Berat bus terkecil di sistem tata surya kita adalah 4769.05 kg
# Berat bus terbesar di sistem tata surya kita adalah 29854 kg
