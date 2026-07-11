#1)
d={10:100,20:200,30:300,40:400}
d.clear()  #removes all the elements/items (i.e. each key-value pair) from the dictionary
print(d)

#2) fromkeys() - returns a dictionary with the specified key(s) and value(s)
# fromkeys() is a dictionary class method used to create a new dictionary where:
# we provide an iterable of keys (like a list, tuple, set, or string)
# every key gets the same value (unless otherwise specified, the value is 'None')

#Example 1: without a specified value
keys=["a","b","c"]
d=dict.fromkeys(keys)
print(d)  

#Example 2: with a value 
d1=dict.fromkeys(keys,5)
print(d1)

#Example 3: using a string
d2=dict.fromkeys("ABC",1)   #each character of the string becomes a key
print(d2)   

#NOTE: fromkeys() is a class method, whereas clear() is an instance method. Therefore:
# clear() works on an existing dictionary object
# fromkeys() is called on the dictionary class (dict) itself as it created a new dictionary

#3) get() - returns the value of the specified key
d={10:100,20:200,30:300,40:400}
print(d.get(10))

#4) items() - returns a list containing a tuple for each key-value pair
print(d.items())

#5) keys() - returns a list containing the dictionary's keys
print(d.keys())

#6) values() - returns a list containing the dictionary's values
print(d.values())

#7) pop() - removes the element with the specified key and also returns the value linked with that key
print(d.pop(30))
print(d)

#8) popitem() - removes the last inserted key-value pair and returns them as a tuple
d={10:100,20:200,30:300,40:400}
print(d.popitem())
print(d)

#9) setdefault() - returns the value of the specified key. If the key doesn't exist: insert the key, with the specified value
d={10:100,20:200,30:300,40:400}
print(d.setdefault(30))  # 300
print(d)  # dictionary remains the same
print(d.setdefault(50,500))  # 500
print(d)  # dictionary is now updated

#10) update() - updates the dictionary with the specified key-value pairs
d.update({10:1000})
d.update({45:600})
print(d)