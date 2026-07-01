#REVERSE A STRING WITHOUT USING BUILT-IN FUNCTIONS
rev=""
s=input("enter a string: ")
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print(rev)

#CHECK IF A STRING IS A PALINDROME
rev=""
s=input("enter a string: ")
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
if rev==s:
    print("the string is a plaindrome")
else:
    print("not palindrome")