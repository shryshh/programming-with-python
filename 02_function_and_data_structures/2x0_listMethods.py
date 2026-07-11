"""A method is a function that is "attached" to a specific type of object.
In Python, everything is an object (a list, a string, an integer, etc.)
While a regular function can be called on its own, 
a method is specifically designed to work with, or manipulate, 
the data inside a particular object."""

print(dir(list))   #all the methods of a list

#1)Adding new element to a list
a=[10,20,30,40,50]
#method 1:
a.append(60)   #adds to the end 
print(a)
a.append("hello")
print(a)

#method 2:
a.insert(0,0)  #adds to any desired position
print(a)
a.insert(2,"hmm")
print(a)

#2)Removing element from a list
b=[10,20,30,45,40,50]
#method 1:
b.pop(3)   #pop by default deletes the last element if we don't specify the index
print(b)

b.insert(3,45)

r=b.pop(3) #pop returns the deleted element as well
print(r)

#method 2:
b=[10,20,30,45,40,50,45]
b.remove(45)  #removes the first occurance only
print(b)

#note:
b=[10,20,30,45,40,50]
b.clear()  #empties the list completely
print(b)

#3)Sorting a list
c=[29,45,67,12,90,34]
c.sort()   #ascending order
print(c)
c.sort(reverse=True)  #descending order
print(c)

#4)Reversing a list
d=[34,65,56,32,45]
d.reverse()
print(d)