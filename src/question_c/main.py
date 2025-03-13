import question_c  # Import the global variable and the function

def main():
    # Display and modify the global variable using the function
    print(f"Initial value of global_num: {question_c.get_global_num()}")  # Call the function to get the value
    question_c.use_global()  # Call the function to modify the global variable
    print(f"Modified value of global_num: {question_c.get_global_num()}")  # Call the function again to get the updated value

if __name__ == "__main__":
    main()
