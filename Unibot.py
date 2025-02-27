def intro():
    return "Hello! I am Unibot, your unit converter friend. I was created by Aabhas to help you with unit conversions."

def mass_conversion(option, value):
    conversions = {
        1: ("Kilogram", "Gram", 1000),
        2: ("Gram", "Kilogram", 1/1000),
        3: ("Gram", "Milligram", 1000),
        4: ("Milligram", "Gram", 1/1000),
        5: ("Pound", "Kilogram", 0.45),
        6: ("Kilogram", "Pound", 1/0.45)
    }
    if option in conversions:
        unit_from, unit_to, factor = conversions[option]
        return f"Converted value: {value * factor} {unit_to}"
    return "Invalid option selected."

def length_conversion(option, value):
    conversions = {
        1: ("Kilometre", "Metre", 1000),
        2: ("Metre", "Kilometre", 1/1000),
        3: ("Metre", "Centimetre", 100),
        4: ("Centimetre", "Metre", 1/100),
        5: ("Inch", "Centimetre", 2.54),
        6: ("Centimetre", "Inch", 1/2.54)
    }
    if option in conversions:
        unit_from, unit_to, factor = conversions[option]
        return f"Converted value: {value * factor} {unit_to}"
    return "Invalid option selected."

def volume_conversion(option, value):
    conversions = {
        1: ("Litre", "Millilitre", 1000),
        2: ("Millilitre", "Litre", 1/1000),
        3: ("Hectolitre", "Litre", 100),
        4: ("Litre", "Hectolitre", 1/100),
        5: ("Gallon", "Litre", 4.54),
        6: ("Litre", "Gallon", 1/4.54)
    }
    if option in conversions:
        unit_from, unit_to, factor = conversions[option]
        return f"Converted value: {value * factor} {unit_to}"
    return "Invalid option selected."

def currency_conversion(option, value):
    conversions = {
        1: ("Dollar", "Rupees", 83),
        2: ("Rupees", "Dollar", 1/83),
        3: ("Euro", "Rupees", 91),
        4: ("Rupees", "Euro", 1/91),
        5: ("Yen", "Rupees", 1/1.77),
        6: ("Rupees", "Yen", 1.77)
    }
    if option in conversions:
        unit_from, unit_to, factor = conversions[option]
        return f"Converted currency: {value * factor} {unit_to}"
    return "Invalid option selected."

def convert_units(category, option, value):
    if category == 1:
        return mass_conversion(option, value)
    elif category == 2:
        return length_conversion(option, value)
    elif category == 3:
        return volume_conversion(option, value)
    elif category == 4:
        return currency_conversion(option, value)
    return "Invalid category selected."