#Asks the user for three sensor readings: pH, temperature (in °C), and dissolved oxygen (in mg/L).
 Checks whether each reading is within its acceptable range:
pH between 6.5 and 8.5 inclusive
 Temperature between 10 and 25 °C inclusive
  Dissolved oxygen greater than 5 mg/L
If all three checks pass, prints “Water is SAFE.”
 Otherwise, prints “Water is UNSAFE.” followed by the specific reason(s) that failed:
"pH out of range" if the pH check failed
"Temperature out of range" if the temperature check failed
"Dissolved oxygen too low" if the DO check failed