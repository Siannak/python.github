# Problem 10: Robot Path Tracking
def move(pos, dx, dy):
	"""Return a new position after moving by (dx, dy)."""
	return (pos[0] + dx, pos[1] + dy)

# Start at the origin
position = (0.0, 0.0)
print(f"Start: {position}")

# Apply two moves
position = move(position, 3.0, 4.0)
position = move(position, -1.0, 2.0)

# Unpack the final position
x, y = position
distance = (x**2 + y**2) ** 0.5

print(f"Final position: {position}")
print(f"Distance from origin: {distance:.2f} m")