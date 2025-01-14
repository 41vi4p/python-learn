
CIPHER = {chr(65+i): str(i+1) for i in range(26)}  # A-Z to 1-26
REVERSE_CIPHER = {str(i+1): chr(65+i) for i in range(26)}  # 1-26 to A-Z

def encode_message(message):
    """Convert text to numbers"""
    return ' '.join(CIPHER.get(c.upper(), c) for c in message)

def decode_message(message):
    """Convert numbers back to text"""
    return ' '.join(REVERSE_CIPHER.get(c, c) for c in message.split())

def display_cipher():
    """Show the cipher key"""
    print("\n=== Cipher Key ===")
    for letter, number in CIPHER.items():
        print(f"{letter}={number}", end='  ')
    print()

def main():
    while True:
        print("\n=== Code Breakers ===")
        print("1. Encode (text to numbers)")
        print("2. Decode (numbers to text)")
        print("3. Show cipher key")
        print("4. Exit")
        
        choice = input("\nChoice (1-4): ")
        
        if choice == '1':
            text = input("Enter text to encode: ")
            print(f"Encoded: {encode_message(text)}")
            
        elif choice == '2':
            numbers = input("Enter numbers to decode: ")
            print(f"Decoded: {decode_message(numbers)}")
            
        elif choice == '3':
            display_cipher()
            
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()