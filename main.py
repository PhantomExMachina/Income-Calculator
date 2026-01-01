"""
Income Calculator
By Matthew Monroe (GhostExMachina)
"""

from file_handler import *

position_type, filing_status, pay_cycle = handle()

rate_of_pay = input("How much do you make per hour?\n>: ")
hours_worked = input("How many hours did you work this week?\n>: ")

if position_type == "hourly":
    if int(hours_worked) > 40:
        overtime_hours = int(hours_worked) - 40
        weekly_income = (int(rate_of_pay) * overtime_hours * 1.5) + (int(rate_of_pay) * 40)
    else:
        weekly_income = int(rate_of_pay) * int(hours_worked)
    
    print(f"Gross income this week: ${weekly_income}")

elif position_type == "salary" or position_type == "contractor":
    weekly_income = int(hours_worked) * int(rate_of_pay)

    print(f"Gross weekly income: {weekly_income}")

