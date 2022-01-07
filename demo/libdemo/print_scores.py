f = open("scores.txt", "rt")

for line in f.readlines():
    parts = line.split(",")
    if len(parts) < 2:
        continue

    name = parts[0]
    total = sum(map(int, parts[1:]))
    print(f"{name:20} {total:4}")

f.close()
