def odd_even_solutions(TestCase):
	'''Check if number is even or odd'''
	if TestCase is None:
			return 'Enter input'

	if type(TestCase) == int:
		
		if TestCase == 0:
			return 'Number is not even or odd'

		elif TestCase % 4 == 0:
			return 'Number is a multiple of four'

		elif TestCase % 2 == 0:
			return 'Number is even'

		elif TestCase % 2 == 1:
			return 'Number is odd'

	return 'Invalid input'

# print odd_even_solutions('steSB')

