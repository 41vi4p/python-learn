def print_multiplication_table(limit):
    # Print header
    print("\n=== Multiplication Table ===")
    print("   ", end="")
    for i in range(1, limit + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * (limit * 4 + 4))

    # Print table content
    for i in range(1, limit + 1):
        print(f"{i:2} |", end="")
        for j in range(1, limit + 1):
            print(f"{i*j:4}", end="")
        print()

def print_exponent_table(limit):
    # Print header
    print("\n=== Exponent Table ===")
    print("   ", end="")
    for i in range(1, limit + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * (limit * 4 + 4))

    # Print table content
    for i in range(1, limit + 1):
        print(f"{i:2} |", end="")
        for j in range(1, limit + 1):
            print(f"{i**j:4}", end="")
        print()

def main():
    try:
        # Get user input
        limit = int(input("Enter the table limit (1-10): "))
        
        # Validate input
        if limit < 1 or limit > 10:
            raise ValueError("Limit must be between 1 and 10")
            
        # Print tables
        print_multiplication_table(limit)
        print_exponent_table(limit)
        
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please enter a valid number between 1 and 10")

if __name__ == "__main__":
    main()