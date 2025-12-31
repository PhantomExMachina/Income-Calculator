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
                position_type == "contractor"
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

    return position_type, filing_status