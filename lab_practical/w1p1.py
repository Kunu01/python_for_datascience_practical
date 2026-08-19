roll_no = 250160450323
name = "Kunal Teli"
age = 23

marks_python = 85
marks_cyber = 78
marks_bigdata = 90

total_marks = marks_python + marks_cyber + marks_bigdata
percentage = (total_marks / 300) * 100

passed_python = marks_python >= 40
passed_cyber = marks_cyber >= 40
passed_bigdata = marks_bigdata >= 40

overall_pass = passed_python and passed_cyber and passed_bigdata

print("----- Student Result-----")
print(f"Roll Number  : {roll_no}")
print(f"Student Name : {name}")
print(f"Age          : {age}")
print(f"Marks (P/C/B): {marks_python}, {marks_cyber}, {marks_bigdata}")
print(f"Total Marks  : {total_marks} / 300")
print(f"Percentage   : {percentage:.2f}%")
print(f"Pass Status  : {'PASSED' if overall_pass else 'FAILED'}")