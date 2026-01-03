"""
Income Calculator
By Matthew Monroe (GhostExMachina)
"""

from settings_handler import *
from utils import *

contents = create_settings()
settings = parse_settings(contents)
settings = solve_undefined(settings)
write_settings(settings)


rate_of_pay, hours_worked = request_info()
weekly_income = calculate_weekly_gross(rate_of_pay, hours_worked)

print(f"Gross income this week: ${weekly_income}")
print(f"Net income this week: ${None}")


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




