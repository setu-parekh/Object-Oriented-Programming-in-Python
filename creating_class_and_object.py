
# Program to check whether the employee has met his/her weekly target or not.

# Creating a class:
class Employee:
    name ="Setu" # As we have hard coded the name of the class attribute, it will remain same for all the objects created within this class.
    designation = "Manager"
    salesThisWeek = 6
    # Defining a method to check wether the employee has achieved the minimum sales target or not. 'self' parameter is passed inside the method to access the attributes of the class.
    def hasAchievedTarget(self):
        if self.salesThisWeek > 5:
            print("Sales target has been achieved")
        else:
            print("Sales target has not been achieved")
# Defining an object for the class. Creating object is called Object instantiation and will have access to all attributes and methods of the class. employeeOne is the object in the class Employee.
employeeOne = Employee()
employeeTwo = Employee()
# Accessing attribute - name :
employeeOne.name
print(employeeOne.name)
# Calling method hasAchievedTarget on the object:
employeeOne.hasAchievedTarget()

# Changing the value of the class attribute.
Employee.name = 'Neel'
print(employeeOne.name)

# Creating Instance attribute for an object.
employeeOne.age = 50
print(employeeOne.age)

# Changing the value of class attribute for a particular object.
employeeOne.designation = "Assistant Manager"
print(employeeOne.designation)  # Output: Assistant Manager
print(employeeTwo.designation)  # Output: Manager
