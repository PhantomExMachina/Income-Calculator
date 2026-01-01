"""
utils.py

Contains varies helper and utility functions
"""

from file_handler import *

position_type, filing_status, pay_cycle = handle()

def request_info():
    rate_of_pay = input("How much do you make per hour?\n>: ")
    hours_worked = input("How many hours did you work this week?\n>: ")

    return rate_of_pay, hours_worked


def calculate_weekly_gross(rate_of_pay, hours_worked):
    if position_type == "hourly":
        if int(hours_worked) > 40:
            overtime_hours = int(hours_worked) - 40
            weekly_income = (int(rate_of_pay) * overtime_hours * 1.5) + (int(rate_of_pay) * 40)
        else:
            weekly_income = int(rate_of_pay) * int(hours_worked)
        
        return weekly_income

    elif position_type == "salary" or position_type == "contractor":
        weekly_income = int(hours_worked) * int(rate_of_pay)

        return weekly_income
        