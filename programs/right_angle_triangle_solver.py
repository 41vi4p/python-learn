import math

def calculate_hypotenuse(base, height):
    """Calculate hypotenuse using Pythagorean theorem"""
    return round(math.sqrt(base**2 + height**2), 2)

def calculate_angle(opposite, hypotenuse):
    """Calculate angle using inverse sine"""
    return round(math.degrees(math.asin(opposite/hypotenuse)), 2)

def calculate_area(base, height):
    """Calculate area of right triangle"""
    return round((base * height) / 2, 2)

def calculate_perimeter(base, height, hypotenuse):
    """Calculate perimeter of right triangle"""
    return round(base + height + hypotenuse, 2)

def validate_input():
    """Get and validate user input"""
    try:
        base = float(input("\nEnter base length: "))
        height = float(input("Enter height length: "))
        if base <= 0 or height <= 0:
            raise ValueError
        return base, height
    except ValueError:
        print("\nPlease enter valid positive numbers!")
        return None, None

def main():
    print("\n=== Right Triangle Solver ===")
    while True:
        base, height = validate_input()
        if base is None:
            continue
            
        hypotenuse = calculate_hypotenuse(base, height)
        angle1 = calculate_angle(height, hypotenuse)
        angle2 = calculate_angle(base, hypotenuse)
        area = calculate_area(base, height)
        perimeter = calculate_perimeter(base, height, hypotenuse)
        
        print("\nResults:")
        print(f"Hypotenuse: {hypotenuse}")
        print(f"Angles: {angle1}° and {angle2}°")
        print(f"Area: {area}")
        print(f"Perimeter: {perimeter}")
        
        if input("\nCalculate another? (y/n): ").lower() != 'y':
            break
    
    print("\nThank you for using Right Triangle Solver!")

if __name__ == "__main__":
    main()