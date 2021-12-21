def has_digit(st):
    for c in st:
        if c.isdigit():
            return True

    return False


data = ["23232anc", "234", "433", "ldkfj", "dkjfd23", "fedkdf", "dflfdfk1"]

for s in filter(has_digit, data):
    print(s)

for s in filter(str.isdigit, data):
    print(s)