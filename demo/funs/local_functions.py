a = 1000  # Global variable

def f1():
    global a
    v1 = 100     # Enclosing variable
    a  = a + 1

    # Local function
    def f2():
        nonlocal v1
        v2 = 200  # Local variable
        v1 = v1 + 1
        print("F2")
        print(v1, v2)

    f2()
    print(v1)
f1()