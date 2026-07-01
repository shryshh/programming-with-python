#for loop works based on a range, i.e. we know how many times the loop will repeat
#while loop works based on a condition, i.e. we dont know how many times the loop will repeat, we just know that we have to repeat it till the condition is met

#range(start, stop+1, steps) ; default value of start:0, default value of steps:1
#create the following ranges: 10-100, 23-56, 0-45
#range(10,101,1) [or range(10,101)] , range(23,57,1) [or range(23,57)], range(0,45,1) [or range(45)]

#FOR LOOP WITH NUMBERS
for i in range(10,21,1):
    print(i)
for i in range(10,21,2):
    print(i)
for i in range(10,101,10):
    print(i)
for i in range(46):
    print(i)

#PRINT TABLE OF 5
for i in range(5,51,5):
    print(i)


#FOR LOOP WITH STRINGS
a="Students"
#method 1
for i in a:
    print(i)
#method 2 (using index)
for j in range(0,len(a),1):     #length of string a : 8, stopping index : 7
    print(a[j])
#more: 
for k in range(len(a)):
    print(f"{k} : {a[k]}")


#SOME MORE LOOP TERMINOLOGIES: break, continue, else (else works hand-in-hand with break)
for i in range(1,11):
    if i==4:
        continue
    if i==8:
        break
    print(i)    #output: 1,2,3,5,6,7

#the else block runs only if the loop finishes without hitting a break
#example 1: break happens, so else doesn't run
for i in range(5):
    if i==3:
        break
    print(i)
    print("break was encountered")
else:
    print("loop finished, no break was encountered")
#example 2: no break, so else runs
for i in range(5):
    if i==7:
        break
    print(i)
    print("break was encountered")
else:
    print("loop finished, no break was encountered")