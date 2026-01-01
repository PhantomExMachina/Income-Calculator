"""
Income Calculator
By Matthew Monroe (GhostExMachina)
"""

from file_handler import *
from utils import *

rate_of_pay, hours_worked = request_info()
weekly_income = calculate_weekly_gross(rate_of_pay, hours_worked)

print(f"Gross income this week: ${weekly_income}")

# Planned structure:


# handle()
# rate of pay
# hours worked
# federal income taxes
# state income taxes
# 401K
# ESPP
# holiday pay
# 




