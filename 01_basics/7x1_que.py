#SEPARATE EACH DIGIT OF A NUMBER AND PRINT ON A NEW LINE SEPARATELY

#method 1
n=input("enter a number: ")
for i in n:
    print(i)

#method 2 (prints in reverse order)
n=int(input("enter a number: "))
while n>0:
    print(n%10)
    n=n//10


#method 3 (prints in correct order)
n = int(input("Enter a number: "))

# Step 1: count digits
temp = n
count = 0
while temp > 0:
    temp //= 10
    count += 1

# Step 2: extract digits from left to right
divisor = 10 ** (count - 1)   # start with the highest place value
while divisor > 0:
    digit = n // divisor      # get the leftmost digit
    print(digit)
    n = n % divisor           # remove that digit
    divisor //= 10            # move to next place
