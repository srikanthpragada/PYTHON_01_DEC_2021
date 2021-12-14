names = ['Python', 'Java', 'C#', 'JavaScript']
vers = ['3.10', '17', '10', "2019", "1.0"]

if len(names) > len(vers):
    f = names
    s = vers
else:
    f = vers
    s = names

for idx, v1 in enumerate(f):
    if idx >= len(s):
        v2 = "Unknown"
    else:
        v2 = s[idx]

    print(f"{v1:15} {v2}")
