n = int(input("Enter number of rows:"))
"""for i in range(0,n):
    for j in range(0,i+1):
        print("*", end=" ")
    print("\n")"""
"""for i in range(0,n):
    for j in range(n-i):
        print("*", end=" ")
    print("\n")"""
"""for i in range(1, n+1):
    for j in range(0, n-i):
        print(" ", end="")
        if j == n-i-1:
            print("*"*i)
    if i == n:
        print("*" * i)
    print("\n")"""
"""for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end="")
    print("* "*i)
    for j in range(1, n-i+1):
        print(" ", end="")
    print("\n")"""
for i in range(0, n):
    for j in range(0, n-i):
        if 65+i < 69:
            print(chr(65+i), end="")
        else:
            print(chr(69+i), end="")
    print("\n")
# print(chr(69+n), end="")


