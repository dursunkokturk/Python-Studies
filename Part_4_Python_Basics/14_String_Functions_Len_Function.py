message = "Hello World"

print("Degiskene Atanan Degerin Toplam Karakter Sayisi")
print(len(message))
print("")

# len(message)-1 Islemi Ile
# indis Numarasini Kullanarak Yapilan Islemde Degiskene Atanan Degerdeki Toplam Karakter Sayisinsan 1 Cikariyoruz.
# Bu Islem Ile Son Karakterden Bir Onceki Karakterin indis Numaraasina Ulasiyoruz
# Sonra Bu Kisimdan Son indisteki Degere Kadar Olan Tum Degerlerin Karakter Sayisini Yazdiriyoruz.
newMessage = message[len(message)-1:len(message)]
print("Degiskene Atanan Degerin Sonunda Yer Alan Karakter Sayisi")
print(len(newMessage))