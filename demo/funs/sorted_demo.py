def extract_number(s):
    return int(s[1:])


nums = [-10, 10, 9, 8, -4, -5]
codes = ['A123', 'B234', 'A99', 'X223', 'B323']

for n in sorted(nums, key=abs):
    print(n)

for n in sorted(codes, key=extract_number):
    print(n)
