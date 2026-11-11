import random
import csv

departments = ["Computer Science", "Accounting", "Economics", "Microbiology"]
levels = [100, 200, 300, 400]

students = []

for i in range(5):
    student_id = input("Enter your Student ID: ")
    department = random.choice(departments)
    level = random.choice(levels)
    attendance = round(random.uniform(40, 100), 1)
    score = round(random.uniform(30, 95), 1)

    students.append([student_id, department, level, attendance, score])

    print(f"""
Student ID: {student_id}
Department: {department}
Level: {level}
Attendance: {attendance}%
Score: {score}
""")

with open("student_dataset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Student_ID", "Department", "Level", "Attendance_Percentage", "Average_Score"])
    writer.writerows(students)

print(f"Saved {len(students)}, students to student_dataset.csv")