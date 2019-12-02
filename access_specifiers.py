# Public - making members (attributes and methods) of the class accessible to that particular class, derived class and also outside the derived class.

# Protected - making members (attributes and methods) of the class accessible to that particular class and its derived members.

# Private - making members (attributes and methods) of the class only accessible to that class only. It is not even accessible to its derived class.

class Car:
    numberOfWheels = 4  # This is syntax for naming public member of the class.
    _color = "Black"  # This is syntax for naming protected member of the class.
    __yearOfManufacture = 2017  # This is syntax for naming private member of the class.

class BMW(Car):
    def displayDetails(self):
        print("The color of the car is {}".format(self._color))

car1 = Car()
print("Public attribute numberOfWheels:", car1.numberOfWheels)
print("Protected attribute color:", car1._color)

print("Private attribute yearOfManufacture:", car1.__yearOfManufacture)
# Above print line will error that attribute does not exist. Correct syntax is shown below:
print("Private attribute yearOfManufacture:", car1._Car__yearOfManufacture)

BMW1 = BMW()
BMW1.displayDetails()
