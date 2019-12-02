# Write a program to create a precious stone. A person cannot posses more than 5 stones at any given point of time. If there are more than 5 stones, delete the first stone and store the new one.

class preciousStones:
    number_of_stones = 0
    stones_list = []
    def __init__(self, stone_name):
        self.name = stone_name
        preciousStones.number_of_stones += 1
        if preciousStones.number_of_stones <= 5:
            preciousStones.stones_list.append(self)
        else:
            del preciousStones.stones_list[0]
            preciousStones.stones_list.append(self)

    @staticmethod
    def printNames():
        for stone in preciousStones.stones_list:
            print(stone.name)

stone1 = preciousStones("Diamond")
stone2 = preciousStones("Ruby")
stone3 = preciousStones("Emerald")
stone4 = preciousStones("Sapphire")
stone5 = preciousStones("Pearl")
# Printing the original list of 5 stones.
stone5.printNames()
stone6 = preciousStones("Alexandrite")
# Printing new list after adding 6th stone and deleting the 1st stone.
stone6.printNames()
