#ACCEPT NAME AND AGE AND CHECK IF THE USER IS A VALID VOTER (18+)
name=input("please enter your name: ")
age=int(input("please enter your age: "))
if age>=18:
    print(f"hello {name}, you are a valid voter")
else:
    print(f"hello {name}, you are not a valid voter as of now but you can vote after {18-age} years")