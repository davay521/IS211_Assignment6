'''
David Vayman
IS211_Assignment6
test
'''


import conversions
import unittest


#test conversion celsius to kelvin

class CelsiusToKelvin(unittest.TestCase):

	def testConvertCelsiusToKelvin_default(self):
		result = conversions.convertCelsiusToKelvin(300.00)
		self.assertEqual(573.15, result)

	def testConvertCelsiusToKelvin_zeroCelsius(self):
		result = conversions.convertCelsiusToKelvin(0.00)
		self.assertEqual(273.15, result)

	def testConvertCelsiusToKelvin_decimalValues(self):
		result = conversions.convertCelsiusToKelvin(0.02)
		self.assertEqual(273.17, result)

	def testConvertCelsiusToKelvin_negativeValues(self):
		result = conversions.convertCelsiusToKelvin(-280.00)
		self.assertEqual(-6.85, result)

	def testConvertCelsiusToKelvin_largeNumber(self):
		result = conversions.convertCelsiusToKelvin(2345670)
		self.assertEqual(2345943.15, result)


#test conversions kelvin to celsius

class KelvinToCelsius(unittest.TestCase):

	def testConvertKelvinToCelsius_default(self):
		result = conversions.convertKelvinToCelsius(573.15)
		self.assertEqual(300.00, result)

	def testConvertKelvinToCelsius_zeroCelsius(self):
		result = conversions.convertKelvinToCelsius(273.15)
		self.assertEqual(0.00, result)

	def testConvertKelvinToCelsius_decimalValues(self):
		result = conversions.convertKelvinToCelsius(273.17)
		self.assertEqual(0.02, result)

	def testConvertKelvinToCelsius_negativeValues(self):
		result = conversions.convertKelvinToCelsius(-6.85)
		self.assertEqual(-280.00, result)

	def testConvertKelvinToCelsius_largeNumber(self):
		result = conversions.convertKelvinToCelsius(2345943.15)
		self.assertEqual(2345670, result)


"""
test conversions celsius to fahrenheit
"""
class CelsiusToFahrenheit(unittest.TestCase):
    
	def testCelsiusToFahrenheit_default(self):
		result = conversions.convertCelsiusToFahrenheit(300.00)
		self.assertEqual(572.00, result)

	def testCelsiusToFahrenheit_zeroCelsius(self):
		result = conversions.convertCelsiusToFahrenheit(0.00)
		self.assertEqual(32.00, result)

	def testCelsiusToFahrenheit_decimalValues(self):
		result = conversions.convertCelsiusToFahrenheit(15.5)
		self.assertEqual(59.9, result)

	def testCelsiusToFahrenheit_negativeValues(self):
		result = conversions.convertCelsiusToFahrenheit(-55.00)
		self.assertEqual(-67.00, result)

	def testCelsiusToFahrenheit_largeNumber(self):
		result = conversions.convertCelsiusToFahrenheit(2345670)
		self.assertEqual(4222238.00, result)



#test conversions fahrenheit to celsius

class FahrenheitToCelsius(unittest.TestCase):
    
	def testFahrenheitToCelsius_default(self):
		result = conversions.convertFahrenheitToCelsius(572.00)
		self.assertEqual(300.00, result)

	def testFahrenheitToCelsius_zeroCelsius(self):
		result = conversions.convertFahrenheitToCelsius(32.00)
		self.assertEqual(0.00, result)

	def testFahrenheitToCelsius_decimalValues(self):
		result = conversions.convertFahrenheitToCelsius(59.9)
		self.assertEqual(15.5, result)

	def testFahrenheitToCelsius_negativeValues(self):
		result = conversions.convertFahrenheitToCelsius(-67.00)
		self.assertEqual(-55.00, result)

	def testFahrenheitToCelsius_largeNumber(self):
		result = conversions.convertFahrenheitToCelsius(4222238.00)
		self.assertEqual(2345670, result)

"""
test conversions kelvin to fahrenheit
"""
class KelvinToFahrenheit(unittest.TestCase):

	def testKelvinToFahrenheit_default(self):
		result = conversions.convertKelvinToFahrenheit(300.00)
		self.assertEqual(80.33, result)

	def testKelvinToFahrenheit_zeroKelvin(self):
		result = conversions.convertKelvinToFahrenheit(0.00)
		self.assertEqual(-459.67, result)

	def testKelvinToFahrenheit_decimalValues(self):
		result = conversions.convertKelvinToFahrenheit(305.35)
		self.assertEqual(89.96, result)

	def testKelvinToFahrenheit_negativeValues(self):
		result = conversions.convertKelvinToFahrenheit(-30.35)
		self.assertEqual(-514.3, result)

	def testKelvinToFahrenheit_largeNumber(self):
		result = conversions.convertKelvinToFahrenheit(4222238.00)
		self.assertEqual(7599568.73, result)


#test conversions fahrenheit to kelvin

class FahrenheitToKelvin(unittest.TestCase):

	def testFahrenheitToKelvin_default(self):
		result = conversions.convertFahrenheitToKelvin(80.33)
		self.assertEqual(300.00, result)

	def testFahrenheitToKelvin_zeroKelvin(self):
		result = conversions.convertFahrenheitToKelvin(-459.67)
		self.assertEqual(0.00, result)

	def testFahrenheitToKelvin_decimalValues(self):
		result = conversions.convertFahrenheitToKelvin(89.96)
		self.assertEqual(305.35, result)

	def testFahrenheitToKelvin_negativeValues(self):
		result = conversions.convertFahrenheitToKelvin(-514.3)
		self.assertEqual(-30.35, result)

	def testFahrenheitToKelvin_largeNumber(self):
		result = conversions.convertFahrenheitToKelvin(7599568.73)
		self.assertEqual(4222238.00, result)


if __name__ == "__main__":
    unittest.main()