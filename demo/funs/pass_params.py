def increment(n):
    print(id(n))
    n += 1
    print(id(n))


a = 100
print(id(a))
increment(a)
print(a)


def prepend(lst, value):
    lst.insert(0, value)


l = [1, 2, 3]
prepend(l, 5)
print(l)
