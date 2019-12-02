# Multiple inheritance - A class can inherit attributes and methods from more than 1 base class.

# When the base class is only used to inherit attributes, then they can be initialized directly only without __init__method.

# In following example, both classes - OperatingSystem and Apple are having same variable: name. So when the common variable is used in the child class, it will consider the attribute of the base class written first while defining the child class. eg - class MacBook(OperatingSystem, Apple). 'name' attribute of OperatingSystem class will be considered.

# Base class
class OperatingSystem:
    multitasking = True
    name = "Mac OS"
# Base class
class Apple:
    website = "www.apple.com"
    name = "Apple"
# Defining class which will inherit characteristics of both base classes.
class MacBook(OperatingSystem, Apple):
    def displayDetails(self):
        if self.multitasking is True:
            print("This is multitasking system. Visit {} for more details.".format(self.website))
            print("Name: {}".format(self.name))

MacBookPro = MacBook()
MacBookPro.displayDetails()
