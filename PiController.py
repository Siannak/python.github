# Problem 15: PID Integral Accumulator
integral = 0.0


def update_integral(error, dt):
	"""Update the PI integral term and return the new accumulator value."""
	global integral
	integral += error * dt
	return integral


# Simulate a control loop
setpoint = 10
dt = 0.1

for t in range(10):
	process_value = t
	error = setpoint - process_value
	I = update_integral(error, dt)
	print(f"t={t} error={error:>2} integral={I:.2f}")