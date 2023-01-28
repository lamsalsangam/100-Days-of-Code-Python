import pandas
student_dict = {
    "student": ["Enjisha", "James", "Lily"],
    "score": [56, 76, 98]
}


# Looping through the dictionaries
for (key, value) in student_dict.items():
    print(key, value)


student_data_frames = pandas.DataFrame(student_dict)
print(student_data_frames)


# Looop through the data frame
# for (key, value) in student_data_frames.items():
#     print(key)
#     print(value)


# pandas inbuilt loop
for (index, row) in student_data_frames.iterrows():
    print(row.student)
    if row.student == "Enjisha":
        (row.score)
