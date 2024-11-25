# Building a calculator for addition, subtraction, multiplication, division
def switch_value(choice, val1, val2):
    if choice == 1:
        print("Summation value:", end="")
        return val1 + val2
    elif choice == 2:
        print("Subtraction value:", end="")
        return val1 - val2
    elif choice == 3:
        print("Multiplication value:", end="")
        return val1 * val2
    elif choice == 4:
        print("Division value:", end="")
        return val1 / val2
    else:
        return f"Invalid Choice Please give a valid input!"


def insert_values(value_1):
    choice: int = int(input("choose an operation:"))
    if value_1 is None:
        value_1: int = int(input("Enter first Value:"))
    value_2: int = int(input("Enter second Value:"))
    return choice, value_1, value_2


def output_view(value_1):
    choice, value_1, value_2 = insert_values(None)
    Output = switch_value(choice, value_1, value_2)
    print(Output)
    select = input("Want to continue with this value? \"yes\" or \"no\":").lower()
    if select == "yes":
        output_view(Output)


print("Following menu:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
select = "yes"
while select != "no":
    if select == "yes":
        output_view(None)
    select = input("Want to do another operation?\n1. Yes\n2. No\nEnter your choice:").lower()




