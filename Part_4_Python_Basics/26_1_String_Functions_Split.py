info1 = "Dursun Köktürk 36 Zonguldak"
print("Degiskene Atanan Degerler")
print(info1)
print("")

print("Split Fonksiyonu Ile Degiskene Atanan String Tipi Degerler Arasinda Bulunan Bosluklari Baz Alarak")
print("Girilen Degerleri Array Haline Getirme")
newInfo1 = info1.split()
print(newInfo1)

# Strip Fonksiyonunu Kullanarak Array Icinde Ayirma Islemleri Istenilen Karaktere Gore Yapabilir
print("Split Fonksiyonu Ile Degiskene Atanan String Tipi Degerlerin Ilk Kismina Ulasma")
info3 = "Dursun Köktürk 36 Zonguldak"
print(info3)
newInfo3 = info3.split(" ")[0]
print("Name : " + newInfo3)