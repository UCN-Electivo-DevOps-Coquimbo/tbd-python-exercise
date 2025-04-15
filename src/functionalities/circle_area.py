import math

def execute():
    try:
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * radius ** 2
        print(f"The area of the circle is: {area:.2f}")
        print()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        print()
