
evens = []
odds = []

while True:
    n = int(input("Enter number [0 to stop] :"))
    if n == 0:
        break

    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

# evens.sort()
# odds.sort()

for n in sorted(evens) + sorted(odds):
    print(n)