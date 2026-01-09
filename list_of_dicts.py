# List of Dictionaries Practice

# Each dictionary represents one student
students = [
    {"name": "Amit", "age": 27, "course": "CA-Intermediate"},
    {"name": "Rahul", "age": 25, "course": "B.Com"},
    {"name": "Sneha", "age": 26, "course": "MBA"}
]

# Loop through list of dictionaries
for student in students:
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Course:", student["course"])
    print("-----")