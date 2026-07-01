#PRINT SUM OF ALL EVEN AND ODD NUMBERS IN A RANGE SEPARATELY

max=int(input("enter max value of the range: "))
min=int(input("enter min value of the range: "))
e_sum=0
o_sum=0
for i in range(min,max+1):
    if i%2==0:
        e_sum=e_sum+i
    else:
        o_sum=o_sum+i
print(f"even sum: {e_sum}")
print(f"odd sum: {o_sum}")