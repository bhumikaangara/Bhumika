class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, name, account_number, balance, interest_rate):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)
        print("Interest added")


# Creating objects
acc1 = BankAccount("Ravi", 101, 5000)
acc2 = SavingsAccount("Ganga", 102, 10000, 5)

# Operations
print("---- Normal Account ----")
acc1.deposit(2000)
acc1.withdraw(1000)
print("Balance:", acc1.get_balance())

print("\n---- Savings Account ----")
acc2.deposit(3000)
acc2.add_interest()
print("Balance:", acc2.get_balance())
