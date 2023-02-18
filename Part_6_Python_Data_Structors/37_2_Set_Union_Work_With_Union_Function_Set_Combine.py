# Set lerde Girilen Data larin Belirli Bir indis Sirasi Yoktur
# Yeni Bir Data Girildiginde Yazdirma Siralamasi Rastgele Olur

# Ortak Olan Datalari Tekrarlamadan 2 Farkli Set i Birlestirme Islemi
setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

# Ortak Olan Datalari Tekrarlamadan A Set i Ile B Set ini Birlestirme Islemi
print(setA.union(setB))

# Ortak Olan Datalari Tekrarlamadan B Set i Ile A Set ini Birlestirme Islemi
print(setB.union(setA))