def isprime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


data = [13, 45, 56, 89, 789, 35]

for n in filter(isprime, data):
    print(n)
