# Example of Multi-level Inheritance: Father inherits from Grandfather and Son inherits from Father. So Son has characteristics of father and grandfather.

# Base class -
class MusicalInstruments:
    numberOfKeys = 12
# Following class will inherit from base class - MusicalInstruments
class StringInstruments(MusicalInstruments):
    typeOfWood = "Teek"
# Following class will inherit from 'StringInstruments' and indirectly also inherits attributes of 'MusicalInstruments'
class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
    def displayDetails(self):
        print("This guitar consist of {} strings. It is made up of {} wood and can play {} keys.".format(self.numberOfStrings, self.typeOfWood, self.numberOfKeys))

guitar1 = Guitar()
guitar1.displayDetails()
