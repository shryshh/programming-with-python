#PRINT ALL FACTORS OF A NUMBER

n=int(input("enter a number: "))
print("factors of the number: ")
for i in range(1,n+1):
    if n%i==0:
        print(i)

#CHECK IF A NUMBER IS PERFECT (SUM OF PROPER FACTORS = THE NUMBER ITSELF)  (proper factors: the number itself is excluded)
n=int(input("enter a number: "))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
if sum==n:
    print("the number is a perfect number")
else:
    print("the number is not perfect")
