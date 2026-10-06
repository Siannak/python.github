print("hello world")
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Engineering Python.")
import math
 # --- Inputs ---
adjacent = float(input("Enter horizontal distance (m): "))
angle_deg = float(input("Enter angle of elevation (deg): "))

# --- Convert angle to radians ---
angle_rad = math.radians(angle_deg)

# --- Calculations ---
height = adjacent * math.tan(angle_rad)
hypotenuse = adjacent / math.cos(angle_rad)

# --- Outputs ---
print(f"Height of tower: {height:.2f} m")
print(f"Line-of-sight: {hypotenuse:.2f} m")