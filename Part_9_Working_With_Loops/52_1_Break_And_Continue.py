# Array Icinde Aranan Deger Bulunduktan Sonra 
# Aranan Degeri Bulundugu Indis Haric Oncekileri Listeleme

cities = ["Ankara","İstanbul","İzmir"]

for city in cities:
    if city == "İzmir":
        break
    print(city + " Icin Kod = " + city[0:3])