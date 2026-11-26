subjects = ["C++", "Data Structures", "Operating Systems", "DBMS", "Software Engineering"]
students = []

print("student marks/performance ")

for i in range(10):
    print(f"\nEnter Details of Student {i + 1}")
    
    while True:
        try:
            roll = int(input("Enter Roll Number : "))
            if roll <= 0:
                print("Roll Number must be greater than 0.")
                continue
            
            duplicate_roll = False
            for s in students:
                if s["Roll"] == roll:
                    duplicate_roll = True
                    break
                    
            if duplicate_roll:
                print("Roll Number already exists.")
                continue
            break
        except ValueError:
            print("Invalid Input! Enter numbers only.")

    while True:
        name = input("Enter Name : ").strip()
        if name == "":
            print("Name cannot be empty.")
        elif not name.replace(" ", "").isalpha():
            print("Name should contain only alphabets.")
        else:
            break

    marks = []
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter Marks in {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid Input! Enter numeric value only.")

    total = sum(marks)
    percentage = total / len(subjects)

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    fail = False
    for m in marks:
        if m < 40:
            fail = True
            break

    student = {
        "Roll": roll,
        "Name": name,
        "Marks": tuple(marks),
        "Total": total,
        "Percentage": percentage,
        "Grade": grade,
        "Fail": fail
    }
    students.append(student)

print("\nSTUDENT REPORT")

for s in students:
    print("Roll Number :", s["Roll"])
    print("Name        :", s["Name"])
    print("Marks       :", s["Marks"])
    print("Total       :", s["Total"])
    print("Percentage  : {:.2f}%".format(s["Percentage"]))
    print("Grade       :", s["Grade"])
    print()

class_average = sum(student["Percentage"] for student in students) / len(students)
print("Class Average Percentage : {:.2f}%".format(class_average))

highest = max(student["Total"] for student in students)
print("\nHighest Scorer(s)")
for student in students:
    if student["Total"] == highest:
        print(student["Name"], "-", student["Total"])

lowest = min(student["Total"] for student in students)
print("\nLowest Scorer(s)")
for student in students:
    if student["Total"] == lowest:
        print(student["Name"], "-", student["Total"])

print("\nStudents Above Class Average")
found = False
for student in students:
    if student["Percentage"] > class_average:
        print(student["Name"], "-", "{:.2f}%".format(student["Percentage"]))
        found = True
if not found:
    print("No student scored above class average.")

print("\nStudents Failed in One or More Subjects")
found = False
for student in students:
    if student["Fail"]:
        print(student["Name"])
        found = True
if not found:
    print("No Student Failed.")

grade_dictionary = {}
for student in students:
    grade = student["Grade"]
    if grade not in grade_dictionary:
        grade_dictionary[grade] = []
    grade_dictionary[grade].append(student["Name"])

print("\nStudents According to Grade")
for grade in grade_dictionary:
    print(grade, ":", grade_dictionary[grade])

print("\nStudent Names in Alphabetical Order")
names = []
for student in students:
    names.append(student["Name"])
sorted_names = sorted(names)
for name in sorted_names:
    print(name)

first = -1
second = -1
for student in students:
    total = student["Total"]
    if total > first:
        second = first
        first = total
    elif total > second and total != first:
        second = total

print("\nSecond Highest Scorer(s)")
if second == -1:
    print("Second Highest Scorer Not Available")
else:
    for student in students:
        if student["Total"] == second:
            print(student["Name"], "-", second)

subject_average = []
for i in range(len(subjects)):
    total = 0
    for student in students:
        total += student["Marks"][i]
    average = total / len(students)
    subject_average.append(average)

highest_average = max(subject_average)
index = subject_average.index(highest_average)

print("\nSubject with Highest Average Marks")
print(subjects[index], "-", "{:.2f}".format(highest_average))

name_count = {}
duplicates = []
for student in students:
    name = student["Name"]
    if name in name_count:
        name_count[name] += 1
        if name not in duplicates:
            duplicates.append(name)
    else:
        name_count[name] = 1

unique_names = list(dict.fromkeys(names))
print("\nUnique Student Names")
for name in unique_names:
    print(name)

if duplicates:
    print("\nDuplicate Student Name(s) Found")
    for name in duplicates:
        print(name)
else:
    print("\nNo Duplicate Students")