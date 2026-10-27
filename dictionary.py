# Problem 11: Material Properties Database
materials = {
	"Aluminium": {"density": 2700, "youngs": 69e9},
	"Steel": {"density": 7850, "youngs": 200e9},
	"Copper": {"density": 8960, "youngs": 117e9},
}

choice = input("Enter material: ").title()
mat = materials.get(choice)

if mat:
	print(f"{choice}")
	print(f" Density: {mat['density']} kg/m3")
	print(f" Young's modulus: {mat['youngs'] / 1e9:.1f} GPa")
else:
	print(f"Material '{choice}' is not in the database.")