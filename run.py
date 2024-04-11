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
                "feet": lambda x: x * 3.28084
            }, 
            "feet" : {
                "meters": lambda x: x / 3.28084
            }
        }
    }
    
    try: 
        conversions_func = conversions[category][from_unit][to_unit]
        converted_value = conversions_func(value)
        return converted_value
    except KeyError: 
        "Invalid unit or category. Please try again."

def main(): 
    while True:
        print("\nMenu:")
        print("1. Temperature")
        print("2. Length")
        print("3. Exit")

        choice = input("Enter your choice:")

        if choice == "1":
            category = "temperature"
            from_unit = input("Enter unit to convert from (celsius, kelvin, fahrenheit):").lower()
            to_unit = input("Enter the value you want to convert to (celsius, kelvin, fahrenheit:)").lower()
        elif choice == "2":
            category = "length"
            from_unit = input("Enter unit to convert from (meter, feet):").lower()
            to_unit = input("Enter the unit to convert to (meter, feet):").lower()
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

        result = convert_unit(value, from_unit, to_unit, category)

        if isinstance(result, str):
            print(result)
        else: 
            print(f"{value} {from_unit} is equal to {result} {to_unit}")


main()

