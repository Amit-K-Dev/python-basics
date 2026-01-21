# Returning multiple values from a function

students = [
    {"name": "Amit", "marks": 85},
    {"name": "Rahul", "marks": 40},
    {"name": "Sneha", "marks": 72},
    {"name": "Priya", "marks": 30}
]

def get_student_stats(students, passing_marks):
    passed = []
    failed = []

    for student in students:
        if student["marks"] >= passing_marks:
            passed.append(student["name"])
        else:
            failed.append(student["name"])

    return passed, failed


passed_students, failed_students = get_student_stats(students, 50)

print("Passed students:", passed_students)
print("Failed students:", failed_students)