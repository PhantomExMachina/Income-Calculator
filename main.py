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

hours_worked = get_hours_worked()
hourly_pay = settings.get("rate_of_pay"); hourly_pay = float(hourly_pay)
weekly_income, weekly_pay, annual_pay, annual_paychecks, paycheck_base = get_all_values(hourly_pay, hours_worked)

net_pay = calculate_net_pay(settings, annual_pay, annual_paychecks, hours_worked)

print(f"Hourly income: ${hourly_pay}")
print(f"Annual base gross income: ${annual_pay}")
print(f"Weekly base gross income: ${weekly_pay}")
print(f"Paycheck base gross income: ${paycheck_base}")
print(f"Take home pay: ${net_pay}")

print(f"Gross income this week: ${weekly_income}")


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