#TAKE A NUMBER AS INPUT AND PRINT ITS MULTIPLICATION TABLE
num=int(input("enter a number: "))
for i in range(num,num*10+1,num):
    print(i)

#TAKE A NUMBER AS INPUT AND PRINT ITS MULTIPLICATION TABLE IN THE FORMAT: 5×1=5
num=int(input("enter a number: "))
n=1
for i in range(num,num*10+1,num):
    for j in range(n,11):
       print(f"{num}x{j}: {i}")
       n+=1   #i.e. n=n+1
       break
#alternate method:
num=int(input("enter a number: "))
for i in range(1,11):
    print(f"{num}x{i} = {num*i}")