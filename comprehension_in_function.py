# Using list comprehension inside a function

students = [
    {"name": "Amit", "age": 27, "course": "CA-Intermediate"},
    {"name": "Rahul", "age": 23, "course": "B.Com"},
    {"name": "Sneha", "age": 26, "course": "MBA"},
    {"name": "Priya", "age": 22, "course": "BBA"}
]

def get_students_above_age(students, min_age):
    """
    Returns a list of students whose age is greater than min_age
    """
    return [
        student
        for student in students
        if student["age"] > min_age
    ]


result = get_students_above_age(students, 24)

for student in result:
    print(student["name"], "-", student["course"])
