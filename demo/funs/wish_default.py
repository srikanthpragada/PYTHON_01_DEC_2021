def wish(name="Guest", message="Hello"):
    print(message, name)


wish("Van", "Hi")  # Positional args
wish("Larry")
wish(message="Hello", name="James")  # Keyword args
wish(name="Scott")
wish(message="Hi")
wish()
