# Count number of days in a month

def check_days(year, month):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print("Year is leap year!")
        if month in [1, 3, 5, 7, 8, 10, 12]:
            print("31 days!")
        elif month == 2:
            print("29 days!")
        else:
            print("30 days!")
    else:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            print("31 days!")
        elif month == 2:
            print("28 days!")
        else:
            print("30 days!")


year: int = int(input("Enter year:"))
month: int = int(input("Enter month:"))
check_days(year, month)

