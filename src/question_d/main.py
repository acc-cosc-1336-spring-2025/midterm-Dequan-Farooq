#add import
import question_d

def main():
    while True:
        age = input("Enter the person's age (or type 'exit' to quit): ")
        
        if age.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            age = int(age)  # Convert input to an integer
            category = question_d.get_person_category(age)
            print(f"The person is: {category}")
        except ValueError:
            print("Invalid input, please enter a valid number.")

# Run the main program
main()