"""
file_handler.py

This file looks for, reads from, and updates the settings.txt file as needed.
"""



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
        settings[key] = handler()  # store the return value

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

def position_type():
    while True:
        answer = input("What kind of employee are you?\n\nA: Hourly\nB: Salary\nC: Contract\n\n>: ").strip().lower()
        if answer == "a" or answer == "hourly" or answer == "1":
            return "hourly"
        if answer == "b" or answer == "salary" or answer == "2":
            return "salary"
        if answer == "c" or answer == "contract" or answer == "3":
            return "contract"
        print("Invalid response.\n\n")


def filing_status():
    while True:
        answer = input("What is your filing status?\n\nA: Single\nB: Married, filing jointly\nC: Head of household\n\n>: ").strip().lower()
        if answer == "a" or answer == "1" or answer == "single":
            return "single"
        if answer == "b" or answer == "2" or answer == "married" or answer == "joint" or answer == "married, filing jointly":
            return "married_filing_jointly"
        if answer == "c" or answer == "3" or answer == "head of household" or answer == "head" or answer == "hoh":
            return "head_of_household"
        print("Invalid response.\n\n")

def pay_cycle():
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

def _401k():
    while True:
        answer = input("How much are you contributing (percentage, not dollar-ammount) per paycheck to your 401k? (Enter as a decimal, such as 0.05 for 5%, or 0.00 for no contribution)\n\n>: ").strip().lower()
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


def share_program():
    while True:
        answer = input("How much are you contributing per paycheck toward an employee stock program? (Enter as a decimal, such as 0.05 for 5%, or 0.00 for no contribution)\n\n>: ").strip().lower()
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

EXPECTED_STRUCTURE = {
    "position_type": position_type,
    "filing_status": filing_status,
    "pay_cycle": pay_cycle,
    "401k": _401k,
    "share_program": share_program,
}