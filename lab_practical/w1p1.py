roll_num = input("Enter your roll number: ")
student_name = input("Enter your name: ")
student_age = int(input("Enter your age: "))

print("\n--- Enter your marks out of 100 ---")
python = float(input("Python marks: "))
cyber = float(input("Cyber Security marks: "))
bigdata = float(input("Big Data marks: "))

total_score = python + cyber + bigdata
percent = (total_score / 300) * 100

if python >= 40 and cyber >= 40 and bigdata >= 40:
    status = "PASSED"
else:
    status = "FAILED"

print("\n----- Student Result -----")
print(f"Roll Number  : {roll_num}")
print(f"Student Name : {student_name}")
print(f"Age          : {student_age}")
print(f"Marks (P/C/B): {python}, {cyber}, {bigdata}")
print(f"Total Marks  : {total_score} / 300")
print(f"Percentage   : {percent:.2f}%")
print(f"Pass Status  : {status}")