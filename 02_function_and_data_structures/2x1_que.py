#Input: [3,-1,4,-5,9]
#Print all positive and negative elements separately

l=[3,-1,9,-5,4]
p=[]
n=[]
for i in l:
    if i>0:
        p.append(i)
    elif i<0:
        n.append(i)
p.sort()
n.sort()
print(f"positive: {p}")
print(f"negative: {n}")