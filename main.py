"""
Unnamed app
Version 0.1.0
By Matthew Monroe (GhostExMachina)
"""

with open("settings.txt", 'a+') as f:
    f.seek(0)
    contents = f.read()
    if "Position_type:" not in contents:
        position_type = input("What kind of employee are you? (Select one of the following)\n\nA: Hourly\nB: Salary\nC: Contractor\n\n>: ")
        if position_type.lower() == "a":
            position_type = "Hourly"
        elif position_type.lower() == "b":
            position_type = "Salary"
        elif position_type.lower() == "c":
            position_type == "Contractor"
        f.write(f"Position_type: {position_type}")
    else:
        if "Hourly" in contents:
            position_type = "Hourly"
        elif "Salary" in contents:
            position_type = "Salary"
        elif "Contractor" in contents:
            position_type = "Contractor"

rate_of_pay = input("How much do you make per hour?\n>: ")
hours_worked = input("How many hours did you work this week?\n>: ")

if position_type == "Hourly":
    if int(hours_worked) > 40:
        overtime_hours = int(hours_worked) - 40
        weekly_income = (int(rate_of_pay) * overtime_hours * 1.5) + (int(rate_of_pay) * 40)
    else:
        weekly_income = int(rate_of_pay) * int(hours_worked)
    
    print(f"Gross income this week: ${weekly_income}")

elif position_type == "Salary" or position_type == "Contractor":
    weekly_income = int(hours_worked) * int(rate_of_pay)

    print(f"Gross weekly income: {weekly_income}")