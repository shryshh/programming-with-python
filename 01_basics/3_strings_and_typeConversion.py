#unicode : every character has a unicode code point
#character : single textual symbol
a='x'
b='X'
c='3'
d='#'
e=' '
f='0'
g='😊'
print(ord(a))
print(ord(b))
print(ord(c))
print(ord(d))
print(ord(e))
print(ord(f))
print(ord(g))
#unicode code point of x = 120
print(chr(120))
print(chr(128522))

"""indexing"""
name='hElLo'
#positive indexing
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
#negative indexing
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])

print(name[0],name[-5])

"""string slicing"""
name2='COLLEGE'
print(name2[3:6:1])   #slicing out LEG 
print(name2[0:7:2])   #slicing out CLEE
print(name2[::2])     #slicing out CLEE  (by default starts from the very start goes till the end)
print(name2[::])      #COLLEGE  (by default starts from the very start goes till the end and takes one step at a time by default as well)

"""type conversion"""
#integer conversion : we can convert a string to int if the string contains an integer; we can convert a float to int
a='5'
print(type(a))
print(a)
a=int(a)     #conversion to integer data type
print(type(a))
print(a)

a=2.7
print(type(a))
print(a)
a=int(a)     #conversion to integer data type
print(type(a))
print(a)

a=3.5
print(type(a))
print(a)
a=int(a)     #conversion to integer data type
print(type(a))
print(a)

#float conversion
a="12.4"
print(type(a))
print(a)
a=float(a)
print(type(a))
print(a)

a="12"
a=float(a)
print(a)    #output:12.0

a=-3
a=float(a)
print(a)

#string conversion
a=153
b=23.2
c=4-5j
d=True
print(type(str(a)))
print(type(str(b)))
print(type(str(c)))
print(type(str(d)))
print(str(a))
print(str(b))
print(str(c))
print(str(d))

#boolean conversion : except 7 falsey values, everything else is true wrt boolean
a=12
b=0
c=-12.4
d=0.0
e=5+2j
f=0.00
g=""
h=" "
i=False
j="hello"
k=0.0003
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
print(bool(g))
print(bool(h))
print(bool(i))
print(bool(j))
print(bool(k))

#implicit conversion
a=12
print(a/2)    #implicit conversion to float
b=a/2         #implicit conversion to float
print(b)