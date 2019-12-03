# Polymorphism - The same method may behave differently in different classes.

# Overriding - A derived class will inherit methods from the base class. But that method might not behave in the same way in the derived class. Derived class has the ability to change the behaviour of the method by redefining it.

class Employee:
    def setNumberOfWorkingHours(self):
        self.workingHours = 40
    def displayWorkingHours(self):
        print(self.workingHours)

class Trainee(Employee):
    # We can create the same method as the parent class and change the value of working hours accordingly. This way we dont have to create seperate method for this thing and waste extra memory. By invoking following method from this class, the number of working hours will be 45 for Trainee instead of general 40 hrs.
    def setNumberOfWorkingHours(self):
        self.workingHours = 45

    # Following method is defined to reset the value of working hours from 45 back to 40 (that of parent class). So when we call this method, the value will be back to original parent class.
    # NOTE - Using 'super()' function in this method uses the value from the parent class(40) instead that of child class(45). It does not change the value 'self.workingHours = 45'. It will remain as it is.
    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

# 1. Creating objects for Employee and Trainee class.
employee1 = Employee()
trainee1 = Trainee()

# 2. Printing working hours for the employee1 object.
employee1.setNumberOfWorkingHours()
employee1.displayWorkingHours()  # This prints 40.

# 3. Printing working hours for trainee1 object.
trainee1.setNumberOfWorkingHours()
trainee1.displayWorkingHours()  # This will print 45. We can call - displayWorkingHours() method which was defined in Parent class Employee.

# 4. Reseting the value of working hours for trainee from 45 back to 40 using - resetNumberOfWorkingHours method.
trainee1.resetNumberOfWorkingHours()
trainee1.displayWorkingHours()  # This will print 40 again.

# 5. If we call below 2 methods after the reset method then -
trainee1.setNumberOfWorkingHours()
trainee1.displayWorkingHours()  # This will return 45 only.
