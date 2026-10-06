# Problem 4: Water Quality Checker
pH = float(input("Enter pH: "))
temp = float(input("Enter temperature (C): "))
DO = float(input("Enter dissolved oxygen (mg/L): "))

# Pre-compute each check (chained comparisons)
pH_ok = 6.5 <= pH <= 8.5
temp_ok = 10 <= temp <= 25
DO_ok = DO > 5

# All checks must pass for the water to be safe
if pH_ok and temp_ok and DO_ok:
    print("Water is SAFE.")
else:
    print("Water is UNSAFE.")
    if not pH_ok:
        print(" - pH out of range")
    if not temp_ok:
        print(" - Temperature out of range")
    if not DO_ok:
        print(" - Dissolved oxygen too low")