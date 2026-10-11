# Student Result System

students = [
    {"name": "Alice", "marks": [80, 75, 90]},
    {"name": "Bob", "marks": [70, 85, 78]},
    {"name": "Charlie", "marks": [88, 92]},  # Missing mark
    {"name": "David", "marks": [65, 72, 68]},
    {"name": "Eva", "marks": [95, 89, 93]}
]

def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks):
    return sum(marks) / 3

try:
    name = input("Enter student name: ")

    student = next(s for s in students if s["name"].lower() == name.lower())

    if len(student["marks"]) < 3:
        print("Error: Subject mark is missing.")
    else:
        total = calculate_total(student["marks"])
        percentage = calculate_percentage(student["marks"])

        print("Total Marks:", total)
        print("Percentage:", percentage)

except StopIteration:
    print("Student does not exist")
    