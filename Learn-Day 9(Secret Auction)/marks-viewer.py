student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}
name = input("What is your name?\n").capitalize()
marks = int(input("What is the marks you have scored?\n"))
student_scores[name] = marks

student_grades = {}

for key in student_scores:
    if 90 < student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif 80 < student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif 70 < student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

for key in student_grades:
    print(key)
    print(f"{student_grades[key]}\n")
