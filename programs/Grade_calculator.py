def get_grades():
    grades = []
    while True:
        grade = input("Enter a grade (or 'e' to end): ")
        if grade.lower() == 'e':
            break
        try:
            grade = float(grade)
            if 0 <= grade <= 100:
                grades.append(grade)
            else:
                print("Please enter a grade between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    return grades

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def determine_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'E'

def main():
    grades = get_grades()
    if not grades:
        print("No grades entered.")
        return

    grades.sort()
    print("Sorted grades:", grades)

    average = calculate_average(grades)
    print("Average grade:", average)

    letter_grade = determine_letter_grade(average)
    print("Letter grade:", letter_grade)

if __name__ == "__main__":
    main()