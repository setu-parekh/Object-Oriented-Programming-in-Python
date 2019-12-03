'''
Write a program to design a car rental system:
    1. Type of cars provided for rent: Hatchback, Sedan, SUV
    2. Rent per day: Hatchback = $30, Sedan = $50, SUV = $100.
    3. Prompt user to ask for type of car required, number of days for renting and provide the user with total fare details.
'''
class Cars:
    # Method to initialize the attribute for rent details -
    def __init__(self):
        self.rent = {'Hatchback': 30, 'Sedan': 50, 'SUV': 100}
    # Method to display rent of each kind of car to customers -
    def displayRentDetails(self):
        print("Rent for Hatchback is ${} per day".format(self.rent['Hatchback']))
        print("Rent for Sedan is ${} per day".format(self.rent['Sedan']))
        print("Rent for SUV is ${} per day".format(self.rent['SUV']))
    # Method to calculate total fare based on type of car and days for renting.
    def calculateFare(self, typeOfCar, numberOfDays):
        self.totalFare = self.rent[typeOfCar] * numberOfDays
        return self.totalFare

car = Cars()
while True:
    # Printing the menu for customers to select the desired action.
    print("Enter 1 for rental information.")
    print("Enter 2 if you want to rent a car.")
    print("Enter 3 to exit.")

    user_input = int(input("Please enter the number: "))

    if user_input == 1:
        car.displayRentDetails()
    elif user_input == 2:
        car_type = input("Please enter the type of car you want to rent: ")
        rental_days = int(input("Please enter the number of days you want to rent the car: "))
        print("Your total fare is {}".format(car.calculateFare(car_type, rental_days)))
    else:
        quit()
