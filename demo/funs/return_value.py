def max(a, b):
    return a if a > b else b


def isprime(n: int) -> bool:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False

    return True


big = max(10, 20)
print(isprime(17), isprime(255))
