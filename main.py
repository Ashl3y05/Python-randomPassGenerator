# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

output = ""
for letter in range(1, nr_letters+1):
    output += random.choice(letters)
for symbol in range(1, nr_symbols+1):
    output += random.choice(symbols)
for number in range(1, nr_numbers+1):
    output += random.choice(numbers)
print(f"Order not randomised: {output}")

passWordList = []
randOutput = ""
for characters in output:
    passWordList.append(characters)
random.shuffle(passWordList)
for randOut in passWordList:
    randOutput += randOut
print(f"Randomized order: {randOutput}")
