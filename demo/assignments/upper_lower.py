def extract_alpha(s):
    alpha = []
    for c in s:
        if c.isalpha():
            alpha.append(c)

    return "".join(alpha)


names = []

while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break

    names.append(name)

for n in map(extract_alpha, names):
    print(n)
