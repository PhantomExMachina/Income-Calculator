"""
Income Calculator
By Matthew Monroe (GhostExMachina)
"""

from settings_handler import *
from utils import *

# Settings.txt control flow
# -------------------------
contents = create_settings()
settings = parse_settings(contents)
settings = solve_undefined(settings)
write_settings(settings)
# -------------------------

rate_of_pay, hours_worked = get_pay_and_hours()
weekly_income, contractual_weekly_pay, contractual_annual_pay, annual_paychecks, paycheck_base = get_all_values(rate_of_pay, hours_worked)

print(f"Annual base gross income: ${contractual_annual_pay}")
print(f"Weekly base gross income: ${contractual_weekly_pay}")
print(f"Paycheck base gross income: ${paycheck_base}")

print(f"Gross income this week: ${weekly_income}")
print(f"Net income this week: ${None}")


print(f"Gross annualized income base on this week: {calculate_annualized_gross(weekly_income)}")


print(f"Paycheck count per year: {get_annual_paycheck_count()}")

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