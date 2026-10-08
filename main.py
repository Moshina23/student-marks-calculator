# Student Marks Calculator

name = input("Enter student name: ")

mark1 = int(input("Enter mark for Python: "))
mark2 = int(input("Enter mark for SQL: "))
mark3 = int(input("Enter mark for Computer Science: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n----- Student Result -----")
print("Name:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)