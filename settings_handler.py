"""
file_handler.py

This file looks for, reads from, and updates the settings.txt file as needed.
"""

EXPECTED_STRUCTURE = {
    "position_type": lambda s: position_type(s),
    "filing_status": lambda s: filing_status(s),
    "pay_cycle": lambda s: pay_cycle(s),
    "401k": lambda s: _401k(s),
    "share_program": lambda s: share_program(s),
    "insurance_frequency": lambda s: insurance_frequency(s),
    "insurance_premium": lambda s: insurance_premium(s),
    "insurance_tax": lambda s: insurance_tax(s)
}

def get_contents(file="settings.txt"):
    try:
        with open(file, 'r') as f:
            contents = f.read()
            return contents
    except FileNotFoundError:
        with open(file, 'w+') as f:
            contents = f.read()
            return contents

def check_contents():
    contents = get_contents()
    for setting in EXPECTED_STRUCTURE:
        if setting not in contents:
            contents = contents + setting + ": \n"
    return contents

def create_settings(file="settings.txt"):
    contents = check_contents()
    with open(file, 'w') as f:
        f.write(contents)
    return contents

def parse_settings(contents):
    settings = {}

    for line in contents.splitlines():
        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        settings[key] = value if value else None
    
    return settings

def find_undefined(settings):
    return [k for k, v in settings.items() if v is None]

def solve_undefined(settings):
    undefined = find_undefined(settings)

    for key in undefined:
        handler = EXPECTED_STRUCTURE.get(key)
        if handler is None:
            continue
        settings[key] = handler(settings)  # store the return value

    return settings

def write_settings(settings, file="settings.txt"):
    """
    Rewrite settings.txt from the settings dict, in the order defined by EXPECTED_STRUCTURE.
    Missing keys get written as blank values.
    """
    lines = []
    for key in EXPECTED_STRUCTURE.keys():
        value = settings.get(key)
        lines.append(f"{key}: {'' if value is None else value}")

    # Optional: preserve unknown keys that might exist in the file already
    for key, value in settings.items():
        if key not in EXPECTED_STRUCTURE:
            lines.append(f"{key}: {'' if value is None else value}")

    with open(file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


    
# ------ settings input functions ------#

def position_type(settings):
    while True:
        answer = input("What kind of employee are you?\n\nA: Hourly\nB: Salary\nC: Contract\n\n>: ").strip().lower()
        if answer == "a" or answer == "hourly" or answer == "1":
            return "hourly"
        if answer == "b" or answer == "salary" or answer == "2":
            return "salary"
        if answer == "c" or answer == "contract" or answer == "3":
            return "contract"
        print("Invalid response.\n\n")


def filing_status(settings):
    while True:
        answer = input("What is your filing status?\n\nA: Single\nB: Married, filing jointly\nC: Head of household\n\n>: ").strip().lower()
        if answer == "a" or answer == "1" or answer == "single":
            return "single"
        if answer == "b" or answer == "2" or answer == "married" or answer == "joint" or answer == "married, filing jointly":
            return "married_filing_jointly"
        if answer == "c" or answer == "3" or answer == "head of household" or answer == "head" or answer == "hoh":
            return "head_of_household"
        print("Invalid response.\n\n")

def pay_cycle(settings):
    while True:
        answer = input("What type of pay cycle are you on?\n\nA: Weekly\nB: Bi-weekly\nC: Semi-monthly\nD: Monthly\nE: Other\n\n>: ").strip().lower()
        if answer == "a" or answer == "1" or answer == "weekly":
            return "weekly"
        if answer == "b" or answer == "2" or answer == "bi-weekly":
            return "bi_weekly"
        if answer == "c" or answer == "3" or answer == "semi-monthly":
            return "semi_monthly"
        if answer == "d" or answer == "4" or answer == "monthly":
            return "monthly"
        if answer == "e" or answer == "5" or answer == "other":
            return "other"
        print("Invalid response.\n\n")

def _401k(settings):
    while True:
        answer = input("401K: How much are you contributing per paycheck to your 401k? (Enter as a decimal, such as 0.05 for 5%, or 0.00 for no contribution)\n\n>: ").strip()
        try:
            if answer.endswith("%"):
                answer = answer.rstrip("%")
            if float(answer) > 1 and float(answer) <= 100:
                return float(answer) / 100
            if float(answer) < 0:
                print("Invalid response.\n\n")
                continue
            if float(answer) > 100:
                print("Invalid response.\n\n")
                continue
            return float(answer)
        except(ValueError):
            print("Invalid response.\n\n")


def share_program(settings):
    while True:
        answer = input("Stock Program: How much are you contributing per paycheck toward an employee stock program? (Enter as a decimal, such as 0.05 for 5%, or 0.00 for no contribution)\n\n>: ").strip()
        try:
            if answer.endswith("%"):
                answer = answer.rstrip("%")
            if float(answer) > 1 and float(answer) <= 100:
                return float(answer) / 100
            if float(answer) < 0:
                print("Invalid response.\n\n")
                continue
            if float(answer) > 100:
                print("Invalid response.\n\n")
                continue
            return float(answer)
        except(ValueError):
            print("Invalid response.\n\n")

def insurance_frequency(settings):
    while True:
        answer_1 = input("Do you pay for an employer provided health insurance premium?\n\nA: Yes\nB: No\n\n>: ").strip().lower()
        if answer_1 == "a" or answer_1 == "1" or answer_1 == "yes":
            answer_2 = input("How often is your deduction billed?\n\nA: Per pay check\nB: Monthly (If you are paid monthly, select this option)\nC: Every other paycheck\nD: Other\n\n>: ").strip().lower()
            if answer_2 == "a" or answer_2 == "1" or answer_2 == "per paycheck":
                return "per_paycheck"
            elif answer_2 == "b" or answer_2 == "2" or answer_2 == "monthly":
                return "monthly"
            elif answer_2 == "c" or answer_2 == "3" or answer_2 == "every other paycheck":
                return "every_other_paycheck"
            elif answer_2 == "d" or answer_2 == "4" or answer_2 == "other":
                return "other"
            else:
                print("invalid response")
                continue
        elif answer_1 == "b" or answer_1 == "2" or answer_1 == "no":
            return "n/a"
        else:
            print("Invalid response.")
            continue

def insurance_premium(settings):
    if settings.get("insurance_frequency") == 'n/a':
        return 'n/a'
    while True:
        try: 
            answer = input("How much is your premium?\n\n> ").strip()
            if answer.startswith("$"):
                answer = answer.lstrip("$")
            if float(answer) < 0:
                print("Invalid response.")
                continue

            return float(answer)
        except ValueError:
            print("Invalid response.")

def insurance_tax(settings):
    if settings.get("insurance_frequency") == 'n/a':
        return 'n/a'
    while True:
        answer = input("Is your insurance premium payment pre-tax or post-tax?\n\nA: Pre-tax (Most common)\nB: Post-tax\n\n>: ").strip().lower()
        if answer == "a" or answer == "1" or answer == "pre-tax" or answer == "pretax" or answer == "pre":
            return "pre_tax"
        if answer == "b" or answer == "2" or answer == "post-tax" or answer == "posttax" or answer == "post":
            return "post_tax"
        print("Invalid response.")

