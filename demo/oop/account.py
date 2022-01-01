class SavingsAccount:
    # Static or class attribute
    minbal = 5000

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal

    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        # Private attributes
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance - SavingsAccount.minbal >= amount:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient Balance")

    def show(self):
        print(self.acno)
        print(self.ahname)
        print(self.__balance)

    def getbalance(self):
        return self.__balance


print(SavingsAccount.getminbal())

a = SavingsAccount(1, "Abc", 10000)
a.deposit(10000)
print(a.getbalance())
print(a.__dict__)
print(a._SavingsAccount__balance)
a.withdraw(18000)
a2 = SavingsAccount(2, "Mark")
