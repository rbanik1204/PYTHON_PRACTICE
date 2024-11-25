weight: int = int(input("Enter your weight(in kg):"))
height: float = int(input("Enter your height(in cm):"))
BMI = round(weight/height**2,5)
BMI *= 10**4
print(round(BMI))
