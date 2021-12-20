def isodd(n: int) -> bool:
    return n % 2 == 1


def ispositive(n: int) -> bool:
    return n > 0


nums = [10, 11, -13, 46, -66, 70]

for n in filter(isodd, nums):
    print(n)

for n in filter(ispositive, nums):
    print(n)
