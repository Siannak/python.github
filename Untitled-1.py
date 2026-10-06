 #pressure vessel

internal_pressure = float(input("Enter internal pressure (psi): "))
wall_temperature = float(input("Enter wall temperature (C): "))
vibration_level = float(input("Enter vibration level (mm/s): "))


def internal_pressure_ok(pressure):     
        """Return True when pressure is within the safe operating range."""
        return 5 <= pressure <= 10


internal_pressure_is_safe = internal_pressure_ok(internal_pressure)
wall_temperature_ok = 20 <= wall_temperature <= 250
vibration_level_ok = vibration_level < 4

if internal_pressure_is_safe and wall_temperature_ok and vibration_level_ok:
    print("System is SAFE.")
else:
    print("System is UNSAFE.")
    if not internal_pressure_is_safe:
        print(" - Internal pressure out of range")
    if not wall_temperature_ok:
        print(" - Wall temperature out of range")
    if not vibration_level_ok:
        print(" - Vibration out of range")
