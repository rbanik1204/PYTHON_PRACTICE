# function calling function

def func2(value):
    return value + 1


def func1(a, b):
    return a+b


print(func2(func1(b=20, a=10)))
