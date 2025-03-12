def use_local_variable(num):
    num = 10  # Local variable inside the function, doesn't affect the outer variable


def test_use_local_variable():
    num = 100  # Variable outside the function
    use_local_variable(num)  # Pass the variable to the function

    print("Value of num in the test case:", num)  # Expected output: 100
    

