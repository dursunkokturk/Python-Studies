tupleList = (2,4,6,"Ankara",(1,3,5))
list = [2,4,6,"Ankara",(1,3,5)]

print("Tuple List")
print(tupleList)
print("Tuple List Data Type")
print(type(tupleList))
print("Tuple List Updated")
print("List Icindeki Degerler Degistirilebilir Ama")
print("Tuple List Icindeki Degerler Sonradan Degistirilemez")
tupleList[0] = 6
print(tupleList)
print("")


print("List")
print(list)
print("List Data Type")
print(type(list))