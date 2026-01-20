# Filtering students using list comprehension

students = [
    {"name": "Amit", "age": 27, "course": "CA-Intermediate"},
    {"name": "Rahul", "age": 23, "course": "B.Com"},
    {"name": "Sneha", "age": 26, "course": "MBA"}
]

def filter_students_by_age(students, min_age):
    return [student for student in students if student["age"] > min_age]


result = filter_students_by_age(students, 25)

for student in result:
    print(student["name"], "-", student["course"])