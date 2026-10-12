x = float(input("Enter a positive number: "))

guess = x / 2
tolerance = 1e-6
iterations = 0

while abs(guess**2 - x) > tolerance:
	guess = 0.5 * (guess + x / guess)
	iterations += 1

print(f"Final guess: {guess:.6f}")
print(f"Iterations: {iterations}")
