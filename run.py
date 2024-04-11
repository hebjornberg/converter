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
        }, 
        "length": {
            "meters": {
                "feet": lambda x: x * 3.28084, 
                "miles": lambda x: x / 1609.34, 
                "kilometers": lambda x: x / 1000
            }, 
            "feet" : {
                "meters": lambda x: x / 3.28084,
                "miles": lambda x: x / 5280,
                "kilometers": lambda x: x / 3280.84
            }, 
            "miles": {
                "meters": lambda x: x * 1609.34,
                "kilometers": lambda x: x * 1.60934,
                "feet": lambda x: x * 5280
            },
            "kilometers": {
                "meters": lambda x: x * 1000,
                "miles": lambda x: x / 1.60934,
                "feet": lambda x: x * 3280.84
            }
        }, 
        "weight": {
            "kilograms"
        }
    }
    
    try: 
        conversions_func = conversions[category][from_unit][to_unit]
        converted_value = conversions_func(value)
        return converted_value
    except KeyError: 
        "Invalid unit or category. Please try again."

unit_abbr = {
    "temperature": {
    "C": "celsius", 
    "F": "fahrenheit", 
    "K": "kelvin"
    }, 
    "weight": {
    "kg": "kilograms", 
    "lbs": "pounds", 
    }, 
    "length": {
    "m": "meters", 
    "ft": "feet", 
    "mi": "miles", 
    "km" : "kilometer"
    }, 
}

def main(): 
    while True:
        print("\nMenu:")
        print("1. Temperature")
        print("2. Length")
        print("3. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            category = "temperature"
            from_unit = input("Enter unit to convert from (celsius/C, kelvin/K, fahrenheit/F):").lower()
            to_unit = input("Enter the value you want to convert to (celsius/C, kelvin/K, fahrenheit/F):").lower()
        elif choice == "2":
            category = "length"
            from_unit = input("Enter unit to convert from (e.g. , m, ft, mi, km):").lower()
            to_unit = input("Enter the unit to convert to (e.g. , m, ft, mi, km):").lower()
        elif choice == "3": 
            print("Exiting...")
            break
        else: 
            print("Invalid choice. Try again.")
            break

        while True: 
            try: 
                value = float(input(f"Enter value in {from_unit}:"))
                break
            except ValueError:
                print("Invalid value. Please enter a number.")

        try: 
            from_unit = unit_abbr[category][from_unit]
            to_unit = unit_abbr[category][to_unit]
        except KeyError:
            print("Invalid unit. Please try again.")
            continue

        result = convert_unit(value, from_unit, to_unit, category)

        if isinstance(result, str):
            print(result)
        else: 
            print(f"{value} {from_unit} is equal to {result} {to_unit}")


main()

