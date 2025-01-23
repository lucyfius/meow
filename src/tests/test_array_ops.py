import unittest
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from interpreter.builtins.array_ops import MeowArrayOps
from interpreter.interpreter import MeowInterpreter

class TestMeowArrayOps(unittest.TestCase):
    def setUp(self):
        self.interpreter = MeowInterpreter()
        self.array_ops = MeowArrayOps(self.interpreter)
        
    def test_furball_hairball(self):
        """Test stack operations"""
        array = ["mouse", "ball"]
        # Add to stack
        result = self.array_ops.furball(array, "yarn")
        self.assertEqual(result, ["mouse", "ball", "yarn"])
        # Remove from stack
        result = self.array_ops.hairball(result)
        self.assertEqual(result, ["mouse", "ball"])

    def test_nhom_shit(self):
        """Test queue operations"""
        array = ["mouse", "ball"]
        # Add to queue
        result = self.array_ops.nhom(array, "yarn")
        self.assertEqual(result, ["yarn", "mouse", "ball"])
        # Remove from queue
        result = self.array_ops.shit(result)
        self.assertEqual(result, ["yarn", "mouse"])

    def test_roll(self):
        """Test array reversal"""
        array = [1, 2, 3]
        result = self.array_ops.roll(array)
        self.assertEqual(result, [3, 2, 1])
        
    def test_purr_sort(self):
        array = [3, 1, 4, 1, 5]
        result = self.array_ops.purr_sort(array)
        self.assertEqual(result, [1, 1, 3, 4, 5])
        
    def test_flip_tail(self):
        array = [1, 2, 3]
        result = self.array_ops.flip_tail(array)
        self.assertEqual(result, [3, 2, 1]) 