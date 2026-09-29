#Practice 4
students = {}

number = int(input("Enter number of students: "))

for i in range(number):
    print("\nStudents", i + 1)

    name = input("Enter Students Name: ")

    grade1 = float(input("Enter Grade 1: "))
    grade2 = float(input("Enter Grade 2: "))
    grade3 = float(input("Enter Grade 3: "))

    students[name] = (grade1,grade2,grade3)

print("\n========Student Records===========")

for name , grades in students.items():
    average = sum(grades) / len(grades)

    print(name, *grades, "Average:", round(average,2))

highest = 0
namehighest = ""
tally = 0

for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "Average:" , f"{average: 0f}")
    if average > highest:
        highest = average
        namehighest = name
    for g in grade:
        if g < 75:
            tally = tally + 1

print(f"Students{namehighest} got the highest average: {highest:.2f}")
print(f"There are {tally} grades which are below 75. ")