#Sets are unordered and can't have duplicates but it is mutable
a={}
print(type(a))  #dictionary; an empty curly brackets is classified as a dictionary
a={1,2,3}
print(type(a))  #set

#how many unique values are in a list?
l=[1,2,2,3,4,4,5,5,5,6,7,8,8,9]
print(f"number of elements in the list: {len(l)}")
print(l)
l=set(l)
print(f"number of unique elements: {len(l)}")
print(l)


"""A hash value is a unique fixed-size number generated from a value by a hash function. 
When you add an element to a set, 
Python computes its hash value and uses that as a kind of "address" to store it. 
Before adding, it checks if that hash already exists in the set — if it does, 
the element is considered a duplicate and gets rejected. 
So duplicates are prevented precisely because two identical values 
always produce the same hash, 
and the set uses that to detect and discard them."""
#example:
print(hash("hello"))   #hash value of a string changes every time we run the python file

"""a set can only store immutable objects
(because hash values for only immutable objects can be generated) 
and hence it can't store a list"""

"""A set is unordered because 
sets store elements based on their hash values, not in the order we insert them."""

"""Since a set is unordered, we can't traverse on a set using the index of its elements"""
"""Even when we traverse on the elements and print them, 
they're not printed in the order in which they are inserted since
the traversal order is determined by their hash values """
s={1,3,30,20}     #hash value of an integer remains the same 
for i in s:
    print(i)    #1 3 20 30

"""Quick rundown:
(session - each run of the python file)
- int, float, bool — hash is always the same across sessions
- tuple — hash is always the same, as long as it contains only integers/floats/bools 
(since the tuple's hash is derived from its elements' hashes)
if the tuple contains a string then its hash is randomized every session
- str — randomized every session
- mutable types (list, dict, set) — not hashable at all, so can't be stored in a set"""