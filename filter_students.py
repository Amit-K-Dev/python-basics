# Filtering students using a function

students = [
    {"name": "Amit", "age": 27, "course": "CA-Intermediate"},
    {"name": "Rahul", "age": 23, "course": "B.Com"},
    {"name": "Sneha", "age": 26, "course": "MBA"}
]

def filter_students_by_age(students, min_age):
    """
    Prints students whose age is greater than min_age
    """
    for student in students:
        if student["age"] > min_age:
            print(student["name"], "-", student["course"])

# Function call
filter_students_by_age(students, 25)