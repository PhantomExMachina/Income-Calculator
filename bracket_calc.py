"""
bracket_calc.py

This script is intended to house the logic behind calculating withheld funds based on gross annualized pay-cycle income.
This script will NOT handle state level income taxes.
"""

import json

def withheld_funds(annualized_income):
    with open("brackets.json", 'r', encoding='utf-8') as brackets:
        data = json.load(brackets)