# Set lerde Girilen Data larin Belirli Bir indis Sirasi Yoktur
# Yeni Bir Data Girildiginde Yazdirma Siralamasi Rastgele Olur
# Set Icinde Aranan Deger Bulundugunda True Bulunmadiginda False Degeri Gorunur
studentsSet = {"Engin","Derin","Salih","Ahmet"}
print(studentsSet)

for student in studentsSet:
    print(student)
print("Set Icinde In Keyword Ile Aranan Deger Bulundugunda True Bulunmadiginda False Degeri Gorunur")
print("Derin" in studentsSet)