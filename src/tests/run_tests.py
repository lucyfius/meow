import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test_array_ops import TestMeowArrayOps
from test_string_ops import TestMeowStringOps
from test_math_ops import TestMeowMathOps
from test_file_ops import TestMeowFileOps

def run_tests():
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMeowArrayOps))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMeowStringOps))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMeowMathOps))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMeowFileOps))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    print("🐱 Running Meow Language Tests...")
    result = runner.run(test_suite)
    
    if result.wasSuccessful():
        print("😺 All tests passed! Purrfect!")
    else:
        print("😿 Some tests failed! Time to chase some bugs!")
        
if __name__ == "__main__":
    run_tests() 