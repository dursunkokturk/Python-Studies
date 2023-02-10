print("Cities Listesi")
cities = list(("Ankara","İstanbul","İzmir"))
print(cities)

print("")

print("Reverse Function Ile List Icindeki Degerleri indis Numarasina Gore Sondan Basa Dogru Ters Cevirerek Yazdirma")
cityIndisNumber = cities.reverse()
print(cities)

print("")

print("List Icindeki 0 Nolu indiste Yer Alan Degerin Guncel Hali")
cities[0] = "Antalya"
print(cities)