#ACCEPT GENDER FROM USER AND PRINT A GREETING MESSAGE
a=input("state your gender: ")
if a=="M" or a=="m" or a=="male" or a=="Male" or a=="MALE":
    print("good evening, sir")
elif a=="F" or a=="f" or a=="female" or a=="female" or a=="FEMALE":
    print("good evening, ma'am")
else:
    print("incorrect gender input")