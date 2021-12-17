# keyword-only parameters
def wish(*, message, name):
    print(message, name)


# wish("Van", "Hi")
wish(name="James", message="Good Morning")
wish(message="Hello", name="James")
