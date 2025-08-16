# Take input
num_subjects = int(input("Enter number of subjects: "))

marks = {}  # dictionary to store subject: mark
for i in range(num_subjects):
    subject = input(f"Enter subject {i+1} name: ")
    score = int(input(f"Enter marks for {subject}: "))
    marks[subject] = score

# Processing
total = sum(marks.values())
percentage = total / (num_subjects * 100) * 100

# Grade calculation
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

# Output
print("\n📊 Student Result 📊")
print("Subjects & Marks:", marks)
print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
