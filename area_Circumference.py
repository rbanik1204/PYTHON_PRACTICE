# Counting area and circumference using class method
import math


class Circle:
    def __init__(self, radii):
        self.radius = radii

    def area_circle(self) -> str:
        area: int = math.pi * self.radius**2
        return "area of the circle having radii {} is {:.2f}".format(self.radius,area)

    def circum_circle(self) -> str:
        circum: int = 2 * math.pi * self.radius
        return "circumference of the circle having radii {} is {:.2f}".format(self.radius,circum)


radius = int(input("Enter radius:"))
circle_1 = Circle(radius)
print(circle_1.area_circle())
print(circle_1.circum_circle())

