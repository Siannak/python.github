pressure = float(input("Enter internal pressure (bar): "))
temperature = float(input("Enter wall temperature (°C): "))
vibration = float(input("Enter vibration level (mm/s): "))

reasons = []

if not 5 <= pressure <= 15:
	reasons.append("internal pressure must be between 5 and 15 bar")
if not 20 <= temperature <= 250:
	reasons.append("wall temperature must be between 20 and 250 °C")
if vibration >= 4:
	reasons.append("vibration level must be below 4 mm/s")

if reasons:
	print("The pressure vessel is unsafe.")
	for reason in reasons:
		print(f"- {reason}")
else:
	print("The pressure vessel is safe.")