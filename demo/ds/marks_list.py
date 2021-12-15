data = ["10,66", "12,90", "15,87", "13,45", "5,89"]

students = {}
for d in data:
    rno, marks = d.split(",")
    students[int(rno)] = marks

for r, m in sorted(students.items()):
    print(r, m)
