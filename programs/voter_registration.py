#voter ID - name age address 2 options register , view voters- print only name and contact number
# Voter registration App

# Dictionary to store voter data
voters = {}
last_voter_id = 1000  # Starting voter ID

def generate_voter_id():
    global last_voter_id
    last_voter_id += 1
    return f"V{last_voter_id}"

def validate_age(age):
    return age >= 18

def register_voter():
    print("\n=== Voter Registration ===")
    
    # Get voter details
    name = input("Enter full name: ")
    
    try:
        age = int(input("Enter age: "))
        if not validate_age(age):
            print("Sorry, minimum age for voting is 18 years.")
            return
    except ValueError:
        print("Invalid age entered.")
        return
    
    address = input("Enter address: ")
    contact = input("Enter contact number: ")
    
    # Generate voter ID and store data
    voter_id = generate_voter_id()
    voters[voter_id] = {
        "name": name,
        "age": age,
        "address": address,
        "contact": contact
    }
    
    print(f"\nRegistration successful!")
    print(f"Your Voter ID is: {voter_id}")

def view_voters():
    if not voters:
        print("\nNo registered voters found.")
        return
    
    print("\n=== Registered Voters ===")
    print("Name\t\tContact Number")
    print("-" * 30)
    
    for voter_id, info in voters.items():
        print(f"{info['name']}\t\t{info['contact']}")

def main():
    while True:
        print("\n=== Voter Registration App ===")
        print("1. Register New Voter")
        print("2. View Registered Voters")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            register_voter()
        elif choice == '2':
            view_voters()
        elif choice == '3':
            print("Thank you for using Voter Registration App!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()