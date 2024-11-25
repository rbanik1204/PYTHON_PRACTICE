import random
letters = ['A', 'B', 'C', 'D', 'E']
letters_new = []
Symbols = ['(', '*', '&', '#', '!']
symbols_new = []
numbers = [1, 2, 3, 4, 5, 6]
numbers_new = []
print("welcome to password generator")
a = input("how many letters would you like in your password?\n")
b = input("how many special characters you want in your password?\n")
c = input("how many numbers you want in your password?\n")
for i in range(0,int(a)):
    letters_new.append(random.choice(letters))
print(letters_new)
for i in range(0,int(b)):
    symbols_new.append(random.choice(Symbols))
for i in range(0,int(c)):
    numbers_new.append(random.choice(numbers))
for i in range(0,int(a)):
    print(letters_new[i], end="")
for i in range(0,int(b)):
    print(symbols_new[i], end="")
for i in range(0,int(c)):
    print(numbers_new[i], end="")