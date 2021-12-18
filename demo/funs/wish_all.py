def wish(*names, message="Hello"):
    for n in names:
        print(f"{message} {n}")


def greet(message, *names):
    for n in names:
        print(f"{message} {n}")


greet("Hello", "Jack", "Mark")

wish("Van", "Larry", "Scott", message="Hi")
wish("Bill", "Bob")
