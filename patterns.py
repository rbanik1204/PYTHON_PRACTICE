row_num: int = int(input("Enter number of rows:"))
# for i in range(0, row_num):
#     print(" "*(row_num-i), end="")
#     for j in range(i+1):
#         print("* ", end="")
#     print("\n")
# for i in range(row_num):
#     print(" "*(row_num-i), end="")
#     for j in range(i+1):
#         print(str(row_num-j)+" ", end="")
#     print("\n")
initial_char_asc: int = int(input("Enter character ASCII:"))
for i in range(row_num):
    for j in range(row_num-i):
        if initial_char_asc == 67:
            initial_char_asc = 70
        print(chr(initial_char_asc)+" ", end="")
    initial_char_asc += 1
    print("\n")

