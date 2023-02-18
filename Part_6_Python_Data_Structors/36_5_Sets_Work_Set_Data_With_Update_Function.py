# Set lerde Girilen Data larin Belirli Bir indis Sirasi Yoktur
# Yeni Bir Data Girildiginde Yazdirma Siralamasi Rastgele Olur
studentsSet = {"Engin","Derin","Salih","Ahmet"}
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("Update Fonksiyonu Ile Set Icindeki Data lari Guncelleme")
studentsSet.update(["Ali","Mehmet"])
print(studentsSet)