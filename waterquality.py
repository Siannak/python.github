# Problem 4: Water Quality Checker
import math
from abc import ABC, abstractmethod


class DO_ok(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def check(self):
        """Return True when the dissolved oxygen is safe."""
        raise NotImplementedError

    @abstractmethod
    def reason(self):
        """Return a message explaining why the oxygen level failed."""
        raise NotImplementedError


class DissolvedOxygenCheck(DO_ok):
    def check(self):
        return self.value > 5

    def reason(self):
        if self.check():
            return ""
        return " - Dissolved oxygen too low"


pH = float(input("Enter pH: "))
temp = float(input("Enter temperature (C): "))
DO = float(input("Enter dissolved oxygen (mg/L): "))

# Pre-compute each check (chained comparisons)
pH_ok = 6.5 <= pH <= 8.5
temp_ok = 10 <= temp <= 25
do_check = DissolvedOxygenCheck(DO)
DO_ok = do_check.check()

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


 


