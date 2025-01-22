import re
from typing import List, Tuple, Dict
from .token_types import TokenType

class MeowLexer:
    def __init__(self):
        # ASCII art for different operations
        self.ascii_cats = {
            'error': """
               /\\___/\\
              (  o o  )
              (  =^=  ) ERROR!
               (______)
            """,
            'array_op': """
               /\\___/\\
              (  - -  )
              (  =^=  ) Array Operation
               (______)
            """,
            'string_op': """
               /\\___/\\
              (  o o  )
              (  =w=  ) String Operation
               (______)
            """,
            'sleep': """
               /\\___/\\
              (  -.-  )
              (  =^=  ) zZzZz
               (______)
            """
        }

        # Token patterns for lexical analysis
        self.token_patterns = [
            (TokenType.MEOW, r'meow'),
            (TokenType.PURR, r'PURR'),
            (TokenType.HISS, r'HISSSS'),
            (TokenType.EQUALS, r'~='),
            (TokenType.TAIL, r'tail'),
            (TokenType.CATNIP, r'catnip'),
            (TokenType.ELSE, r'else'),
            (TokenType.GREATER, r'>:3'),
            (TokenType.LESS, r'<:3'),
            (TokenType.INCREMENT, r'\^\^'),
            (TokenType.MULTIPLY, r'\*:3'),
            (TokenType.DIVIDE, r'/:3'),
            (TokenType.PLUS, r'\+:3'),
            (TokenType.MINUS, r'-:3'),
            (TokenType.POW, r'\*\*:3'),
            (TokenType.MOD, r'%:3'),
            (TokenType.NOT, r'!:3'),
            (TokenType.AND, r'&:3'),
            (TokenType.OR, r'\|:3'),
            (TokenType.MEOWMEOW, r'meowmeow'),
            (TokenType.RETURN, r'nyaa'),
            (TokenType.ARRAY, r'\[\^.\^\]'),
            (TokenType.NAP, r'nap'),
            (TokenType.POUNCE, r'pounce'),
            (TokenType.SCRATCH, r'scratch'),
            (TokenType.MEOW_CONCAT, r'meow_concat'),
            (TokenType.LENGTH, r'whiskers'),
            (TokenType.SLICE, r'claw'),
            (TokenType.REPEAT, r'purr_repeat'),
            (TokenType.PAWWRITE, r'pawwrite'),
            (TokenType.PAWREAD, r'pawread'),
            (TokenType.SORT, r'purr_sort'),
            (TokenType.REVERSE, r'flip_tail'),
            (TokenType.SIN, r'purr_sin'),
            (TokenType.COS, r'purr_cos'),
            (TokenType.TAN, r'purr_tan'),
            (TokenType.SQRT, r'root_meow'),
            (TokenType.LOG, r'log_meow'),
            (TokenType.ABS, r'paw_abs'),
            (TokenType.FLOOR, r'floor_paw'),
            (TokenType.CEIL, r'ceiling_paw'),
            # Syntax elements
            (TokenType.LPAREN, r'\('),
            (TokenType.RPAREN, r'\)'),
            (TokenType.LBRACE, r'\{'),
            (TokenType.RBRACE, r'\}'),
            (TokenType.LBRACKET, r'\['),
            (TokenType.RBRACKET, r'\]'),
            (TokenType.COMMA, r','),
            (TokenType.COMMENT, r'%\^.*$'),
            (TokenType.STRING, r'"[^"]*"'),
            (TokenType.NUMBER, r'\d+(\.\d+)?'),
            (TokenType.IDENTIFIER, r'[a-zA-Z_][a-zA-Z0-9_]*'),
            (TokenType.NEWLINE, r'\n'),
        ]

    def tokenize(self, code: str) -> List[Tuple[TokenType, str]]:
        """Convert source code into a list of tokens."""
        tokens = []
        position = 0
        
        while position < len(code):
            match = None
            
            # Skip whitespace
            if code[position].isspace() and code[position] != '\n':
                position += 1
                continue
                
            # Try to match each pattern
            for token_type, pattern in self.token_patterns:
                regex = re.compile(pattern)
                match = regex.match(code, position)
                
                if match:
                    value = match.group(0)
                    if token_type != TokenType.COMMENT:  # Skip comments
                        tokens.append((token_type, value))
                    position = match.end()
                    break
                    
            if not match:
                raise SyntaxError(f"Invalid syntax at position {position}: {code[position:position+10]}...")
                
        return tokens 