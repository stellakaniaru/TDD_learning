'''Test suite for odd even solutions'''

from unittest import TestCase
from odd_even_solutions_functions import odd_even_solutions

class OddEvenSolutionsTestCase(TestCase):
	'''Check if a number is even or odd'''
	

	def Test_empty_input(self):
		'''Test empty input'''
		self.assertEqual(odd_even_solutions(None), 'Enter input')

	def Test_zero_input(self):
		'''Test for zero input'''
		self.assertEqual(odd_even_solutions(0), 'Number is not even or odd')

	def Test_even_number(self):
		'''Test even number'''
		self.assertEqual(odd_even_solutions(2), 'Number is even')

	def Test_odd_number(self):
		'''Test odd number'''
		self.assertEqual(odd_even_solutions(3), 'Number is odd')

	def Test_multiple_of_four(self):
		'''Test multiples of four'''
		self.assertEqual(odd_even_solutions(4), 'Number is a multiple of four')



