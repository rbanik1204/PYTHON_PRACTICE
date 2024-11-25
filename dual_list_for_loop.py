list1: list = ["Hi", "Hello","Welcome"]
names: list = ["Ratul", "jenny", "Ritu"]
for i in list1:
    for name in names:
        print(i, name)
    if i == "Hello":
        break
else:
    print("Out of for loop!")
print("Out of loop!")
