#ACCEPT TEMP IN °C AND PROVIDE A DESCRIPTION
temp=int(input("enter temp: "))
if temp>=-5 and temp<=5:
    print("very cold")
elif temp<-5:
    print("very very cold")
elif temp>=6 and temp<=18:
    print("cold")
elif temp>=19 and temp<=30:
    print("hot")
else:
    print("very hot")