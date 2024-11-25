size=input("what size of pizza do you want?\nL/M/S\n")
bill=0
if size == 's' or size == 'S':
    bill += 100
    print(f"please pay {bill} rupees")
elif size == 'm' or size == 'M':
    bill += 200
    print(f"please pay{bill} rupees")
elif size == 'l' or size == 'L':
    bill += 300
    print(f"please pay{bill} rupees")
add_pepperoni=input("do u want extra pepperoni?")
if add_pepperoni == 'y' or add_pepperoni == 'Y':
    if size == 's' or size == 'S':
        bill += 30
    else:
        bill += 50
add_cheese = input("do you want extra cheese?")
if add_cheese == 'y' or add_cheese == 'Y':
    bill += 20
print(f"then your total bill is {bill}")
print("Thank you")
