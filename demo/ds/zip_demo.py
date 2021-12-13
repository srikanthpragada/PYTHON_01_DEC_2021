names = ['Python', 'Java', 'C#', 'JavaScript']
vers = ['3.10', '17', '10']

for n, v in zip(names, vers, strict = True):
    print(f"{n} {v}")
