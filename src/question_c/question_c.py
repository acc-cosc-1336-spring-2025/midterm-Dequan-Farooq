
global_num = 10  


def use_global():
    global global_num 
    global_num = 20  


def test_use_global():
    global global_num  
    use_global()  

    
    assert global_num == 20, f"Test failed! global_num should be 20 but got {global_num}"
    print("Test passed: global_num is now", global_num)  
