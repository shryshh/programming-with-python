#COUNT LETTERS, DIGITS, AND SPECIAL SYMBOLS IN A STRING

#method 1
text = input("Enter a string: ")

letters = 0
digits = 0
special = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special symbols:", special)

#method 2
text = input("Enter a string: ")

letters = 0
digits = 0
special = 0

for ch in text:
    code = ord(ch)  # get ASCII/Unicode code

    # Check if it's a letter (A–Z or a–z)
    if (65 <= code <= 90) or (97 <= code <= 122):
        letters += 1
    # Check if it's a digit (0–9)
    elif 48 <= code <= 57:
        digits += 1
    # Otherwise, it's a special symbol
    else:
        special += 1

print("Letters:", letters)
print("Digits:", digits)
print("Special symbols:", special)
