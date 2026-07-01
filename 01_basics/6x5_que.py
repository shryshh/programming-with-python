#PRINT 'n' DOWN TO 1

n=int(input("enter n: "))
for i in range(n,0,-1):      #when counting down: range(start, stop-1, step); step will be negative
    print(i)

##PRINT 'n' DOWN TO 0
n=int(input("enter n: "))
for i in range(n,-1,-1):      
    print(i)