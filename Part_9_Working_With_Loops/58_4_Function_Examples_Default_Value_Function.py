# Kullanicinin Olusturdugu Parametreli Fonksiyonun Icinde 
# Kullanici Fonksiyona Hic Bir Sekilde Parametre Gondermez Ise 
# Parametreye Atanan Deger Yada Degerler Ekrana Yazdirilacak 
def hello(name = "Visitor" , surname = " Friend"):
    
    # Fonksiyon Icinde 
    # Fonksiyon Cagirildiginda Ekrana Yazdirilacak Yazi Ve
    # Parametre Olarak Girilecek Datayi Yada Data lar Yazdirilacak
    # Parametre Yada Parametrelere Atanmis Degerin Yok Ise 
    # Fonksiyonda Degiskenlere Atanan Degerler
    # Ekrana Yazdirma Islemi Yapiliyor
    print("Hello " + name + surname)

# Fonksiyon Parametre Gonderilmeden Cagirilirsa
# Fonksiyon Icindeki Degiskenlere Atanan Degerler Ekrana Yazdirilacak
hello()

# Fonksiyonda 1 Tane Parametreye Data Gonderilerek Cagirildiginda 
# Ilk Olarak Fonksiyon Icindeki Yazi Ekrana Yazdirilacak Sonra 
# Fonksiyona Parametre Olarak Girilen Data Ekrana Yazdirilacak
# Birden Fazla Parametre Var Ise Deger Gonderilmeyen Parametrelerin
# Fonksiyon Icindeki Atanan Degerleri Ekrana Yazilacak
hello("Dursun")

# Fonksiyonda 2 Parametreye Data Gonderilerek Cagirildiginda 
# Ilk Olarak Fonksiyon Icindeki Yazi Ekrana Yazdirilacak Sonra 
# Fonksiyona Parametre Olarak Girilen Data lar Ekrana Yazdirilacak
hello("Dursun"," Köktürk")