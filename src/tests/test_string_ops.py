import unittest
from ..interpreter.builtins.string_ops import MeowStringOps

class TestMeowStringOps(unittest.TestCase):
    def setUp(self):
        self.string_ops = MeowStringOps()
        
    def test_meow_concat(self):
        result = self.string_ops.meow_concat("Meow", " World!")
        self.assertEqual(result, "Meow World!")
        
    def test_purr_repeat(self):
        result = self.string_ops.purr_repeat("Meow ", 3)
        self.assertEqual(result, "Meow Meow Meow ")
        
    def test_yarn_split(self):
        result = self.string_ops.yarn_split("cat,dog,fish", ",")
        self.assertEqual(result, ["cat", "dog", "fish"])
        
    def test_yarn_join(self):
        result = self.string_ops.yarn_join(["cat", "dog", "fish"], ", ")
        self.assertEqual(result, "cat, dog, fish") 