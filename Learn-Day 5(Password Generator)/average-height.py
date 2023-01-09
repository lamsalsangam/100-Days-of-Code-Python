student_heights = input("Input a list of student heights.\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

count = 0
sum = 0
for k in student_heights:
    sum += k
    count += 1

average = sum/count
# print("%.0f" %average)
print(round(average))
