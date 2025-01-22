"""File operations for the Meow language."""
from typing import Optional, Union, TextIO
from ...utils.config import DEFAULT_ENCODING

class MeowFileOps:
    def __init__(self, interpreter):
        self.interpreter = interpreter

    def pawwrite(self, filename: str, content: str) -> None:
        """Write content to file."""
        print(self.interpreter.lexer.ascii_cats['file'])
        try:
            with open(filename, 'w', encoding=DEFAULT_ENCODING) as f:
                f.write(str(content))
            print(f"😺 *successfully wrote to* {filename}")
        except Exception as e:
            print(f"😿 *failed to write* {str(e)}")
            raise

    def pawread(self, filename: str) -> str:
        """Read content from file."""
        print(self.interpreter.lexer.ascii_cats['file'])
        try:
            with open(filename, 'r', encoding=DEFAULT_ENCODING) as f:
                content = f.read()
            print(f"😺 *successfully read from* {filename}")
            return content
        except Exception as e:
            print(f"😿 *failed to read* {str(e)}")
            raise

    def pawappend(self, filename: str, content: str) -> None:
        """Append content to file."""
        print(self.interpreter.lexer.ascii_cats['file'])
        try:
            with open(filename, 'a', encoding=DEFAULT_ENCODING) as f:
                f.write(str(content))
            print(f"😺 *successfully appended to* {filename}")
        except Exception as e:
            print(f"😿 *failed to append* {str(e)}")
            raise 