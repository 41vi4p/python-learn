#Grocery List App:
# This app allows users to add items, view the list, remove items, and clear the list.
version = 0.2
grocery_list = {}  # Dictionary to store item:quantity pairs

def add_item():
    item = input("Enter item name: ").strip().lower()
    try:
        quantity = int(input("Enter quantity: "))
        grocery_list[item] = grocery_list.get(item, 0) + quantity
        print(f"\n{quantity} {item}(s) added to list")
    except ValueError:
        print("Please enter a valid quantity")

def remove_item():
    if not grocery_list:
        print("\nList is empty!")
        return
        
    item = input("Enter item to remove: ").strip().lower()
    if item in grocery_list:
        del grocery_list[item]
        print(f"\n{item} removed from list")
    else:
        print("\nItem not found in list")

def view_list():
    if not grocery_list:
        print("\nGrocery list is empty!")
        return
        
    print("\nCurrent Grocery List:")
    print("-" * 20)
    for item, quantity in grocery_list.items():
        print(f"{item}: {quantity}")
    print("-" * 20)

def clear_list():
    grocery_list.clear()
    print("\nGrocery list cleared!")

def main():
    while True:
        print("\nGrocery List App v"+str(version)+" by 41vi4p\n")
        print("\nGrocery List Menu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View List")
        print("4. Clear List")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_list()
        elif choice == '4':
            clear_list()
        elif choice == '5':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()

