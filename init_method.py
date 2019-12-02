# We have to initialize all the object or class attributes before they are called or being used. There is a special method called 'init' method which is called during object creation.
'''
class Employee:
    def employeeDetails(self):
        self.name = 'Setu'

    def displayEmployeeDetails(self):
        print("My name is", self.name)

employee1 = Employee()
employee1.displayEmployeeDetails()
'''
# Above line will result into error when we invoke the method - displayEmployeeDetails first. This is because we havent called 'employeeDetails' method to initialize the attribute.

# We will use the special method - '__init__' to initialize the instance attributes.
# Revised code -
'''
class Employee:
    def __init__(self):
        self.name = 'Ben'
    def displayEmployeeDetails(self):
        print('My name is', self.name)

employee1 = Employee()
employee1.displayEmployeeDetails()
'''

# Another way -
# If we dont want to hard code the name and age attributes, we can pass those parameters while creating the object and providing aliases for the attributes while defining the __init__ method as shown below.
class Employee:
    def __init__(self, employee_name, employee_age):
        self.name = employee_name
        self.age = employee_age
    def displayEmployeeDetails(self):
        print("My name is {0} and my age is {1}.".format(self.name, self.age))

employee1 = Employee('Setu Neel Gandhi', 27)
employee2 = Employee('Neel Gandhi', 27)
employee1.displayEmployeeDetails()
employee2.displayEmployeeDetails()
