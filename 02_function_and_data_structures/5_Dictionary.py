#A dictionary is a collection of key-value pairs — think of it like a real dictionary where you look up a word (key) to find its meaning (value).
d = {"name": "Alex", "age": 20, "city": "Delhi"}
#Here:
#"name", "age", "city" are the keys
#"Alex", 20, "Delhi" are the values

#You access a value by providing its key, not an index like a list:
print(d["name"])  # prints 'Alex'
print(d["age"])   # prints 20
print(d["city"])  # prints 'Delhi'

#Keys must be unique — just like a set, dictionaries use hashing internally to store keys, 
#so no two keys can be the same. If you assign to an existing key, it just overwrites the value:
#d["age"] = 25   # updates age to 25, doesn't add a new entry

#creating a new key-value pair:
d["gender"]="Male"
print(d["gender"])  # prints 'Male'

#updating a key's value:
d["age"]="25"
print(d["age"])   # prints 25

#Keys must be immutable — same reason as sets, keys need to be hashable, 
#so you can use strings, integers, tuples as keys but not lists.
#Values can be anything — strings, integers, lists, even another dictionary:
d1 = {"scores": [10, 20, 30]}   # the value here is a list
print(d1)
print(d1["scores"])

# Dictionaries are ordered — dictionaries maintain insertion order, unlike sets. 
# So when you loop through a dictionary, you get keys in the order they were added.

# Traversing on a dictionary: 
d={10:100,20:200,30:300,40:400}
for i in d:    # iterates on the keys
    print(f"key: {i}, value: {d[i]}")  
