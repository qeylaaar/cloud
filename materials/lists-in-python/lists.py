# akses item dari daftar menurut index
planets = ["Merkurius", "Venus", "Bumi", "Mars", "Jupiter", "Saturnus", "Uranus", "Neptunus"]

print("Planet pertama adalah", planets[0])
print("Planet kedua adalah", planets[1])
print("Planet ketiga adalah", planets[2])

# hasil =
# planet pertama adalah Merkurius
# planets kedua adalah Venus
# planet ketiga adalah Bumi

# mengubah nilai dalam daftar index
planets[3] = "Planet Merah"
print("Mars adalah planet ke-4 dari matahari, tapi sekarang kita tahu bahwa mars juga sering disebut", planets[3])

# hasil = Mars adalah planet ke-4 dari matahari, tapi sekarang kita tahu bahwa mars juga sering disebut Planet Merah

# menentukan panjang daftar
jumlah_planet = len(planets)
print("Sistem tata surya kita memiliki ", jumlah_planet, " planet.")

# hasil = Sistem tata surya kita memiliki 8 planet.

# menambahkan item ke daftar
planets.append("Pluto")
jumlah_planet = len(planets)
print("Sebenarnya, Sistem tata surya kita memiliki ", jumlah_planet , " planet.")

# hasil = Sistem tata surya kita memiliki 9 planet.

# menghapus item dari daftar
planets.pop()
jumlah_planet = len(planets)
print("Tapi Pluto tidak lagi dianggap sebagai planet, jadi sekarang kita hanya memiliki ", jumlah_planet, " planet.")

# hasil = Tapi Pluto tidak lagi dianggap sebagai planet, jadi sekarang kita hanya memiliki 8 planet.

# menggunakan indeks negatif untuk mengakses item dari daftar
print("Planet terakhir adalah", planets[7])

# hasil = Planet terakhir adalah Neptunus

print("Planet terakhir adalah", planets[-1])
print("The penultimate planet is", planets[-2])

# Output
# Planet terakhir adalah Neptunus
# The penultimate planet is Uranus

# menemukan item dalam daftar
jupiter_index = planets.index("Jupiter")
print("Jupiter adalah planet ke ", jupiter_index + 1, " dari matahari")

# Output
# Jupiter adalah planet ke 5 dari matahari
