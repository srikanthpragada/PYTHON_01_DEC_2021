def wish(name: str, message: str):
    print(message, name)


wish("Van", "Hi")  # Positional args
wish(message="Hello", name="James")  # Keyword args
#wish(name = "Larry")
