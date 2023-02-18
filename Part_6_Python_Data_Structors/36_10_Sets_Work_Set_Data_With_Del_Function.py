# Set lerde Girilen Data larin Belirli Bir indis Sirasi Yoktur
# Yeni Bir Data Girildiginde Yazdirma Siralamasi Rastgele Olur

# Del Fonksiyonu Ile
# Hem Set i Ve Hem De Icindeki Data larin Hepsini Tek Seferde Silme Islemi Yapiyoruz

studentsSet = {"Engin","Derin","Salih","Ahmet"}
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("Clear Fonksiyonu Ile")
print("Set Icindeki Data larin Hepsini Tek Seferde Silme")
del studentsSet
print(studentsSet)