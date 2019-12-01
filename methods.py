# Instance method example:
class Employee:
    def employeeDetails(self):
        self.name = "Ben"
        self.age = 27
        # return self.name, self.age

    # If we dont pass self parameter inside the method - welcomeMessage, then it will give error because we are passing the object as the parameter while invoking the method. But while defining, we didnt pass any parameter.

    # We can use '@staticmethod' when the method belongs to the class but does not use the object as the parameter.
    @staticmethod
    def welcomeMessage():
        print("Welcome to our organization!")

employee1 = Employee()
employee1.employeeDetails()
print(employee1.name)
print(employee1.age)

# Following line will give an error if we dont use '@staticmethod'. After using '@staticmethod', following line will still execute the method - welcomeMessage even without passing the object while invoking the method.
employee1.welcomeMessage()
