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