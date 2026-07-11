#Input: [10,20,30,40]
#Find the mean (average) of all list elements
l=[10,20,30,40]
add=0
for i in l:
    add=add+i
print(f"average: {add/len(l)}")