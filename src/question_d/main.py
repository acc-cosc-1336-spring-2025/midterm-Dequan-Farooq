import question_d

def main():
    # Testing the get_person_category function
    age = 25  # Example age
    category = question_d.get_person_category(age)  # Call the function
    
    # Display the result
    print(f"The category for age {age} is: {category}")

# Run the main program
if __name__ == '__main__':
    main()