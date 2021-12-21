st = "89,45,55,67,abc,78"

marks_st = list(filter(str.isdigit,  st.split(",")))
marks = map(int,marks_st)
total = sum(marks)

print(f"Total = {total}, Average = {total // len(marks_st)}")
