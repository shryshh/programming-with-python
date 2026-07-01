"""using a variable inside a string"""
name='yash'
age='19'
print(f'hello my name is {name} and I am {age} years old')  #formatted string
#another way:
print("hello my name is",name,"and I am",age,"years old")   #spaces is automatically applied


"""taking input from user"""
age=int(input("please state your age:- "))    #input() always returns a 'string'
print(f"okay, so your age is {age}")


""" Arithmetic Operators (+,-,*,**,/,//,%) """
a=10
print(a+20)
print(a-20)
print(a/5)       #float
print(int(a/5))  #int
#another way to get int : //
print(a//5)      #int
print(a/4)       #float
print(a//4)      #int
print(a*5)
print(a**5)      #exponent
print(a%4)       #remainder
""" Priority order:
() - brackets
** - exponent (works right to left: 2**2**3 = 2**(2**3))
*,/,//,% (works left to right)
+,- (works left to right)
"""
print(10/2*5)    #25.0
print(10//2*5)   #25
print(10*2/5)    #4.0
print(10*2//5)   #4
print(3+4*2)     #11
print(15//4+15%4)  #6
print(3+2**2*5-1)  #22

"""COMPARISION OPERATORS: boolean results"""
# ==, >, <, >=, <=, !=
print(12==12)  #true
print(14==12)  #false
print(12>45)
print(12<45)
print(12>=12)
print(45<=55)
print(23!=23)
a=5
b=65
print(a<b)

"""LOGICAL OPERATORS"""
# and, or, not
print(12>10 and 34==34 and 3<=2)  #returns false if even any one comaprison is false
print(12>100 or 34==4 or 3<=3)    #returns true if even any one comparison is true
print(not 12==12)  #returns the opposite

print((5>3 and 10==10) or (4!=4 and 2<1))   #true or false = true
print((10==10 and 23!=23) or (34==12 and bool("hello")))  #false or false = false
print(not(5==5 and 3!=4) or (10>20))   #false or false = false

"""ASSIGNMENT OPERATORS"""
# +=, -=, *=, **=, /=, //=, %=
a=10
a+=10
a+=10  #implies a=a+10
print(a) #30

"""COMPARISON OPERATORS ON STRINGS"""
print("hello">"Hello")   #true
#reason: unicode of 'h' > unicode of 'H'
print("hello"=="hello")  #true
print("hello">"hELlo")   