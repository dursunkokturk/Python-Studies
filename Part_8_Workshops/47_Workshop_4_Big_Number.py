number1 = int(input("Enter Number 1"))
number2 = int(input("Enter Number 2"))
number3 = int(input("Enter Number 3"))

if (number1 >= number2) and (number1 > number3):
    moreBigNumber = number1
elif (number2 >= number1) and (number2 > number3):
    moreBigNumber = number2
else:
    moreBigNumber = number3
print("More Big Number : "+moreBigNumber)