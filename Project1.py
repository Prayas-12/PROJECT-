#STUDENT GRADE CALCULATOR
print("----- STUDENT GRADE CALCULATOR -----")

# taking inputs
name = input("Enter student name: ")

print("\nEnter marks for 5 subjects:")
phy = int(input("Physics: "))
chem = int(input("Chemistry: "))
math = int(input("Maths: "))
eng = int(input("English: "))
comp = int(input("Computer: "))

# store data inside a dictionary
student = {
    "Name": name,
    "Marks": [phy, chem, math, eng, comp]
}

# calculate total and percentage
total = phy + chem + math + eng + comp
percentage = total / 5

# determining grade using conditions
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F (Fail)"

# printing report card
print("\n----- REPORT CARD -----")
print("Student Name:", student["Name"])
print("Marks:", student["Marks"])
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("------------------------")
