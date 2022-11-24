input_planet_pertama = input("Masukkan jarak planet pertama: ")
input_planet_kedua = input("Masukkan jarak planet kedua: ")

planet_pertama = int(input_planet_pertama)
planet_kedua = int(input_planet_kedua)

jarak_km = planet_pertama - planet_kedua
print(abs(jarak_km))
