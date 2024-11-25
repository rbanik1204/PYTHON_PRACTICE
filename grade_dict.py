# define grade of each student

student_marks: dict = {"Ram": 91, "Shyam": 70, "Mohan": 79}

for name, numbers in student_marks.items():
    if numbers >= 90:
        student_marks[name] = 'A'
    elif 90 > numbers > 80:
        student_marks[name] = 'B'
    elif 80 > numbers >= 70:
        student_marks[name] = 'C'
print(dict(reversed(list(student_marks.items()))))
