
import csv
def student_summary(filename: str) -> None:
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            total = 0
            count = 0
            print("\nSTUDENT REPORT")
            for student in reader:
                try:
                    name = student["name"]
                    marks = [
                        float(student["python"]),
                        float(student["maths"]),
                        float(student["english"])
                    ]

                    average = sum(marks) / len(marks)
                    print(f"{name} - Average: {average:.2f}")
                    total += average
                    count += 1
                except (KeyError, ValueError) as error:
                    print("Invalid student data:", error)
                    continue
            if count > 0:
                print(f"\nClass Average: {total / count:.2f}")
            else:
                print("No valid student records found.")
    except FileNotFoundError:
        print("Students CSV file not found.")
    finally:
        print("Student report process completed.")
if __name__ == "__main__":
    student_summary("students.csv")
