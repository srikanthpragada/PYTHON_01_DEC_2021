def details(**kwargs):
    print(type(kwargs), kwargs)


def fun(*args, **kwargs):
    pass


fun(10, 20, x=10, y=20)

details(a=10, b=20, c=100)
details(x="abc", y="bbc")
# details(10, 20)
