def volume_cylinder(radius, height):
	'''Find volume of a cylinder'''

	pi = 3.142

	if radius == None or height == None:
		return 'enter input'

	elif type(radius) and type(height) == int or type(radius) and type(height) == float:
		r = radius ** 2
		volume = 2 * pi * r * height
		return volume
	return 'invalid input'
