#CHECK IF A NUMBER IS PALINDROME (EQUAL TO ITS REVERSE)
n=int(input("enter number: "))
temp=n
rev=0
while temp>0:
    rev=rev*10+temp%10
    temp=temp//10
if rev==n:
    print("the number is palindrome")
else:
    print("the number is not palindrome")