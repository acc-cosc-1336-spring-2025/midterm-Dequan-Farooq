import sys
import unittest
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../src'))

from question_d.question_d import get_person_category 
from question_b.question_b import is_prime
from question_a.question_a import use_local_variable
from question_c.question_c import use_global, get_global_num



class TestPersonCategory(unittest.TestCase):

    def test_get_person_category(self):
        self.assertEqual(get_person_category(1), "infant", "Test failed for age 1")
        self.assertEqual(get_person_category(2), "child", "Test failed for age 2")
        self.assertEqual(get_person_category(14), "teenager", "Test failed for age 14")
        self.assertEqual(get_person_category(20), "adult", "Test failed for age 20")
        self.assertEqual(get_person_category(-1), "Invalid number", "Test failed for negative age")
        self.assertEqual(get_person_category(130), "Invalid number", "Test failed for age greater than 125")
class TestValueFunction(unittest.TestCase):
    def test_is_prime_4(self):
        self.assertFalse(is_prime(4), "Test failed for number 4")
    
    def test_is_prime_5(self):
        self.assertTrue(is_prime(5), "Test failed for number 5")
    
    def test_is_prime_11(self):
        self.assertTrue(is_prime(11), "Test failed for number 11")

class TestUseLocalVariable(unittest.TestCase):
    def test_local_variable(self):
        num = 100  # Variable outside the function
        use_local_variable(num)  # Call the function with num as parameter
        self.assertEqual(num, 100)
      

class TestGlobalVariable(unittest.TestCase):
    
    def test_use_global(self):
        # Assert the initial value of global_num
        self.assertEqual(get_global_num(), 10, "Initial value of global_num should be 10")

        
        # Call the function to modify the global variable
        use_global()
        
        # Assert that the global_num is now 20
        self.assertEqual(get_global_num(), 20, "global_num should be 20 after calling use_global")


# Run the tests
if __name__ == "__main__":
    unittest.main()