marks_list = [85, 92, 78, 65, 85, 92, 54, 88, 73, 90]

marks_tuple = tuple(marks_list)

student_records = {
    "Aarav": 85,
    "Diya": 92,
    "Kabir": 78,
    "Ananya": 65,
    "Rohan": 85,
    "Isha": 92,
    "Vikram": 54,
    "Pooja": 88,
    "Kunal": 73,
    "Neha": 90,
}

highest_marks = max(marks_tuple)
lowest_marks = min(marks_tuple)
average_marks = sum(marks_tuple) / len(marks_tuple)

unique_marks = set(marks_list)

print("--- Marks Analysis ---")
print(f"Marks List          : {marks_list}")
print(f"Marks Tuple         : {marks_tuple}")
print(f"Unique Marks (Set)  : {unique_marks}")
print(f"Highest Marks       : {highest_marks}")
print(f"Lowest Marks        : {lowest_marks}")
print(f"Average Marks       : {average_marks:.2f}")

print("\n--- Students Scoring Above Average ---")
for name, score in student_records.items():
    if score > average_marks:
        print(f"{name}: {score}")
