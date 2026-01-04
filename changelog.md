# Changelog

## 0.0.1 - 2025-12-31
Initial Working Version

## 0.1.0 - 2025-12-31
- Added position types to better calculate overtime wages
- Added file i/o for a settings file so that the script can access common preferences automatically

## 0.2.0 - 2025-12-31
- Added brackets.json for federal income tax for single filers, joint filers, and HoH filers

## 0.2.1 - 2025-12-31
- Added filing status to settings file and i/o block logic
- Split file i/o block into file_handler.py and converted it into a function which returns a tuple
- Added __pycache__ to .gitignore

## 0.2.2 - 2025-12-31
- Updated readme to be more realistic and a bit more organized

## 0.3.0 - 2025-12-31
- Extended file handler to also check for and include pay cycle information
- Removed versioning from main.py
- Added a docstring to file_handler.p
- Corrected a syntax error in file_handler.py that may have led to a crash when handling contractors
- Corrected a logical error in file_handler.py that may cause issues with weekly vs bi-weekly and monthly vs semi-monthly checks
- Corrected a typo in file_handler.py: ":> " -> ">: 
- Added bracket_calc.py (unfinished) to calculate esteimated withheld funds based on annualized cycle income.
- Renamed brackets.json to federal_income_brackets.json for better readability
- Added state_income_brackets.json (unfinished)
- Added a todo list for me to keep track of (included in .gitignore)
- Added a roadmap to README.md

## 0.3.1 - 2025-12-31
- Created utils.py
- Refactored main.py, moved input logic and conditional logic to utils.py
- Finished state_income_brackets.json (Giving chatgpt the credit for this. WAY too much repetitive typing for my taste.)

## 0.3.2 - 2026-01-01
- Changed all instances of '"married"' in state_income_brackets.json to '"married_filing_jointly"' to better align with patterns in federal_income_brackets.json
- Major changes to the file handling logic, but not purpose. Added a number of new functions that validate the settings.txt is structured properly, and if not, rewrites the file with the appropriate structure.
- The above changes have inadvertently broken utils.py, but realistically, most of the code needs to be rewritten for future proofing.

## 0.3.3 - 2026-01-02
- Fixed all issues with utils.py
- renamed file_handler.py to settings_handler.py
- Finished input functions + input sanitation and normalization in settings_handler.py

## 0.3.4 - 2026-01-04
- Added mappings.py - this will contain any dictionary style mapping for use in this project.
- Defined pay_cycle_map within mappings.py, which just assigns the annual paycycle count based on pay_cycle type.
- Defined get_annual_paycheck_count() - a function that gets the annual paycheck count from settings.pay_cycle > mappings.pay_cycle_map("pay_cycle")
- Added a few new functions for calculating static information such as weekly and annual base pay, annualized pay based on weekly pay + overtime, paycheck base pay, etc.