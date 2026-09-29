

classrecord = {"Liza": {"StudID" : "5001",
                "Grade": [90,85,86,82,83,90,92]
                },
               "Jeremy": {"StudID" : "5002",
               "Grade": [72,75,69,80,84,75,85]
                }
               }
search = input("Enter student name to search: ").title()

if search in classrecord:
    print("\nStudent Found!")
    print("\nStudent Name: ",search)
    print("StudentID: ",classrecord[search]["StudID"])

    grades = classrecord[search]["Grade"]

    print("Grades: ",grades)

    average = sum(grades) / len(grades)
    print("Average: ",round(average,2))

    if min(grades) < 60:
        print("Candidate for Intervention")
    else:
        print("No Intervention Needed.")


    print("Highest Grade:", max(grades))
    print("Lowest Grade:", min(grades))

else:
    print("\nNo Student Found.")





