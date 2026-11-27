
def analyze_marks(marks):
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)
    return average, highest, lowest
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
students = [
    {"name": "Anu", "marks": [95, 90, 92]},
    {"name": "Priya", "marks": [85, 88, 90]},
    {"name": "Ravi", "marks": [65, 70, 60]},
    {"name": "Kavi", "marks": [45, 50, 40]}
]
print("=" * 45)
print("       GRADEVISION ANALYZER")
print("=" * 45)
for student in students:
    marks = student["marks"]
    average, highest, lowest = analyze_marks(marks)
    grade = calculate_grade(average)
    status = "PASS" if all(mark >= 35 for mark in marks) else "FAIL"
    print(f"\nStudent Name : {student['name']}")
    print(f"Marks        : {marks}")
    print(f"Average      : {average:.2f}")
    print(f"Highest      : {highest}")
    print(f"Lowest       : {lowest}")
    print(f"Grade        : {grade}")
    print(f"Result       : {status}")
topper = max(students, key=lambda s: sum(s["marks"]) / len(s["marks"]))
print("\n" + "=" * 45)
print("          CLASS PERFORMANCE")
print("=" * 45)
print(f"Total Students : {len(students)}")
print(f"Class Topper   : {topper['name']}")
all_marks = [mark for student in students for mark in student["marks"]]
print(f"Class Average  : {sum(all_marks) / len(all_marks):.2f}")
print(f"Highest Mark   : {max(all_marks)}")
print(f"Lowest Mark    : {min(all_marks)}")
print("\nThank you for using GradeVision!")
