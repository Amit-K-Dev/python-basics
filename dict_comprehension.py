# Python Dictionary Comprehension Practice

students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 40},
    {"name": "Sneha", "marks": 72}
]

# Create a dictionary of student name -> marks
student_scores = {
    student["name"]: student["marks"]
    for student in students
}

print(student_scores)

# Dictionary with only passing students
passing_scores = {
    student["name"]: student["marks"]
    for student in students
    if student["marks"] >= 50
}

print(passing_scores)

