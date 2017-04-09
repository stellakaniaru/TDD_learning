'''Test suite for area function'''

import unittest
from unittest import TestCase
from area_function import area_circle

class AreaCircleTestCase(TestCase):
	'''Test case for area function'''

	def Test_empty_input(self):
		'''Test for no input'''
		self.assertEqual(area_circle(None), 'enter input')

	def Test_integer_input_returns(self):
		'''Test for integer values'''
		self.assertEqual(area_circle(1), 6.284)

	def Test_float_input_returns(self):
		'''Test for float values'''
		self.assertEqual(area_circle(1.0), 6.284)

	def Test_string_input_returns(self):
		'''Test for string input'''
		self.assertEqual(area_circle('stella'), 'invalid input')

	def Test_long_type_input_returns(self):
		'''Test for long values'''
		self.assertEqual(area_circle(50**50), 'invalid input')

	def Test_boolean_input_returns(self):
		'''Test for boolean values'''
		self.assertEqual(area_circle(False), 'invalid input')


if __name__ == '__main__':
        unittest.main()
