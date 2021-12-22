nums = [10, 11, -13, 46, -66, 70]

for n in filter(lambda n : n % 2 == 0, nums):
    print(n)

for n in filter(lambda n : n > 0, nums):
    print(n)
