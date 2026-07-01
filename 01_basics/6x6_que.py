#FIND SUM OF FIRST 'n' NATURAL NUMBERS

n=int(input("enter n: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)


#FIND FACTORIAL OF A NUMBER
num=int(input("enter a number: "))
fac=1
for i in range(1,num+1):
    fac=fac*i
print(fac)