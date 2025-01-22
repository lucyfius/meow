import unittest
import math
from ..interpreter.builtins.math_ops import MeowMathOps

class TestMeowMathOps(unittest.TestCase):
    def setUp(self):
        self.math_ops = MeowMathOps()
        
    def test_purr_sin(self):
        result = self.math_ops.purr_sin(math.pi/2)
        self.assertAlmostEqual(result, 1.0)
        
    def test_purr_cos(self):
        result = self.math_ops.purr_cos(0)
        self.assertAlmostEqual(result, 1.0)
        
    def test_root_meow(self):
        result = self.math_ops.root_meow(16)
        self.assertEqual(result, 4.0)
        
    def test_log_meow(self):
        result = self.math_ops.log_meow(math.e)
        self.assertAlmostEqual(result, 1.0) 