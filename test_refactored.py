'''
David Vayman
IS211_Assignment6
Test_refactored
'''

import conversions_refactored
import unittest


#test all temperature conversions

class TempTest(unittest.TestCase):

	def testConvertCelsiusToKelvin(self):
		result = conversions_refactored.convert('Celsius', 'Kelvin', 300.00)
		self.assertEqual(573.15, result)

	def testConvertKelvinToCelsius(self):
		result = conversions_refactored.convert('Kelvin', 'Celsius', 573.15)
		self.assertEqual(300.00, result)

	def testCelsiusToFahrenheit(self):
		result = conversions_refactored.convert('Celsius', 'Fahrenheit', 300.00)
		self.assertEqual(572.00, result)

	def testFahrenheitToCelsius(self):
		result = conversions_refactored.convert('Fahrenheit', 'Celsius', 572.00)
		self.assertEqual(300.00, result)

	def testKelvinToFahrenheit(self):
		result = conversions_refactored.convert('Kelvin', 'Fahrenheit', 300.00)
		self.assertEqual(80.33, result)

	def testFahrenheitToKelvin(self):
		result = conversions_refactored.convert('Fahrenheit', 'Kelvin', 80.33)
		self.assertEqual(300.00, result)



#test all distance conversions

class DistanceTest(unittest.TestCase):

	def testConvertMetersToYards(self):
		result = conversions_refactored.convert('Meter', 'Yard', 1.00)
		self.assertEqual(1.0936, result)

	def testConvertYardsToMeters(self):
		result = conversions_refactored.convert('Yard', 'Meter', 1.00)
		self.assertEqual(0.9144111, result)

	def testConvertYardsToMiles(self):
		result = conversions_refactored.convert('Yard', 'Mile', 10000.0416)
		self.assertEqual(5.6819, result)

	def testConvertMilesToYards(self):
		result = conversions_refactored.convert('Mile', 'Yard', 5.6819)
		self.assertEqual(10000.0415855, result)

	def testConvertMetersToMiles(self):
		result = conversions_refactored.convert('Meter', 'Mile', 1.00)
		self.assertEqual(0.0006214, result)

	def testConvertMilesToMeters(self):
		result = conversions_refactored.convert('Mile', 'Meter', 1.00)
		self.assertEqual(1609.3470879, result)


class DistanceSelfConversion(unittest.TestCase):
	measures = ( 'Meter', 'Yard', 'Mile')

	def testConvertSelf(self):
		for measure in self.measures:
			result = conversions_refactored.convert(measure, measure, 10.00)
			self.assertEqual(10.00, result)

class IncompatibleConversion(unittest.TestCase):

	def testConvertDistanceToTemp(self):
		self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert, 'Meter', 'Kelvin', 10.00)


	def testConvertTempToDistance(self):
		self.assertRaises(conversions_refactored.ConversionNotPossible, conversions_refactored.convert, 'Celsius', 'Yard', 10.00)


if __name__ == "__main__":
    unittest.main()
