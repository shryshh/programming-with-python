#ACCEPT A YEAR AND CHECK IF ITS A LEAP YEAR
year=int(input("please enter a year: "))
if year%100!=0 and year%4==0:
    print(f"{year} is a leap year")
elif year%100==0 and year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")