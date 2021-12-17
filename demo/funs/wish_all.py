def wish(*names, message="Hello"):
    for n in names:
        print(f"{message} {n}")


wish("Van", "Larry", "Scott", message="Hi")
wish("Bill", "Bob")
