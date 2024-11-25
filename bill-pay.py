import random
names = input("Write names with space:")
list = names.split(" ")
random.shuffle(list)
turn = random.choice(list)
print(f"{turn} will pay the bill")