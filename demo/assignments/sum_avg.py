st = "89,45,55,67,78"

total = 0
count = 0
for n in st.split(","):
    total += int(n)
    count += 1

print(f"Total = {total}, Average = {total // count}")
