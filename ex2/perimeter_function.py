def perimeter_circle(diameter):
	'''Find the perimeter of a circle.'''

	pi = 3.142

	if diameter is None:
		return 'enter input'
	if type(diameter) == int or type(diameter) == float:
		perimeter = pi * diameter
		return perimeter
	return 'invalid input'

