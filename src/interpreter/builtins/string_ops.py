"""String operations for the Meow language."""
from typing import List

class MeowStringOps:
    @staticmethod
    def meow_concat(str1: str, str2: str) -> str:
        """Concatenate two strings."""
        return str(str1) + str(str2)
        
    @staticmethod
    def purr_repeat(string: str, times: int) -> str:
        """Repeat a string multiple times."""
        return str(string) * int(times)
        
    @staticmethod
    def yarn_split(string: str, delimiter: str) -> List[str]:
        """Split a string by delimiter."""
        return str(string).split(delimiter)
        
    @staticmethod
    def yarn_join(strings: List[str], delimiter: str) -> str:
        """Join strings with delimiter."""
        return delimiter.join(map(str, strings)) 