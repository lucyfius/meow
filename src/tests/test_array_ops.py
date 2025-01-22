import unittest
from ..interpreter.builtins.array_ops import MeowArrayOps
from ..interpreter.interpreter import MeowInterpreter

class TestMeowArrayOps(unittest.TestCase):
    def setUp(self):
        self.interpreter = MeowInterpreter()
        self.array_ops = MeowArrayOps(self.interpreter)
        
    def test_pounce(self):
        array = ["mouse", "ball"]
        result = self.array_ops.pounce(array, "yarn")
        self.assertEqual(result, ["mouse", "ball", "yarn"])
        
    def test_scratch(self):
        array = ["mouse", "ball", "yarn"]
        result = self.array_ops.scratch(array)
        self.assertEqual(result, ["mouse", "ball"])
        
    def test_purr_sort(self):
        array = [3, 1, 4, 1, 5]
        result = self.array_ops.purr_sort(array)
        self.assertEqual(result, [1, 1, 3, 4, 5])
        
    def test_flip_tail(self):
        array = [1, 2, 3]
        result = self.array_ops.flip_tail(array)
        self.assertEqual(result, [3, 2, 1]) 