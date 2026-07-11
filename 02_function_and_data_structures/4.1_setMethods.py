"""Single set operations"""
#1)
s={10,20,30,40}
s.add(50)
print(s)
s.add(10)   #nothing happens
print(s)

#2)
s.clear()   #removes all the elements - creates an empty set
print(s)

#3)
s={10,20,30,40}
s.discard(20)  #removes a specific element
print(s)
s.remove(30)   #removes a specific element
print(s)

#4)
s={10,20,30,40}
a=s.pop()  #removes any random element and then returns that element
print(s)
print(a)


"""Multi set operations"""
#1)Difference
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.difference(s2))  #or alternatively we can do 'print(s1-s2)' 
print(s2.difference(s1))  #or alternatively we can do 'print(s2-s1)' 

#2)Difference & Update
s1.difference_update(s2)  #or alternatively we can do 's1-=s2' - updates the set s1 to the difference s1-s2
print(s1)
s1={10,20,30,40}
s2={30,40,50,60}
s2-=s1
print(s2)

#3)Intersection
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.intersection(s2))  #or alternatively we can do 'print(s1&s2)'
#and obviously we get the same output for 'print(s2&s1)'

#4)Intersection & Update
s1&=s2
print(s1)  #s1 is updated
print(s2)  #s2 is still the same
s2&=s1
print(s2)  #s2 is also updated 

#5)issubset() - returns 'True' is all items of a provided set is present in another set
s1={10,20,30,40}
s2={30,40,50,60}
s3={30,40,60}
print(s3.issubset(s1))   #or alternatively we can do 'print(s3<=s1)'  - False
print(s3.issubset(s2))   #or alternatively we can do 'print(s3<=s2)'  - True

#6)issuperset()
s1={10,20,30,40}
s2={30,40,50,60}
s3={30,40,60}
print(s1.issuperset(s3))   #or alternatively we can do 'print(s1>=s3)'  - False
print(s2.issuperset(s3))   #or alternatively we can do 'print(s2>=s3)'  - True

#7)symmetric_difference() 
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.symmetric_difference(s2))   #or alternatively we can do 'print(s1^s2)' - a new set which has all the elements of set s1 and s2 except the common elements
#same output for s2^s1

#8)symmetric_difference() & update
s1^=s2   #set s1 is now updated 
print(s1)
s1={10,20,30,40}
s2^=s1   #set s2 is now updated
print(s2)

#9)Union
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.union(s2))      #or alternatively we can do 'print(s1|s2)'
#same output for s2|s1

#10)union & update 
s1.update(s2)    #or alternatively we can do 'print(s1|=s2)'
print(s1)     #set s1 is now updated
s1={10,20,30,40}
s2|=s1
print(s2)     #set s2 is now updated

#11)isdisjoint() - checks whether two sets have no common elements
#returs True if the sets have no common elements
#returs False if the sets share at least one element
s1={1,2,3}
s2={4,5,6}
print(s1.isdisjoint(s2))  #True
s1={1,2,3}
s2={3,4,5}
print(s1.isdisjoint(s2))  #False
s1={1,2,3}
s2={2,4,3,5}
print(s2.isdisjoint(s1))  #False
