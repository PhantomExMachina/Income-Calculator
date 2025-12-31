"""
Unnamed app0
Version 0.0.1
By Matthew Monroe (GhostExMachina)
"""

income = input("How much do you make per hour?\n>: ")
hours_worked = input("How many hours did you work this week?\n>: ")

weekly_income = int(income) * int(hours_worked)
print(f"Gross income this week: ${weekly_income}")