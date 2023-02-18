# Set lerde Girilen Data larin Belirli Bir indis Sirasi Yoktur
# Yeni Bir Data Girildiginde Yazdirma Siralamasi Rastgele Olur

# Del Fonksiyonu Ile
# Hem Set i Ve Hem De Icindeki Data larin Hepsini Tek Seferde Silme Islemi Yapiyoruz

studentsSet = set("Engin","Derin","Salih","Ahmet")
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("Set Fonksiyonu Ile")
print("Set Olusturma Ve Degisken Uzerinden Set e Ulasma")
print(studentsSet)