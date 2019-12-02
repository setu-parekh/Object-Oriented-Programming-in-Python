# Two classes will be created. First class will have some attributes and methods and the 2nd class will inherit those attributes and methods apart from having their own.
class Apple:
    manufacture = 'Apple Inc.'
    contactWebsite = 'www.apple.com/contact'
    def contactDetails(self):
        print("To contact us, log on to", self.contactWebsite)

# When created class in the following manner, class MacBook inherits all the properties from the class Apple apart from its own.
class MacBook(Apple):
    yearOfManufacture = 2017
    # or,
    # def __init__(self):
    #     self.yearOfManufacture = 2017
    def manufactureDetails(self):
        print('This MacBook was manufactured by {} in the year {}'.format(self.manufacture, self.yearOfManufacture))

macbook1 = MacBook()
macbook1.manufactureDetails()
macbook1.contactDetails()
