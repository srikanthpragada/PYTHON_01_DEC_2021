def numbers():
    for v in range(1, 6):
        yield v


g = numbers()
print(next(g))
print(next(g))

for v in g:
    print(v)

print(type(g))
