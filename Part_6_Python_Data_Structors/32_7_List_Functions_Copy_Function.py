print("Cities Listesi")
cities = list(("Ankara","İstanbul","İzmir"))
print(cities)

print("")

print("Copy Function Ile Listin Orjinal Halinin Kopyasini Alip Gerektiginde Goruntuleme")
citiesCopy = cities.copy()


print("")

print("List Icindeki 0 Nolu indiste Yer Alan Degerin Guncel Hali")
cities[0] = "Antalya"
print(cities)

print("")

print("Cities Listesinin Kopyasi")
print(citiesCopy)