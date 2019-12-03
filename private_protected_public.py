# Public - making members (attributes and methods) of the class accessible to that particular class, derived class and also outside the derived class.

# Protected - making members (attributes and methods) of the class accessible to that particular class and its derived members.

# Private - making members (attributes and methods) of the class only accessible to that class only. It is not even accessible to its derived class.

# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj, ceo):
        self.name = name      # name(name of company) is public
        self._proj = proj     # proj(current project) is protected
        self.__ceo = ceo      # ceo is private

    def who_is_ceo(self):
        print("CEO is {}".format(self.__ceo))

# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj, ceo):
        # calling parent class constructor
        Company.__init__(self, cName, proj, ceo)
        self.name = eName   # public member variable
        self.__sal = sal    # private member variable

    # public function to show salary details
    def show_sal(self):
        print("The salary of {} is {} ".format(self.name, self.__sal,))

    def show_ceo_and_proj(self):
        print("CEO: {} || Project: {}".format(self.__ceo, self._proj))

import ipdb; ipdb.set_trace()
# creating instance of Company class
comp = Company("Stark Industries", "Mark 4", "Mr. CEO")

# print(comp.__ceo) - This will not work. Because __ceo is private attribute.

# creating instance of Employee class
empl = Emp("Steve", 9999999, comp.name, comp._proj, 'Ms. New CEO')

print("Welcome to ", comp.name)
print("Here",empl.name,"is working on",empl._proj)

# to show the value of __sal we have created a public function show_sal()
empl.show_sal()
