#Input: [4,8,2,9,1]
#Find the greatest element and print its index

l=[4,8,2,9,1]
g=l[0]
for i in l:
    if i>g:
        g=i
print(f"greatest element: {g} at the index {l.index(g)}")

#alternatively:
g=l[0]
index=0
for i in range(len(l)):
    if l[i]>g:
        g=l[i]
        index=i
print(f"greatest element: {g} at the index {index}")

#what if the greatest element occurs more than once?
l=[4,9,2,9,1,9]
g=l[0]
for i in l:
    if i>g:
        g=i
indices=[]
for i in range(len(l)):
    if l[i]==g:
        indices.append(i)
print(f"greatest element: {g} at the indices {indices}")

#alternatively:
g=l[0]
indices=[]
for i in range(1,len(l)):
    if l[i]>g:
        g=l[i]
        indices.append(i)
    elif l[i]==g:
        indices.append(i)
print(f"greatest element: {g} at the indices {indices}")