# Condition - There are 4 classes - LivingThing, Animal, Reptile and Snake.
# Base class - LivingThing.
# Animal and Reptile inherits from LivingThing.
# Snake inherits from Animal and Reptile.

#  Case 1: No overriding of method in any class.
class LivingThing:
    def breathe(self):
        print("I breathe like a living thing.")
class Animal(LivingThing):
    pass
class Reptile(LivingThing):
    pass
class Snake(Animal, Reptile):
    pass

cobra = Snake()
cobra.breathe() # This will invoke the method inside the base class - Living Thing. Output: I breathe like a living thing.

# Case 2: Overriding method in class Animal only.
class LivingThing:
    def breathe(self):
        print("I breathe like a living thing.")
class Animal(LivingThing):
    def breathe(self):
        print("I breathe like an Animal.")
class Reptile(LivingThing):
    pass
class Snake(Animal, Reptile):
    pass

cobra = Snake()
cobra.breathe() # This will invoke overriden method inside class Animal and output: I breathe like an Animal.

# Case 3: Overriding method in class Reptile only.
class LivingThing:
    def breathe(self):
        print("I breathe like a living thing.")
class Animal(LivingThing):
    pass
class Reptile(LivingThing):
    def breathe(self):
        print("I breathe like a Reptile.")
class Snake(Animal, Reptile):
    pass

cobra = Snake()
cobra.breathe() # This will invoke overriden method inside class Reptile and output: I breathe like a Reptile.

# Case 4: Overriding method in both class Animal and Reptile.
class LivingThing:
    def breathe(self):
        print("I breathe like a living thing.")
class Animal(LivingThing):
    def breathe(self):
        print("I breathe like an Animal.")
class Reptile(LivingThing):
    def breathe(self):
        print("I breathe like a Reptile.")
class Snake(Animal, Reptile):
    pass

cobra = Snake()
cobra.breathe() # This will invoke overriden method inside class Animal because of the order in class Snake(Animal, Reptile) and output: I breathe like an Animal.
# If class Snake(Reptile, Animal), then output will be - I breathe like a Reptile.
