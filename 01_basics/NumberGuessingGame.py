#COMPUTER PICKS A RANDOM NUMBER BETWEEN A RANGE SET BY A USER, THE USER KEEPS GUESSING UNTIL CORRECT 

import random

low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

# swap bounds if user entered them in the wrong order
if low > high:
    temp = low
    low = high
    high = temp

number = random.randint(low, high)
print("okay so the computer has decided on a random number in the range provided by you")
guess=0
t=0
while guess!=number:
    guess=int(input(f"please enter your guess (between {low} and {high}): "))
    if guess>number:
        print("hint: go lower")
    elif guess<number:
        print("hint: go higher")
    t=t+1
    print(f"(number of tries: {t})")    
print("congratulations! you guessed the number")
print(f"total tries: {t}")