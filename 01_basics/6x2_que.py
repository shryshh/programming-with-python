#CREATE A PROGRAM WHICH RUNS A LOOP AND MENTIONS WHETHER A BREAK WAS ENCOUNTERED OR NOT
#example 1: break happens, so else doesn't run
break_check=False  #FLAG VARIABLE: a variable which is used to remember whether something has happened or not
for i in range(5):
    if i==3:
        break_check=True
        break
    print(i)
else:
    print("loop finished, no break was encountered")
if break_check==True:
    print("loop finished, break was encountered")

print()

#example 2: no break, so else runs
break_check=False
for i in range(5):
    if i==7:
        break_check=True
        break
    print(i)
else:
    print("loop finished, no break was encountered")
if break_check==True:
    print("loop finished, break was encountered")