import time
import math
import random
from typing import Any, List

class MeowBuiltins:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        
    def nap(self, seconds: float) -> None:
        """Pause execution for specified seconds."""
        print(self.interpreter.lexer.ascii_cats['sleep'])
        time.sleep(float(seconds))
        print("😺 *yawns* Back from my cat nap!")
        
    def pounce(self, array: List[Any], item: Any) -> List[Any]:
        """Add item to array."""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        array.append(item)
        print(f"😺 *pounced on* {item}")
        return array
        
    def scratch(self, array: List[Any]) -> List[Any]:
        """Remove and return last item from array."""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        if array:
            item = array.pop()
            print(f"😺 *scratched off* {item}")
        else:
            print("😿 *sad meow* Nothing to scratch!")
        return array

    # Math operations
    def purr_sin(self, x: float) -> float:
        return math.sin(float(x))
        
    def purr_cos(self, x: float) -> float:
        return math.cos(float(x))
        
    def purr_tan(self, x: float) -> float:
        return math.tan(float(x))
        
    def root_meow(self, x: float) -> float:
        return math.sqrt(float(x))

    # String operations
    def meow_concat(self, str1: str, str2: str) -> str:
        print(self.interpreter.lexer.ascii_cats['string_op'])
        return str(str1) + str(str2)
        
    def purr_repeat(self, string: str, times: int) -> str:
        return str(string) * int(times) 