class ExcessFeeError(Exception):
    def __init__(self,amount,dueamount):
        self.amount = amount
        self.dueamount = dueamount

    def __str__(self):
        return f"Excess amount {self.amount} is being paid where only {self.dueamount} is to be paid"

class Student:
    # Class attribute
    courses = {"python": 10000, "java": 15000, "aws": 5000}

    # Constructor
    def __init__(self, name, course):
        # Object attributes
        self.name = name
        if course not in Student.courses:
            raise ValueError("Invalid Course!")
        self.course = course
        self.feepaid = 0

    def payment(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount. Must be > 0")

        if amount > self.getdue():
            raise ExcessFeeError(amount, self.getdue())

        self.feepaid += amount

    def show(self):
        print(f"Name   : {self.name}")
        print(f"Course : {self.course}")
        print(f"Feepaid: {self.feepaid}")

    def gettotalfee(self):
        return Student.courses[self.course]

    def getdue(self):
        return self.gettotalfee() - self.feepaid

    # Create an object


s1 = Student("Larry", "python")
s1.course = "java"

s1.payment(50000)
s1.payment(5000)
s1.show()
s2 = Student("Mark", "java")
