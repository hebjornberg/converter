def convert_unit(value, from_unit, to_unit, category):
    conversions = {
        "temperature": {
            "celsius": {
                "fahrenheit": lambda x: (x * 9/5) + 32, 
                "kelvin": lambda x: x + 273.15
            },
            "fahrenheit": {
                "celsius": lambda x: (x - 32) * 5/9, 
                "kelvin": lambda x: (x + 459.67) * 5/9
            },
            "kelvin": {
                "celsius": lambda x: x - 273.15,
                "fahrenheit": lambda x: (x * 9/5) - 459.67
            }
        }
    }
    
    print(conversions)

convert_unit(0, "celsius", "fahrenheit", "temperature")