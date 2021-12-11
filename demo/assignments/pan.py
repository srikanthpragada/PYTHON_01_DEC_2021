
st = "ABCEE1234"

if len(st) != 10:
    print("Invalid PAN")
elif st[:5].isalpha() and st[-1].isalpha() and st[5:9].isdigit():
    print("Valid PAN")
else:
    print("Invalid PAN")


