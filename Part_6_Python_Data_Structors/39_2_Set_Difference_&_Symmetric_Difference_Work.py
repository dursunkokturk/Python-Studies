# Set lerde Ortak Olan Datalari Alma Islemi
setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

# Intersection Function Ortak Olan Data lari Alma Islemi
print("Symmetric Difference Function Kullanarak")
print("SetA da Olan Ama SetB de Olmayan Ve")
print("Ayni Zamanda Kesisimde Yer Almayan Data lari Alma Islemi")
print(setA.symmetric_difference(setB))
print("Symmetric Difference Function Kullanarak")
print("SetB de Olan Ama SetA de Olmayan Ve")
print("Ayni Zamanda Kesisimde Yer Almayan Data lari Alma Islemi")
print(setB.symmetric_difference(setA))