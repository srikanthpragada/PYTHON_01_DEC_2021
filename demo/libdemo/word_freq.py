import re

f = open(r"..\..\old_man.txt","rt")
content = f.read()
f.close()

words = re.findall(r"\w+",content)

word_freq = {}
for w in set(words):
    word_freq[w] = words.count(w)

for w, c in sorted(word_freq.items()):
    print(f"{w:20}  {c:3}")


