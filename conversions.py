'''
David Vayman
IS211_Assignment6
Conversions
'''

from decimal import Decimal

"""
Takes in a float representing a Celsius measurement, and returns that
temperature converted into Kelvins
"""
def convertCelsiusToKelvin(floatVal):
    result = Decimal(float(floatVal) + 273.15)
    return round(result,2)

"""
Takes in a float representing a Celsius measurement, and returns
that temperature converted into Fahrenheit
"""
def convertCelsiusToFahrenheit(floatVal):
    return float(floatVal) * 9/5 + 32

"""
Takes in a float representing a Fahrenheit measurement, and returns
that temperature converted into Celsius
"""
def convertFahrenheitToCelsius(floatVal):
    result = Decimal( (float(floatVal) - 32) * 5/9)
    return round(result,2)


"""
Takes in a float representing a Fahrenheit measurement, and returns
that temperature converted into Kelvin
"""
def convertFahrenheitToKelvin(floatVal):
    result = Decimal( (float(floatVal)  + 459.67) * 5/9)
    return round(result,2)

"""
Takes in a float representing a Kelvin measurement, and returns
that temperature converted into Celsius
"""
def convertKelvinToCelsius(floatVal):
    result = Decimal(float(floatVal) - 273.15)
    return round(result,2)

"""
Takes in a float representing a Kelvin measurement, and returns
that temperature converted into Fahrenheit
"""
def convertKelvinToFahrenheit(floatVal):
    result = Decimal(float(floatVal)  * 9/5 - 459.67)
    return round(result,2)

