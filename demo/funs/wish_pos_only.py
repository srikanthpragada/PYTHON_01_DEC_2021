# Positional-only parameters
def wish(name, message, /):
    print(message, name)


wish("Van", "Hi")
# wish(name="James", message="Good Morning")
