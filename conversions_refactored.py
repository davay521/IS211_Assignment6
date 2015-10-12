'''
David Vayman
IS211_Assignment6
Conversions_refactored
'''

from decimal import Decimal


def convert(fromUnit, toUnit, value):
    """
        Yards to meter  Meter= Yards/1.0936
        Mile To meter   Meter =Mile/0.00062137
        Yard to Mile    Mile = Yard * 0.00056818
        Meter to Mile   Mile = Meter * 0.00062137
        Meter to Yard   Yard = Meter * 1.0936
        Mile to Yard    Yard = Mile * 1760
    """
    dist_convert_values = {
        'Mile': (0.00062137),
        'Yard': (1.0936),
        'Meter': (1)
    }

    temp_convert_values = {
        'Celsius': (1, 0),
        'Fahrenheit': ( 1.8, 32),
        'Kelvin': (1, 273.15)
    }

    if ( temp_convert_values.viewkeys() >= {fromUnit} and dist_convert_values.viewkeys() >= { toUnit}) \
        or ( temp_convert_values.viewkeys() >= {toUnit} and dist_convert_values.viewkeys() >= { fromUnit}):
        raise ConversionNotPossible("Conversion is not possible")

    elif dist_convert_values.viewkeys() >= {fromUnit, toUnit}:
        devisor = dist_convert_values[fromUnit]
        multiplier = dist_convert_values[toUnit]

        result =  Decimal( float(value)/devisor * multiplier )
        return round(result,7)

    elif temp_convert_values.viewkeys() >= {fromUnit, toUnit}:
        fromUnit = temp_convert_values[fromUnit]
        toUnit = temp_convert_values[toUnit]

        devisor = fromUnit[0]
        substract = fromUnit[1]
        divident = toUnit[0]
        addent = toUnit[1]

        result =  Decimal( (float(value) - substract) * divident / devisor  + addent)
        return round(result,7)


class ConversionNotPossible(Exception):
    """ Exception """
    pass

