st = "Abcde132"
if len(st) < 8:
    print("Invalid Password")
    exit(0)

upper = digit = False

for c in st:
    if c.isupper():
        upper = True
    elif c.isdigit():
        digit = True

if upper and digit:
    print("Valid Password")
else:
    print("Invalid password")
