'''Test suite for volume_function'''

from unittest import TestCase
from volume_function import volume_cylinder

class VolumeFunctionTestCase(TestCase):
	'''Test case for volume function'''

	def Test_empty_input(self):
		'''Test for no input'''
		self.assertEqual(volume_cylinder(None, None), 'enter input')

	def Test_integer_input_returns(self):
		'''Test for integer inputs'''
		self.assertEqual(volume_cylinder(1, 1), 6.284)

	def Test_float_input_returns(self):
		'''Test for float inputs'''
		self.assertEqual(volume_cylinder(1.0, 1.0), 6.284)

	def Test_string_input_returns(self):
		'''Test for string inputs'''
		self.assertEqual(volume_cylinder('stek', 'kil'), 'invalid input')

	def Test_string_input_returns(self):
		'''Test for string inputs'''
		self.assertEqual(volume_cylinder('stek', 1), 'invalid input')

	def Test_string_input_returns(self):
		'''Test for string inputs'''
		self.assertEqual(volume_cylinder(1.0, 'stek'), 'invalid input')

	def Test_long_input_returns(self):
		'''Test for long inputs'''
		self.assertEqual(volume_cylinder(50**50, 60**60), 'invalid input')

	def Test_boolean_input_returns(self):
		'''Test for boolean inputs'''
		self.assertEqual(volume_cylinder(True, False), 'invalid input')