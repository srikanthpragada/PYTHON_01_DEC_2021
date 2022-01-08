import os

entries = os.walk(r"d:\classroom\dec1\demo")
count = 0
for dirname, dirs, files in entries:
    for file in files:
        if file.endswith(".py"):
            print(dirname + "\\" + file)
            count += 1

print("Count = ", count)