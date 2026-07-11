"""DATA STRUCTURES: when we need to store multiple values in one variable,
we use a data structure.
Python gives us four data structures ready for use: list, tuple, set, dictionary"""

#LIST

#creating a list
a=[23,45,63,2,100]
print(a)
print(type(a))

#a list has an ordered nature - it works on the same indexing principle as a string
#we can access any element of a list at any point of time
print(a[0])
print(a[-1])
print(a[-5])

#a list is mutable - we can change any single or multiple elements inside a list
# a string is immutable, e.g.: s="hellq"; s[-1] = o - error; we'll have to change the entire string
l=[10,22,30,40]
l[1]=20
print(l)
l[0]=30
l[3]=50
print(l)

#a list can store duplicates
l=[1,1,22,22,3,4,5,6,123,123,123]
print(l)

#same principles apply on string elements; example:
fruits=["apple", "banana", "mango"]
print(fruits[0])   #apple
print(fruits[-1])  #mango
print(fruits[0:2]) #list slicing: ["apple", "banana"]
fruits[1]=2 #mutation
print(fruits)
fruits[0]="grapes" #mutation
print(fruits)
fruits=["apple", "apple", "banana", 2.3]
print(fruits)

#traversing on list i.e. using loop on a list
b=[10,15,20,25,30]
#method 1: traversing on values
for i in b:
    print(i)
#method 2: traversing on index
for i in range(0,len(b)):
    print(b[i])