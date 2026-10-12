print("hello world")
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Engineering Python.")
import math
 # --- Inputs ---
adjacent = float(input("Enter horizontal distance (m): "))
angle_deg = float(input("Enter angle of elevation (deg): "))

# --- Convert angle to radians ---
class angle_rad:
	"""Represent an angle supplied in degrees and provide radian trig values."""

	def __init__(self, degrees):
		self.degrees = float(degrees)

	def radians(self):
		return math.radians(self.degrees)

	def sin(self):
		return math.sin(self.radians())

	def cos(self):
		return math.cos(self.radians())

	def tan(self):
		return math.tan(self.radians())


angle = angle_rad(angle_deg)

# --- Calculations ---
height = adjacent * angle.tan()
hypotenuse = adjacent / angle.cos()

# --- Outputs ---
print(f"Height of tower: {height:.2f} m")
print(f"Line-of-sight: {hypotenuse:.2f} m")


