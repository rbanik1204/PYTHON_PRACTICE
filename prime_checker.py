def prime_checker(number: int):
    for i in range(2, number):
        if number % i == 0:
            print("Number is not prime")
            return
    print("It is a prime number!")


number: int = int(input("Enter value:"))
prime_checker(number)

