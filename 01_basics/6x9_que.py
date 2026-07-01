#CHECK IF A NUMBER IS PRIME

n=int(input("enter the number: "))
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum=sum+i
if sum==n+1:
    print("the number is prime")
else:
    print("the number is not prime")

#another way:
n=int(input("enter the number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("the number is prime")
else:
    print("the number is not prime")
