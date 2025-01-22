"""Mathematical operations for the Meow language."""
import math
from typing import Union

class MeowMathOps:
    @staticmethod
    def purr_sin(x: Union[int, float]) -> float:
        """Compute sine of a number."""
        return math.sin(float(x))
        
    @staticmethod
    def purr_cos(x: Union[int, float]) -> float:
        """Compute cosine of a number."""
        return math.cos(float(x))
        
    @staticmethod
    def purr_tan(x: Union[int, float]) -> float:
        """Compute tangent of a number."""
        return math.tan(float(x))
        
    @staticmethod
    def root_meow(x: Union[int, float]) -> float:
        """Compute square root of a number."""
        return math.sqrt(float(x))
        
    @staticmethod
    def log_meow(x: Union[int, float]) -> float:
        """Compute natural logarithm of a number."""
        return math.log(float(x)) 