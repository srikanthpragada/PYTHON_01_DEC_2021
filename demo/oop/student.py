class Student:
    # Class attribute
    courses = {"python": 10000, "java": 15000, "aws": 5000}

    # Constructor
    def __init__(self, name, course):
        # Object attributes
        self.name = name
        self.course = course
        self.feepaid = 0

    def payment(self, amount):
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
s1.course = "Java"
s1.payment(5000)
s1.payment(5000)
s1.show()
s2 = Student("Mark", "java")
