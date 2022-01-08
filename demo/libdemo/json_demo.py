import json


class SavingsAccount:
    def __init__(self, acno, ahname, balance=0):
        self.acno = acno
        self.ahname = ahname
        self.balance = balance


a = SavingsAccount(1, "Abc", 10000)
s = json.dumps(a.__dict__)
print(s)

d = json.loads(s)
print(d)
