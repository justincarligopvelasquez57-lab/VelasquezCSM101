while True:
    velasquezname = input("Enter Your Name: ").title()
    velasquezposition = input("Enter Your Position: (Janitor, Clerk, Cashier, Manager): ").title()
    velasquez_hours = float(input("Actual Hours Worked: "))

    match velasquezposition.lower():
        case "janitor":
          velasquez_monthly = 18000
        case "clerk":
          velasquez_monthly = 22000
        case "cashier":
          velasquez_monthly = 24000
        case "manager":
          velasquez_monthly = 40000
        case _:
          print(f"\033[31mInvalid job position\033[0m")
          continue


    velasquez_bms = velasquez_monthly / 2
    velasquez_hr = velasquez_bms / 88

    velasquez_absent_hours = 0
    velasquez_absence_deduction = 0
    velasquez_overtime_hours = 0
    velasquez_overtime_rate = 0
    velasquez_overtime_pay = 0

    if velasquez_hours < 88:
        velasquez_absent_hours = 88 - velasquez_hours
        velasquez_absence_deduction = velasquez_absent_hours * velasquez_hr
    elif velasquez_hours > 88:

        velasquez_overtime_hours = velasquez_hours - 88
        velasquez_overtime_rate = velasquez_hr * 1.25
    else:

        velasquez_absent_hours = 0
        velasquez_overtime_hours = 0

        velasquez_net_salary = (velasquez_bms
        -velasquez_absence_deduction
        + velasquez_overtime_pay
        )

        print("==================(PAYROLL)=======================")
        print(f"Employee Name:      \033[33m{velasquezname}\033[0m")
        print(f"Job Position:        \033[35m{velasquezposition}\033[0m")
        print(f"Actual Hours Worked: \033[32m{velasquez_hours:.2f}\033[0m")
        print(f"Monthly Salary:      \033[32m{velasquez_monthly:,.2f}\033[0m")
        print(f"Basic Half-Month:    \033[32m{velasquez_bms:,.2f}\033[0m")
        print(f"Hourly Rate:        \033[32m {velasquez_hr:,.2f}\033[0m")

    if velasquez_hours < 88 :
           print(f"Absent Hours:          \033[32m{velasquez_absent_hours:.2f}\033[0m")
           print(f"Absence Deduction:   \033[32m{velasquez_absence_deduction:.2f}\033[0m")
           print(f"Overtime Hours:      \033[32m{0.00}\033[0m ")
           print(f"Overtime Pay:        \033[32m{0.00}\033[0m ")

    elif velasquez_hours > 88 :
           print(f"Absent Hours:        0.00")
           print(f"Absence Deduction:   0.00")
           print(f"Overtime Hours:      \033[32m{velasquez_overtime_hours:.2f}\033[0m")
           print(f"Overtime Rate:       \033[32m{velasquez_overtime_rate:,.2f}\033[0m")
           print(f"Overtime Pay:        {velasquez_overtime_pay:,.2f}")
    else:
           print("Absent Hours:        0.00")
           print("Absence Deduction:   0.00")
           print("Overtime Hours:      0.00")
           print("Overtime Pay:        0.00")

           print("\n===============================================")
           print(f"NET HALF-MONTH SALARY: \033[34m{velasquez_net_salary:,.2f}\033[0m")
           print("\n===============================================")
           again = input("Do you want to enter again?:  (Y/N)")

           if again.upper() != "N":
              print("Thank You")
              break















