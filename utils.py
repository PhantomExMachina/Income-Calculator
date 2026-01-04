"""
utils.py

Contains varies helper and utility functions
"""

from settings_handler import *
from mappings import *

# position_type, filing_status, pay_cycle = handle()

def get_pay_and_hours():
    rate_of_pay = input("How much do you make per hour?\n>: ")
    hours_worked = input("How many hours did you work this week?\n>: ")

    return float(rate_of_pay), float(hours_worked)

def get_annual_paycheck_count():
    contents = get_contents()
    settings = parse_settings(contents)
    cycle = settings.get("pay_cycle")
    annual_paychecks = pay_cycle_map.get(cycle)

    return annual_paychecks

def calculate_annual_base(rate_of_pay):
    return rate_of_pay * 2080

def calculate_weekly_base(annual_pay):
    return annual_pay / 52

def calculate_paycheck_base(annual_pay, annual_paychecks):
    return annual_pay / annual_paychecks

def calculate_weekly_gross(rate_of_pay, hours_worked):
    contents = get_contents()
    settings = parse_settings(contents)

    if settings.get("position_type") == "hourly":
        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            weekly_income = (rate_of_pay * overtime_hours * 1.5) + (rate_of_pay * 40)
        else:
            weekly_income = rate_of_pay * hours_worked
        
        return weekly_income

    elif settings.get("position_type") == "salary" or settings.get("position_type") == "contract":
        weekly_income = hours_worked * rate_of_pay

        return weekly_income
    
def calculate_annualized_gross(weekly_income):
    return weekly_income * 52

def get_all_values(rate_of_pay, hours_worked):
    annual_paychecks = get_annual_paycheck_count()
    weekly_income = calculate_weekly_gross(rate_of_pay, hours_worked)
    contractual_annual_pay = calculate_annual_base(rate_of_pay)
    contractual_weekly_pay = calculate_weekly_base(contractual_annual_pay)
    paycheck_base = calculate_paycheck_base(contractual_annual_pay, annual_paychecks)

    return weekly_income, contractual_weekly_pay, contractual_annual_pay, annual_paychecks, paycheck_base

def annualized_net():
    pass

def populate_settings():
    pass