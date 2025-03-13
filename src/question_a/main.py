from question_a import use_local_variable


def main():
    num = 100  # Define the variable num
    use_local_variable(num)  # Call the function with num as parameter
    print("The value of num after calling the function:", num) 

if __name__ == '__main__':
    main()
