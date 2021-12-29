def iseven(n):
    """
    Returns true if the given number is even otherwise false

    param n : number to test
    return  : true or false
    """
    return n % 2 == 0


def sign(n):
    """
       Returns the sign of the given number.

       param n : number to test
       return  : 0 for 0, 1 for positive, -1 for negative
    """
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


print(__name__)
if __name__ == '__main__':  # execute when run as script
    print(iseven(10))
    print(sign(-10), sign(10))
