import random
array: list = []
size: int = int(input("Enter size:"))
for i in range(0,size):
    array.append(int(input()))
select_value: int = random.choice(array)
print(select_value)
