'''Test suite for perimeter_function'''

#import unittest
from unittest import TestCase
from perimeter_function import perimeter_circle

class PerimeterCircleTestCase(TestCase):
	'''Test Case for perimeter function'''

	def Test_empty_input(self):
		'''Test empty input'''
		self.assertEqual(perimeter_circle(None), 'enter input')

	def Test_integer_input_returns(self):
		'''test integer input'''
		self.assertEqual(perimeter_circle(1), 3.142)

	def Test_float_input_returns(self):
		'''test float input'''
		self.assertEqual(perimeter_circle(1.0), 3.142)

	def Test_string_input_returns(self):
		'''test string input'''
		self.assertEqual(perimeter_circle('stella'), 'invalid input')

	def Test_long_type_input_returns(self):
		'''test long input'''
		self.assertEqual(perimeter_circle(50**50), 'invalid input')

	def Test_boolean_input_returns(self):
		'''test boolean input'''
		self.assertEqual(perimeter_circle(True), 'invalid input')
		
