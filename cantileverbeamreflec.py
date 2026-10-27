def beam_deflection(P, L, I, E=200e9):
	"""Calculate cantilever beam deflection.

	Args:
		P: Applied load in newtons (N).
		L: Beam length in metres (m).
		I: Second moment of area in metres to the fourth (m^4).
		E: Young's modulus in pascals (Pa), defaulting to steel.

	Returns:
		Deflection in metres (m).
	"""
	return P * L**3 / (3 * E * I)


if __name__ == "__main__":
	P = 1000
	L = 2
	I = 1e-6

	steel_deflection = beam_deflection(P, L, I)
	aluminium_deflection = beam_deflection(P, L, I, E=69e9)

	print(f"Steel beam deflection: {steel_deflection * 1000:.2f} mm")
	print(f"Aluminium beam deflection: {aluminium_deflection * 1000:.2f} mm")