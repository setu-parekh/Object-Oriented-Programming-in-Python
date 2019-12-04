from random import randint

class SavingsAccount:
# Defining method to create a dictionary to store the account number and the customer's name, deposit details attached to that number. Dictionary is in the form - {accountNumber:[name, deposit_amount]}
    def __init__(self):
        self.accountDetails = {}

# Defining method for creating new account where customer will provide their name and initial deposit amount. This method will also generate a random account number.
    def createNewAccount(self, name, initial_deposit):
        self.name = name
        self.deposit = initial_deposit
        # Generating new account number using randint function:
        self.accountNumber = randint(10000, 99999)
        # Linking the newly created account number with the customer's name and initial deposit details. Storing these details in a dictionary named 'accountDetails'
        self.accountDetails[self.accountNumber] = [name, initial_deposit]
        print("Account creation has been successful. Your account number is ", self.accountNumber)

# Defining method to create authentication system. It will match the account number and name provided by the customer and check for its existence in its 'accountDetails' dictionary. If the data exists correctly, the authentication is successful.
    def authenticateAccount(self, name, accountNumber):
        if accountNumber in self.accountDetails.keys():
            if self.accountDetails[accountNumber][0] == name:
                print("Authentication successful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication failed")
                return False
        else:
            print("Authentication failed")
            return False

# Defining a method to display the account balance:
    def displayBalance(self):
        print("Your account balance is Rs.{}".format(self.accountDetails[self.accountNumber][1]))

# Defining a method for money withdrawal by the customers. It takes the amount of withdrawal as the parameter and displays the resulting balance in the account.
    def withdrawMoney(self, withdrawalMoney):

        if withdrawalMoney < self.accountDetails[self.accountNumber][1]:
            self.accountDetails[self.accountNumber][1] = self.accountDetails[self.accountNumber][1] - withdrawalMoney
            print("Withdrawal was successful!")
        else:
            print("Sorry!Insufficient Balance.")
        self.displayBalance()

# Defining method to deposit money into the account and then displaying the resultant account balance.
    def depositMoney(self, depositMoney):
        self.accountDetails[self.accountNumber][1] = self.accountDetails[self.accountNumber][1] + depositMoney
        self.displayBalance()

customerSavingAccount = SavingsAccount()

while True:
# Providing menu to customers for selecting the action they want to perform.
    print("1 : Create new account.")
    print("2 : Access your existing account.")
    print("3 : Exit.")
    user_choice = int(input("Enter your choice: "))
# Creating new account if the choice is 1.
    if user_choice == 1:
        customerSavingAccount.createNewAccount("Setu", 1300)
        print(customerSavingAccount.accountDetails)
# Accessing the existing account if the choice is 2. Authenticating the details first and then performing Deposit and Withdrawal actions.
    elif user_choice == 2:
        customer_name = input("Enter your name: ")
        customer_account_number = int(input("Enter your 5 digit account number: "))
        authentication_status = customerSavingAccount.authenticateAccount('Setu', customer_account_number)
        if authentication_status is True:
            while True:
                print("Type 'D' to deposit money.")
                print("Type 'W' to withdraw money.")
                print("Type 'DB' to display the balance.")
                user_action = input("Select from above options: ")
                if user_action == "D":
                    deposit_amount = int(input("How much do you want to deposit? "))
                    customerSavingAccount.depositMoney(deposit_amount)
                elif user_action == 'W':
                    withdraw_amount = int(input("How much do you want to withdraw? "))
                    customerSavingAccount.withdrawMoney(withdraw_amount)
                else:
                    customerSavingAccount.displayBalance()
        else:
            print("Sorry, You are not a authorized user. Please enter correct credentials.")
            break
    else:
        quit()







    # break
