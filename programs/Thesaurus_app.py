# Initialize thesaurus dictionary with some sample data
thesaurus = {
    "happy": ["joyful", "pleased", "delighted", "cheerful"],
    "sad": ["unhappy", "depressed", "gloomy", "miserable"],
    "big": ["large", "huge", "enormous", "gigantic"],
    "small": ["tiny", "little", "miniature", "compact"]
}

def get_synonyms(word):
    return thesaurus.get(word.lower(), [])

def add_word(word, synonyms):
    thesaurus[word.lower()] = [syn.lower() for syn in synonyms]

def display_all():
    for word, synonyms in thesaurus.items():
        print(f"\n{word.capitalize()}: {', '.join(synonyms)}")

def main():
    while True:
        print("\n=== Thesaurus App ===")
        print("1. Look up synonyms")
        print("2. Add new word")
        print("3. Display all")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            word = input("Enter word to look up: ")
            synonyms = get_synonyms(word)
            if synonyms:
                print(f"Synonyms for {word}: {', '.join(synonyms)}")
            else:
                print("Word not found in thesaurus.")
                
        elif choice == '2':
            word = input("Enter new word: ")
            synonyms = input("Enter synonyms (comma-separated): ").split(',')
            add_word(word, synonyms)
            print("Word added successfully!")
            
        elif choice == '3':
            display_all()
            
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()