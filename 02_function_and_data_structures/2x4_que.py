#Input: [4,2,9,8,1,8,7,9,8,9,10]
#Find the second greatest element and print its index

l=[4,2,9,8,1,8,7,9,8,9,10]
g=l[0]
s_g=l[0]
s_g_index=[]
for i in l:
    if i>g:
        s_g=g
        g=i
    elif i>s_g and i!=g:
        s_g=i
for j in range(len(l)):
    if l[j]==s_g:
        s_g_index.append(j)
print(f"second greatest: {s_g} at the indices {s_g_index}")