#Tuple is exactly the same as list except the fact that it's immutable
#Use tuples for data that should stay constant - like days of the week

a=()
print(type(a))   #tuple

#creating a tuple:
#method 1:
t=("monday", "tuesday", 123)
#method 2: converting a list into a tuple
t=["monday", "tuesday", 123]
t=tuple(t)
print(type(t))

print(t[0])  #monday

#t[0]="wednesday"  - error

#Tuple methods:
print(t.index("tuesday"))   # 1
t=("mon", "tue", "tue", 55, 43, 6.5,"tue", True)
print(t.count("tue"))       # 3

"""Tuple packing and unpacking: """
#Tuple packing is when you group multiple values into a tuple:
t = 1, 2, 3   # packing — Python sees this as (1, 2, 3)
#You don't even need parentheses, (though adding them is more common for clarity)
#Tuple unpacking is the reverse — taking a tuple and assigning its values to individual variables:
a, b, c = t   # unpacking — a=1, b=2, c=3
#The number of variables on the left must match the number of elements in the tuple, otherwise Python throws an error.
print(a,b,c)   #1 2 3

#EXAMPLE:
def student():
    return "yash",19,"yash@xyz.com"
info=student()
name,age,email=info
print(name,age,email) 