number = int(input("Sayi Giriniz = "))

isPrime = True

for x in range(2,number):
    if (number % x) == 0:
        isPrime = False
        break
    
if isPrime == "Yes":
    print("Bu Sayi Asaldir")
else:
    print("Bu Sayi Asal Degildir")