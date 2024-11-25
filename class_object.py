# classes and objects

# class CarDesign:
#     pass
#
#
# car_1 = CarDesign()
# car_2 = CarDesign()
# print(type(car_1))
# print(type(car_2))
class Instructor:
    def __init__(self, name, address):
        self.instructor_name = name
        self.address = address

    def display(self, name):
        print("Hi i'm {}".format(name))


instructor_1 = Instructor("jenny", "gurgaon")
print(instructor_1.instructor_name)
instructor_1.display("Ratul")
print(instructor_1.instructor_name)



