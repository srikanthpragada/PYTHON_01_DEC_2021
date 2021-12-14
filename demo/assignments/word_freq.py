st = "How are you today and how were you yesterday"

words = st.split(" ")
usedwords = []
for w in words:
    if w not in usedwords:
        print( f"{w:10}  {words.count(w)}")
        usedwords.append(w)


