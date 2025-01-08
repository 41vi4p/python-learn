import math

def find_side_with_hypotenuse(hypotenuse: float, known_side: float) -> float:
    """Find missing side given hypotenuse and one side."""
    if hypotenuse <= known_side:
        raise ValueError("Hypotenuse must be larger than other side")
    return math.sqrt(hypotenuse**2 - known_side**2)

def find_hypotenuse(side1: float, side2: float) -> float:
    """Find hypotenuse given two sides."""
    return math.sqrt(side1**2 + side2**2)

def find_angles(side1: float, side2: float, hypotenuse: float) -> tuple:
    """Calculate all angles in the triangle (in degrees)."""
    if not (side1 > 0 and side2 > 0 and hypotenuse > 0):
        raise ValueError("All sides must be positive")
    if hypotenuse <= side1 or hypotenuse <= side2:
        raise ValueError("Hypotenuse must be the longest side")
    
    # Calculate angles using inverse trigonometric functions
    angle1 = math.degrees(math.asin(side1/hypotenuse))
    angle2 = math.degrees(math.asin(side2/hypotenuse))
    angle3 = 90  # Right angle
    
    return (angle1, angle2, angle3)

def is_pythagorean_triple(a: int, b: int, c: int) -> bool:
    """Check if three numbers form a Pythagorean triple."""
    return a**2 + b**2 == c**2

def main():
    print("Right Triangle Calculator")
    print("1. Find missing side (given hypotenuse and one side)")
    print("2. Find hypotenuse (given two sides)")
    print("3. Check Pythagorean triple")
    print("4. Find angles")
    
    choice = input("Enter your choice (1-4): ")
    
    try:
        if choice == '1':
            h = float(input("Enter hypotenuse: "))
            s = float(input("Enter known side: "))
            result = find_side_with_hypotenuse(h, s)
            print(f"Missing side: {result:.2f}")
            
        elif choice == '2':
            s1 = float(input("Enter first side: "))
            s2 = float(input("Enter second side: "))
            result = find_hypotenuse(s1, s2)
            print(f"Hypotenuse: {result:.2f}")
            
        elif choice == '3':
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            c = int(input("Enter third number: "))
            result = is_pythagorean_triple(a, b, c)
            print(f"Is Pythagorean triple? {result}")
            
        elif choice == '4':
            s1 = float(input("Enter first side: "))
            s2 = float(input("Enter second side: "))
            h = float(input("Enter hypotenuse: "))
            angles = find_angles(s1, s2, h)
            print(f"Angles: {angles[0]:.2f}°, {angles[1]:.2f}°, {angles[2]}°")
            
        else:
            print("Invalid choice")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()