"""
file_handler.py

This file looks for, reads from, and updates the settings.txt file as needed.
"""

def handle(file="settings.txt"):
    with open(file, 'a+') as f:
        f.seek(0)
        contents = f.read()
        if "position_type:" not in contents:
            position_type = input("What kind of employee are you? (Select one of the following)\n\nA: Hourly\nB: Salary\nC: Contractor\n\n>: ")
            if position_type.lower() == "a":
                position_type = "hourly"
            elif position_type.lower() == "b":
                position_type = "salary"
            elif position_type.lower() == "c":
                position_type = "contractor"
            f.write(f"position_type: {position_type}\n")
        else:
            if "hourly" in contents:
                position_type = "hourly"
            elif "salary" in contents:
                position_type = "salary"
            elif "contractor" in contents:
                position_type = "contractor"
        
        if "filing_status:" not in contents:
            filing_status = input("What is your filing status? (Select one of the following)\n\nA: Single\nB: Married - Filing Jointly\nC: Head of household\n\n>: ")
            if filing_status.lower() == "a":
                filing_status = "single"
            elif filing_status.lower() == "b":
                filing_status = "married_filing_jointly"
            elif filing_status.lower() == "c":
                filing_status = "head_of_household"
            f.write(f"filing_status: {filing_status}\n")
        else:
            if "single" in contents:
                filing_status = "single"
            elif "married_filing_jointly" in contents:
                filing_status = "married_filing_jointly"
            elif "head_of_household" in contents:
                filing_status = "head_of_household"
        
        if "pay_cycle" not in contents:
            pay_cycle = input("What type of pay cycle does your employer utilize?\n\n" \
            "A: Weekly\n" \
            "B: Bi-weekly (Every two weeks)\n" \
            "C: Semi-monthly (e.g., 1st & 15th, or 15th and last day)\n" \
            "D: Monthly\n" \
            "E: Daily\n" \
            "F: On-Demand\n" \
            "G: Per-project / Milestone nased\n" \
            "H: Net-X invoicing\n" \
            "I: 13-Period (Every 28 days)\n\n" \
            ">: ")

            if pay_cycle.lower() == "a":
                pay_cycle = "weekly"
            elif pay_cycle.lower() == "b":
                pay_cycle = "bi_weekly"
            elif pay_cycle.lower() == "c":
                pay_cycle = "semi_monthly"
            elif pay_cycle.lower() == "d":
                pay_cycle = "monthly"
            elif pay_cycle.lower() == "e":
                pay_cycle = "daily"
            elif pay_cycle.lower() == "f":
                pay_cycle = "on_demand"
            elif pay_cycle.lower() == "g":
                pay_cycle = "per_project"
            elif pay_cycle.lower() == "h":
                pay_cycle = "net_x"
            elif pay_cycle.lower() == "i":
                pay_cycle = "13_period"
            f.write(f"pay_cycle: {pay_cycle}\n")
        else:
            if "weekly" in contents and not "bi-weekly" in contents:
                pay_cycle = "weekly"
            elif "bi_weekly" in contents:
                pay_cycle = "bi_weekly"
            elif "semi_monthly" in contents:
                pay_cycle = "semi_monthly"
            elif "monthly" in contents and not "semi_monthly" in contents:
                pay_cycle = "monthly"
            elif "daily" in contents:
                pay_cycle = "daily"
            elif "on_demand" in contents:
                pay_cycle = "on_demand"
            elif "per_project" in contents:
                pay_cycle = "per_project"
            elif "net_x" in contents:
                pay_cycle = "net_x"
            elif "13_period" in contents:
                pay_cycle = "13_period"

    return position_type, filing_status, pay_cycle