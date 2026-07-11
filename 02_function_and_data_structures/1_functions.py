#A function is a named, reusable block of code

#defining/creating a function
def hello():    #function name: hello
    print("hello, how are you?")
    print("hope you're doing good")
#calling the function
hello()

#parameters and arguments
def addition(a,b):    #a,b: parameters
    print(a+b)
addition(5,10)        #5,10: arguments for the parameters
addition(20,13)

#palindrome number checker
def palindrome_check(n):
    rev=0
    save=n
    while n>0:
        rev=rev*10+n%10
        n=n//10
    if rev==save:
        print("palindrome number")
    else:
        print("not a palindrome number")
num=int(input("enter a number: "))
palindrome_check(num)

#types of arguments
#1) positional - order matters
def multiply(a,b,c,d):
    print(a*b*c*d)
multiply(5,2,4,3)   #a=5, b=2, c=4, d=3
#2) default - works even without passing a value
def subtraction(a,b,c=5):   #a default value of 5 is assigned to c, so no error occurs even if we don't pass a value to c
    print(a-b-c)
subtraction(10,2)
subtraction(10,2,3)

"""note: after assigning a default value to a parameter, you'll have to 
assign a default value to every parameter which comes after it. If you don't want to assign a default value
to a parameter, you'll have to define it before
example: def addition(a,b,c=5,d) - shows error
def addition(a,b,d,c=5) - this is correct
def addition(a,b,c=5,d=3) - this is also correct"""

def arithmetic(a,b,d,c=8):
    print(a+b-c*d)
arithmetic(7,5,7)   #a=7, b=5, d=7, c=8
arithmetic(2,4,4,4) #a=2, b=4, d=4, c=4

#keyword - can pass value in any order
def exponent(a,b):
    print(a**b)
exponent(b=5,a=3)  #if we had just wrote exponent(5,3), a would have gotten 5 and b would have gotten 3 because of the order of the parameter
#note: exponent(b=5,3) - shows error
def power(a,b,c):
    print(a**b**c)
power(2,c=4,b=2) 

#There are two kinds of functions:
#1)Returns a value — you use return to send something back to the caller:
def add(a, b):
    return a + b
result = add(3, 4)  # result = 7
print(result)

#2)Returns nothing — it just does something (like printing) and ends:
def greet(name):
    print(f"Hello, {name}")  # no return statement
greet("Alex")  # just prints, nothing comes back

#another example: 
def hi():
    return "how are you"
print(hi())