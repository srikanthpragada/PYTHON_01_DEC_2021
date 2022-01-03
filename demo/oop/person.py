# Special methods

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        print("__eq__")
        return self.name == other.name and self.age == other.age

    # def __lt__(self, other):
    #     print('__lt__')
    #     return self.age < other.age

    def __gt__(self, other):
        print('__gt__')
        return self.age > other.age

    def __int__(self):
        return self.age


p1 = Person("Mark", 30)
p2 = Person("Mark", 30)
print(p1)
print(str(p1))
print(p1.__str__())
print(id(p1), id(p2))
print(p1 == p2)  # p1.__eq__(p2)
print(p1 != p2)

persons = [Person("A", 20), Person("B", 40), Person("C", 30)]

for p in sorted(persons):
    print(p)

print(int(p1) + int(p2))  # p1.__int__() + p2.__int__()

for p in sorted(persons, key=lambda p: p.name):
    print(p)
