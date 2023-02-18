# Set lerde Girilen Data larin Belirli Bir indis Sirasi Yoktur
# Yeni Bir Data Girildiginde Yazdirma Siralamasi Rastgele Olur

# Pop Fonksiyonu Ile
# Set Icindeki Data lari Silme Isleminde Silinecek Hata Bulunamazsa
# Bu Hatanin Gorunmesini Engelleme

studentsSet = {"Engin","Derin","Salih","Ahmet"}
print(studentsSet)

for student in studentsSet:
    print(student)
    
print("Pop Fonksiyonu Ile")
print("Set Icindeki Data larin En Sonundaki Data yi Silme")
studentsSet.pop()
print(studentsSet)