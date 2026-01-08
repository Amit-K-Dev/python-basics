# Python Dictionaries Practice

# Creating a dictionary
student = {
    "name": "Amit",
    "age": 27,
    "course": "CA-Intermediate"
}

# Accessing values
print(student["name"])
print(student["age"])

# Updating a value
student["age"] = 28
print(student)

# Adding a new key-value pair
student["city"] = "Mumbai"
print(student)

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)