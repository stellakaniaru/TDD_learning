def area_circle(radius):
	'''Find area of a circle'''

	pi = 3.142
	

	if radius is None:
		return 'enter input'

	elif type(radius) == int or type(radius) == float:
		r = radius ** 2
		area = 2 * pi * r
		return area
	return 'invalid input'




if __name__ == '__main__':
        unittest.main()
