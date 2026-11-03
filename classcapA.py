class Capacitor:
	def __init__(self, capacitance):
		self.capacitance = capacitance

	def charge(self, voltage):
		return self.capacitance * voltage

	def energy(self, voltage):
		return 0.5 * self.capacitance * voltage**2


capacitor = Capacitor(100e-6)
voltage = 12

print(f"Charge: {capacitor.charge(voltage):.4f} C")
print(f"Energy: {capacitor.energy(voltage):.4f} J")