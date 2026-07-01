#ACCEPT A NUMBER AND PRINT ITS REVERSE

#method 1
n=int(input("enter number: "))
s=""
while n>0:
    s=s+str(n%10)
    n=n//10
print(f"the reverse: {int(s)}")

#method 2
n=int(input("enter number: "))
rev=0
while n>0:
    rev=rev*10+n%10
    n=n//10
print(f"the reverse: {rev}")