# Filtering students using a function

students = [
    {"name": "Amit", "age": 27, "course": "CA-Intermediate"},
    {"name": "Rahul", "age": 23, "course": "B.Com"},
    {"name": "Sneha", "age": 26, "course": "MBA"}
]

def filter_students_by_age(students, min_age):
    """
    Returns students whose age is greater than min_age
    """
    filtered_students = []

    for student in students:
        if student["age"] > min_age:
            filtered_students.append(student)

    return filtered_students


# Function call
result = filter_students_by_age(students, 25)

for student in result:
    print(student["name"], "-", student["course"])