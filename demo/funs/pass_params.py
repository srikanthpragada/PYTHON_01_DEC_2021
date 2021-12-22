def increment(n):
    print(id(n))
    n += 1


a = 100
print(id(a))
increment(a)
print(a)
