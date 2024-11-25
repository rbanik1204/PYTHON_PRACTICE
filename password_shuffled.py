import random
array: list = []
password: list = []
sub_list_num: int = int((input("Enter the number of sub-lists :")))
for i in range(sub_list_num):
    sub_list_input: str = input("Enter {} index items with commas:".format(i))
    sub_list = list(map(str, sub_list_input.split(",")))
    array.append(sub_list)
for i in range(len(array)):
    random.shuffle(array[i])
random.shuffle(array)
print("Suggested passcode:")
for i in range(0, random.randint(1, len(array))):
    for j in range(0, random.randint(1, len(array[i]))):
        password.append(array[i][j])
random.shuffle(password)
for i in range(len(password)):
    print(password[i], end="")



