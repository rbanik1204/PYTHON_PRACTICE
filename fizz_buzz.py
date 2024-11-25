a=range(1,101)
for i in a:
    if i%5!=0 and i%3!=0:
        print(i)
    elif i%3==0 and i%5!=0:
        i="fizz"
        print(i)
    elif i%5==0 and i%3!=0:
        i="buzz"
        print(i)
    elif i%5==0 and i%3==0:
        i="fizzbuzz"
        print(i)

