import unittest
import os
from ..interpreter.builtins.file_ops import MeowFileOps
from ..interpreter.interpreter import MeowInterpreter

class TestMeowFileOps(unittest.TestCase):
    def setUp(self):
        self.interpreter = MeowInterpreter()
        self.file_ops = MeowFileOps(self.interpreter)
        self.test_file = "test_meow.txt"
        
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
            
    def test_pawwrite_pawread(self):
        content = "Hello from Meow!"
        self.file_ops.pawwrite(self.test_file, content)
        result = self.file_ops.pawread(self.test_file)
        self.assertEqual(result, content)
        
    def test_pawappend(self):
        content1 = "First line\n"
        content2 = "Second line"
        self.file_ops.pawwrite(self.test_file, content1)
        self.file_ops.pawappend(self.test_file, content2)
        result = self.file_ops.pawread(self.test_file)
        self.assertEqual(result, content1 + content2) 