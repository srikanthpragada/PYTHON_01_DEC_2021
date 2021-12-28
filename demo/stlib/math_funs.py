def iseven(n):
    return n % 2 == 0


def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

print(__name__)
if __name__ == '__main__':   # execute when run as script
    print(iseven(10))
    print(sign(-10), sign(10))
