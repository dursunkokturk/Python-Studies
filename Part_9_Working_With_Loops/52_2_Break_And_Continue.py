# "Array Icinde Aranan Degere Kadar Olan Degerleri Ve 
# Aranan Degerden Sonraki Degerleri 
# Aranan Deger Haric Tutularak Listeleme"

cities = ["Ankara","İstanbul","İzmir"]

for city in cities:
    if city == "İstanbul":
        continue
    print(city + " Icin Kod = " + city[0:3])