def add(*numbers): # creates a tuple of the numbers
    c: int = 0
    for i in numbers:
        c = c + i
    print(f"sum is {c}")


add(5, 7, 9)
