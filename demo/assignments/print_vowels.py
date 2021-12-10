str = input("Enter String:")
for c in str:
    if c in "aeiouAEIOU":
        print(c, end='')
