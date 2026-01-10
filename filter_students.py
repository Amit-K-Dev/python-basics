# Filtering data using conditions inside list of dictionaries

students = [
    {"name": "Amit", "age": 27, "course": "CA-Intermediate"},
    {"name": "Rahul", "age": 23, "course": "B.Com"},
    {"name": "Sneha", "age": 26, "course": "MBA"}
]

# Print students who are older than 25
for student in students:
    if student["age"] > 25:
        print(student["name"], "-", student["course"])