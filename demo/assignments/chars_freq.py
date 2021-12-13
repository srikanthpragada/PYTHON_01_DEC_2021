st = "This is to test"

chars = []
for c in st:
    if c not in chars:
       print(f"{c} occurs {st.count(c)} time(s)")
       chars.append(c)




