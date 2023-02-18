print("Cities Listesi")
cities = list(("Ankara","İstanbul","İzmir"))
cities1 = list(("Antalya","Muğla","Mersin"))
cities2 = list(("Adana","Konya","Zonguldak"))
print(cities)

print("")

print("Extend Fonksiyonu Ile Bir List in Devamina Baska Bir List Ekleme")
cities.extend(cities1)

print("")

print("Sort Fonksiyonu Ile Bir List Icindeki Degerleri Siralama")
cities.sort()
print(cities)