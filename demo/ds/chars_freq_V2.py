st = "This is to test"
chars = {}
for c in sorted(set(st)):
    chars[c] = st.count(c)

print(chars)
