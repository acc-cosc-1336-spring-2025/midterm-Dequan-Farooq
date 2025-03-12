#add import
import question_b

def main():
    while True:
        
        user_input = input("Enter a number to check if it's prime (or type 'quit' to exit): ")

        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

       
        if user_input.isdigit():
            num = int(user_input)
            
            if question_b.is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        else:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
