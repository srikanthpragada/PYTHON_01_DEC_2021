names = ['Python', 'Java', 'C#', 'JavaScript']
vers = ['3.10', '17', '10']

for idx, name in enumerate(names):
    if idx >= len(vers):
        v = "Unknown"
    else:
        v = vers[idx]

    print(f"{name:15} {v}")
