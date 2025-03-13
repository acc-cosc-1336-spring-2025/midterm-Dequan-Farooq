global_num = 10

# Function to modify the global variable using globals()
def use_global():
    globals()['global_num'] = 20  # Modify the global variable

# Helper function to retrieve the current value of global_num
def get_global_num():
    return globals()['global_num'] 