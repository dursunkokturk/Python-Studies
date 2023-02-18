# Kullanicinin Olusturdugu Parametreli Fonksiyonun Icinde 
# Kullanici Fonksiyona Parametre Gondermez Ise 
# Parametreye Atanan Deger Ekrana Yazdirilacak 
def hello(name = "Visitor"):
    
    # Fonksiyon Icinde Fonksiyon Cagirildiginda Ekrana Yazdirilacak Yazi Ve
    # Parametre Olarak Girilecek Datayi Yada Parametreye Atanmis Degerin 
    # Ekrana Yazdirma Islemi Yapiliyor
    print("Hello " + name)

# Fonksiyon Parametreye Data Gonderilerek Cagirildiginda 
# Ilk Olarak Fonksiyon Icindeki Yazi Ekrana Yazdirilacak Sonra 
# Fonksiyona Parametre Olarak Girilen Data Ekrana Yazdirilacak
hello("Dursun")

# Fonksiyon Parametreye Data Gonderilmeden Cagirildiginda 
# Ilk Olarak Fonksiyon Icindeki Yazi Ekrana Yazdirilacak Sonra 
# Fonksiyon Icindeki Degiskene Atanan Deger Ekrana Yazdirilacak
hello()