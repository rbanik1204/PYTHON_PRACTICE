# program to square each element of a list and find sum of them

numbers: list = [2, 6, 7, 8]
powers: list = [4, 3, 2, 1]
squared = list(map(lambda x: x[0] ** x[1], zip(numbers, powers)))
print(squared)
