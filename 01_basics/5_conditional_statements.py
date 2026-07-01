#THERE ARE TWO TYPES OF CONTROL FLOW STATEMENTS : CONDITIONAL STATEMENTS AND LOOPS
"""if True : 
    print("hello")   #output: hello
if False:
    print("hello")   #no output

if(22==7 or 3>1):
    print("okay")    #output: okay
if(22==7 and 3>1):
    print("okay")    #no output

#take age as input and tell whether the person can vote or not
age = int(input("Please state your age: "))
if age<18:
    print("you can not vote")
else:
    print("you can vote!") """

#if-elif-else ladder
money=int(input("input money: "))
if money==0:
    print("starvation")
elif money == 50:
    print("food A")
elif money==100:
    print("food B")
else:
    print("don't know what to get")
