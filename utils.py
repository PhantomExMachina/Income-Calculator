"""
utils.py

Contains varies helper and utility functions
"""

from settings_handler import *
from mappings import *

def get_hours_worked():
    hours_worked = input("How many hours did you work this week?\n>: ")

    return float(hours_worked)

def get_annual_paycheck_count():
    contents = get_contents()
    settings = parse_settings(contents)
    cycle = settings.get("pay_cycle")
    annual_paychecks = pay_cycle_map.get(cycle)

    return annual_paychecks

def calculate_annual_base(hourly_pay):
    return hourly_pay * 2080

def calculate_weekly_base(annual_pay):
    return annual_pay / 52

def calculate_paycheck_base(annual_pay, annual_paychecks):
    return float(annual_pay) / annual_paychecks

def calculate_weekly_gross(hourly_pay, hours_worked):
    contents = get_contents()
    settings = parse_settings(contents)

    if settings.get("position_type") == "hourly":
        if hours_worked > 40:
            overtime_hours = hours_worked - 40
            weekly_income = (hourly_pay * overtime_hours * 1.5) + (hourly_pay * 40)
        else:
            weekly_income = hourly_pay * hours_worked
        
        return weekly_income

    elif settings.get("position_type") == "salary" or settings.get("position_type") == "contract":
        weekly_income = hours_worked * hourly_pay

        return weekly_income
    
def calculate_annualized_gross(weekly_income):
    return weekly_income * 52

def get_all_values(hourly_pay, hours_worked):
    annual_paychecks = get_annual_paycheck_count()
    weekly_income = calculate_weekly_gross(hourly_pay, hours_worked)
    annual_pay = calculate_annual_base(hourly_pay)
    weekly_pay = calculate_weekly_base(annual_pay)
    paycheck_base = calculate_paycheck_base(annual_pay, annual_paychecks)

    return weekly_income, weekly_pay, annual_pay, annual_paychecks, paycheck_base

def annualized_net():
    pass

# Currently only calculating take home of a pay cycle with no overtime.
def calculate_net_pay(settings, annual_pay, annual_paychecks, hours_worked): 
    hourly_pay = settings.get("rate_of_pay")
    gross_paycheck = calculate_paycheck_base(annual_pay, annual_paychecks)

    net_pay = gross_paycheck
    net_pay = net_pay - float(settings.get("insurance_premium")) if settings.get("insurance_premium") != "n/a" else net_pay - 0
    net_pay = net_pay - (gross_paycheck * (float(settings.get("401k"))))                                                                    # NOTE - Pre-tax
    net_pay = net_pay - (gross_paycheck * (float(settings.get("espp"))))                                                                    # NOTE - Post-tax
    net_pay = net_pay - float(settings.get("child_support")) if settings.get("child_support") != "n/a" else net_pay - 0
    net_pay = net_pay - float(settings.get("tuition_repayment")) if settings.get("tuition_repayment") != "n/a" else net_pay - 0

    return net_pay
