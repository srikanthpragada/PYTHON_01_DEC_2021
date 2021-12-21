def extract_digits(s):
    digits = []
    for c in s:
        if c.isdigit():
            digits.append(c)

    return "".join(digits)

data = ['anc', 'kdkd', 'ldkdkdkdd', 'll']

values = ['a344nc', 'kdkd32', '334ldk333dkdkdd', 'll32']
for l in map(extract_digits, values):
    print(l)
