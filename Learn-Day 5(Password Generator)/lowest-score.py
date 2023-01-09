student_scores = input("Input the list of student scores:\n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

lowest_score = student_scores[0]
for score in student_scores:
    if lowest_score > score:
        lowest_score = score

print(f"The lowest score in the class is: {lowest_score}")
