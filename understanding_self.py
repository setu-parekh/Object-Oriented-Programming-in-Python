# 'self' refers to the object of the class. It is kind of a placeholder for the object. All the instance attributes without 'self' will not be available throughout the lifetime of an object. That particular attribute will only be available for a particular method.
class Employee:
    def employeeDetails(self):
        self.name = "Neel"
        age = 30   # Lifespan of this attribute is only within this method. It cannot be accessed from another method with 'self'.
        return self.name
        return age

employee1 = Employee()
employee_name = employee1.employeeDetails()
print(employee_name)
