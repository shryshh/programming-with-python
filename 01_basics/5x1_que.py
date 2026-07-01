#ACCEPT TWO NUMBERS AND PRINT THE GREATEST BETWEEN THEM
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
if a>b:
    print(a,"is the bigger number")
elif a<b:
    print(b,"is the bigger number")
else:
    print("both numbers are equal")