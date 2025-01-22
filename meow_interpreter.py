import re
from enum import Enum, auto
from typing import List, Tuple, Dict, Any
import random

class TokenType(Enum):
    MEOW = auto()        # Variable declaration
    PURR = auto()        # Print statement
    HISS = auto()        # Exit program
    IDENTIFIER = auto()  # Variable names
    STRING = auto()      # String literals
    NUMBER = auto()      # Numbers
    EQUALS = auto()      # ~= operator
    NEWLINE = auto()     # Line endings
    TAIL = auto()        # Loop keyword
    CATNIP = auto()      # If statement
    ELSE = auto()        # Else statement
    GREATER = auto()     # >:3 operator
    LESS = auto()        # <:3 operator
    LPAREN = auto()      # (
    RPAREN = auto()      # )
    LBRACE = auto()      # {
    RBRACE = auto()      # }
    COMMENT = auto()     # %^ comments
    INCREMENT = auto()   # ^^ operator
    MULTIPLY = auto()     # *:3 operator
    DIVIDE = auto()       # /:3 operator
    PLUS = auto()        # +:3 operator
    MINUS = auto()       # -:3 operator
    MEOWMEOW = auto()    # Function declaration
    RETURN = auto()      # nyaa keyword for return
    COMMA = auto()       # ,
    LBRACKET = auto()    # [
    RBRACKET = auto()    # ]
    ARRAY = auto()       # [^.^]
    NAP = auto()         # Sleep function
    POUNCE = auto()      # Array push
    SCRATCH = auto()     # Array pop
    MEOW_CONCAT = auto() # String concatenation
    LENGTH = auto()      # Array/string length
    SLICE = auto()       # Array/string slice
    REPEAT = auto()      # String repeat
    NOT = auto()         # !:3 operator
    AND = auto()         # &:3 operator
    OR = auto()          # |:3 operator
    PAWWRITE = auto()    # Write to file
    PAWREAD = auto()     # Read from file
    SORT = auto()        # Sort array (purr_sort)
    REVERSE = auto()     # Reverse array (flip_tail)
    SIN = auto()         # sin (purr_sin)
    COS = auto()         # cos (purr_cos)
    TAN = auto()         # tan (purr_tan)
    SQRT = auto()        # sqrt (root_meow)
    LAND = auto()        # catch
    FINALLY = auto()     # finally (groom)
    POW = auto()         # **:3 for power
    MOD = auto()         # %:3 for modulo
    LOG = auto()         # log_meow for logarithm
    ABS = auto()         # paw_abs for absolute value
    FLOOR = auto()       # floor_paw
    CEIL = auto()        # ceiling_paw
    SPLIT = auto()       # yarn_split
    JOIN = auto()        # yarn_join
    REPLACE = auto()     # yarn_replace
    UPPER = auto()       # loud_meow
    LOWER = auto()       # quiet_meow
    MAP = auto()         # paw_map
    FILTER = auto()      # paw_filter
    REDUCE = auto()      # paw_reduce
    FIND = auto()        # find_toy
    COUNT = auto()       # count_toys
    RANDOM = auto()      # random_paw
    CHOICE = auto()      # pick_toy
    SHUFFLE = auto()     # mix_toys

class MeowLexer:
    def __init__(self):
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
            (TokenType.LPAREN, r'\('),
            (TokenType.RPAREN, r'\)'),
            (TokenType.LBRACE, r'\{'),
            (TokenType.RBRACE, r'\}'),
            (TokenType.COMMENT, r'%\^.*$'),
            (TokenType.STRING, r'"[^"]*"'),
            (TokenType.NUMBER, r'\d+'),
            (TokenType.IDENTIFIER, r'[a-zA-Z_][a-zA-Z0-9_]*'),
            (TokenType.NEWLINE, r'\n'),
            (TokenType.MULTIPLY, r'\*:3'),
            (TokenType.DIVIDE, r'/:3'),
            (TokenType.PLUS, r'\+:3'),
            (TokenType.MINUS, r'-:3'),
            (TokenType.MEOWMEOW, r'meowmeow'),
            (TokenType.RETURN, r'nyaa'),
            (TokenType.COMMA, r','),
            (TokenType.LBRACKET, r'\['),
            (TokenType.RBRACKET, r'\]'),
            (TokenType.ARRAY, r'\[\^.\^\]'),
            (TokenType.NAP, r'nap'),
            (TokenType.POUNCE, r'pounce'),
            (TokenType.SCRATCH, r'scratch'),
            (TokenType.MEOW_CONCAT, r'meow_concat'),
            (TokenType.LENGTH, r'whiskers'),
            (TokenType.SLICE, r'claw'),
            (TokenType.REPEAT, r'purr_repeat'),
            (TokenType.NOT, r'!:3'),
            (TokenType.AND, r'&:3'),
            (TokenType.OR, r'\|:3'),
            (TokenType.PAWWRITE, r'pawwrite'),
            (TokenType.PAWREAD, r'pawread'),
            (TokenType.SORT, r'purr_sort'),
            (TokenType.REVERSE, r'flip_tail'),
            (TokenType.SIN, r'purr_sin'),
            (TokenType.COS, r'purr_cos'),
            (TokenType.TAN, r'purr_tan'),
            (TokenType.SQRT, r'root_meow'),
            (TokenType.LAND, r'land'),
            (TokenType.FINALLY, r'groom'),
            (TokenType.POW, r'\*\*:3'),
            (TokenType.MOD, r'%:3'),
            (TokenType.LOG, r'log_meow'),
            (TokenType.ABS, r'paw_abs'),
            (TokenType.FLOOR, r'floor_paw'),
            (TokenType.CEIL, r'ceiling_paw'),
            (TokenType.SPLIT, r'yarn_split'),
            (TokenType.JOIN, r'yarn_join'),
            (TokenType.REPLACE, r'yarn_replace'),
            (TokenType.UPPER, r'loud_meow'),
            (TokenType.LOWER, r'quiet_meow'),
            (TokenType.MAP, r'paw_map'),
            (TokenType.FILTER, r'paw_filter'),
            (TokenType.REDUCE, r'paw_reduce'),
            (TokenType.FIND, r'find_toy'),
            (TokenType.COUNT, r'count_toys'),
            (TokenType.RANDOM, r'random_paw'),
            (TokenType.CHOICE, r'pick_toy'),
            (TokenType.SHUFFLE, r'mix_toys'),
        ]
        # Add some cat-themed error messages
        self.error_messages = [
            "MEOWCH! 🙀 Syntax error at position",
            "Fur-midable error detected at",
            "Paw-don me, but there's an error at",
            "Cat-astrophic syntax error at"
        ]
        
        self.ascii_cats = {
            'function': """
               /\\___/\\
              (  o.o  ) *function defined*
               >  ^  <
            """,
            'array': """
               /\\___/\\ 
              (  =.=  ) *new array created*
               > [] <
            """,
            'math': """
               /\\___/\\
              (  %.%  ) *calculating*
               > == <
            """,
            'sleep': """
               /\\___/\\   zZz
              (  -.-  )  
               >  z  <
            """,
            'array_op': """
               /\\___/\\
              (  >.<  ) *playing with array*
               > [] <
            """,
            'string_op': """
               /\\___/\\
              (  ^o^  ) *meowing intensifies*
               > "" <
            """,
            'file': """
               /\\___/\\
              (  @.@  ) *playing with files*
               > 📁 <
            """,
            'math_func': """
               /\\___/\\
              (  🔢.🔢  ) *doing advanced math*
               > ~~ <
            """,
            'error': """
               /\\___/\\
              (  x.x  ) *caught an error*
               > !! <
            """
        }

    def tokenize(self, code: str) -> List[Tuple[TokenType, str]]:
        tokens = []
        position = 0
        
        while position < len(code):
            match = None
            for token_type, pattern in self.token_patterns:
                regex = re.compile(r'^\s*(' + pattern + r')')
                match = regex.match(code[position:])
                if match:
                    value = match.group(1)
                    if token_type != TokenType.NEWLINE:  # Skip newlines
                        tokens.append((token_type, value))
                    position += match.end()
                    break
            
            if not match:
                if code[position].isspace():
                    position += 1
                    continue
                # Use random cat-themed error message
                error_msg = random.choice(self.error_messages)
                raise SyntaxError(f"{error_msg} {position}: {code[position:]}")

        return tokens

class MeowInterpreter:
    def __init__(self):
        self.variables: Dict[str, Any] = {}
        self.functions: Dict[str, Dict] = {}
        self.lexer = MeowLexer()
        # Add some cat-themed messages
        print("😺 Meow interpreter is purring to life...")
        print("    /\\___/\\   Meow v1.0")
        print("   (  ^.^  )  The Purrfect Programming Language")
        print("    >  o  <   ")
        self.built_ins = {
            'nap': self.nap,
            'pounce': self.pounce,
            'scratch': self.scratch,
            'meow_concat': self.meow_concat,
            'whiskers': self.length,
            'claw': self.slice,
            'purr_repeat': self.repeat,
            'pawwrite': self.pawwrite,
            'pawread': self.pawread,
            'purr_sort': self.purr_sort,
            'flip_tail': self.flip_tail,
            'purr_sin': self.purr_sin,
            'purr_cos': self.purr_cos,
            'purr_tan': self.purr_tan,
            'root_meow': self.root_meow,
            'yarn_split': lambda s, delim: s.split(delim),
            'yarn_join': lambda arr, delim: delim.join(arr),
            'yarn_replace': lambda s, old, new: s.replace(old, new),
            'loud_meow': lambda s: s.upper(),
            'quiet_meow': lambda s: s.lower(),
            'random_paw': random.random,
            'pick_toy': random.choice,
            'mix_toys': random.shuffle,
        }

    def evaluate_condition(self, tokens, i):
        left = self.variables.get(tokens[i][1], tokens[i][1])
        i += 1
        operator = tokens[i][0]
        i += 1
        right = self.variables.get(tokens[i][1], tokens[i][1])
        
        if operator == TokenType.EQUALS:
            return str(left) == str(right), i
        elif operator == TokenType.GREATER:
            return float(left) > float(right), i
        elif operator == TokenType.LESS:
            return float(left) < float(right), i
        
        raise SyntaxError("Unexpected operator in condition! *hisses*")

    def evaluate_math(self, tokens, i):
        left = float(self.variables.get(tokens[i][1], tokens[i][1]))
        i += 1
        operator = tokens[i][0]
        i += 1
        right = float(self.variables.get(tokens[i][1], tokens[i][1]))
        
        print(self.lexer.ascii_cats['math'])
        
        if operator == TokenType.MULTIPLY:
            return left * right, i
        elif operator == TokenType.DIVIDE:
            return left / right, i
        elif operator == TokenType.PLUS:
            return left + right, i
        elif operator == TokenType.MINUS:
            return left - right, i
            
    def create_array(self, tokens, i):
        array = []
        print(self.lexer.ascii_cats['array'])
        
        while tokens[i][0] != TokenType.RBRACKET:
            if tokens[i][0] in (TokenType.STRING, TokenType.NUMBER):
                array.append(tokens[i][1])
            elif tokens[i][0] == TokenType.IDENTIFIER:
                array.append(self.variables.get(tokens[i][1]))
            i += 1
            if tokens[i][0] == TokenType.COMMA:
                i += 1
                
        return array, i
        
    def define_function(self, tokens, i):
        print(self.lexer.ascii_cats['function'])
        
        i += 1  # Skip meowmeow
        func_name = tokens[i][1]
        i += 2  # Skip name and (
        
        params = []
        while tokens[i][0] != TokenType.RPAREN:
            if tokens[i][0] == TokenType.IDENTIFIER:
                params.append(tokens[i][1])
            i += 1
            if tokens[i][0] == TokenType.COMMA:
                i += 1
                
        i += 2  # Skip ) and {
        
        body_start = i
        brace_count = 1
        while brace_count > 0:
            i += 1
            if tokens[i][0] == TokenType.LBRACE:
                brace_count += 1
            elif tokens[i][0] == TokenType.RBRACE:
                brace_count -= 1
                
        self.functions[func_name] = {
            'params': params,
            'body': tokens[body_start:i]
        }
        
        return i

    def nap(self, seconds):
        print(self.lexer.ascii_cats['sleep'])
        import time
        time.sleep(float(seconds))
        print("😺 *yawns* Back from my cat nap!")
        
    def pounce(self, array, item):
        print(self.lexer.ascii_cats['array_op'])
        array.append(item)
        print(f"😺 *pounced on* {item}")
        return array
        
    def scratch(self, array):
        print(self.lexer.ascii_cats['array_op'])
        if array:
            item = array.pop()
            print(f"😺 *scratched off* {item}")
        else:
            print("😿 *sad meow* Nothing to scratch!")
        return array
        
    def meow_concat(self, str1, str2):
        print(self.lexer.ascii_cats['string_op'])
        return str(str1) + str(str2)
        
    def length(self, collection):
        if isinstance(collection, (list, str)):
            return len(collection)
        raise TypeError("😾 Can only count whiskers of strings and arrays!")
        
    def slice(self, collection, start, end=None):
        if isinstance(collection, (list, str)):
            return collection[int(start):int(end) if end else None]
        raise TypeError("😾 Can only use claws on strings and arrays!")
        
    def repeat(self, string, times):
        print(self.lexer.ascii_cats['string_op'])
        return str(string) * int(times)

    def pawwrite(self, filename, content):
        print(self.lexer.ascii_cats['file'])
        try:
            with open(filename, 'w') as f:
                f.write(str(content))
            print(f"😺 *successfully wrote to* {filename}")
        except Exception as e:
            print(f"😿 *failed to write* {str(e)}")
            raise

    def pawread(self, filename):
        print(self.lexer.ascii_cats['file'])
        try:
            with open(filename, 'r') as f:
                content = f.read()
            print(f"😺 *successfully read from* {filename}")
            return content
        except Exception as e:
            print(f"😿 *failed to read* {str(e)}")
            raise

    def purr_sort(self, array, reverse=False):
        print(self.lexer.ascii_cats['array_op'])
        return sorted(array, reverse=reverse)

    def flip_tail(self, array):
        print(self.lexer.ascii_cats['array_op'])
        return array[::-1]

    def purr_sin(self, x):
        print(self.lexer.ascii_cats['math_func'])
        import math
        return math.sin(float(x))

    def purr_cos(self, x):
        print(self.lexer.ascii_cats['math_func'])
        import math
        return math.cos(float(x))

    def purr_tan(self, x):
        print(self.lexer.ascii_cats['math_func'])
        import math
        return math.tan(float(x))

    def root_meow(self, x):
        print(self.lexer.ascii_cats['math_func'])
        import math
        return math.sqrt(float(x))

    def paw_map(self, array, func):
        return [func(x) for x in array]
        
    def paw_filter(self, array, condition):
        return [x for x in array if condition(x)]

    def run(self, code: str):
        print("🐱 Starting to parse your purr-fect code...")
        tokens = self.lexer.tokenize(code)
        i = 0
        while i < len(tokens):
            token_type, value = tokens[i]
            
            if token_type == TokenType.MEOW:
                # Variable declaration
                i += 1
                if i >= len(tokens):
                    raise SyntaxError("Expected variable name after 'meow'")
                
                var_name = tokens[i][1]
                i += 1
                
                if i >= len(tokens) or tokens[i][0] != TokenType.EQUALS:
                    raise SyntaxError("Expected '~=' after variable name")
                i += 1
                
                if i >= len(tokens):
                    raise SyntaxError("Expected value after '~='")
                
                var_value = tokens[i][1]
                # Remove quotes from strings
                if tokens[i][0] == TokenType.STRING:
                    var_value = var_value[1:-1]
                
                self.variables[var_name] = var_value
                
            elif token_type == TokenType.PURR:
                # Print statement
                i += 1
                if i >= len(tokens):
                    raise SyntaxError("MEOWCH! Expected value after PURR 😿")
                
                var_name = tokens[i][1]
                if var_name in self.variables:
                    print(f"😺 *purrs contentedly* {self.variables[var_name]}")
                else:
                    print(f"😿 *sad meow* Variable '{var_name}' not found in the litter box!")
                    
            elif token_type == TokenType.HISS:
                print("🙀 *dramatic cat screech* Program terminated with a HISSSS!")
                print("    /\\___/\\")
                print("   (  o o  )")
                print("   (  =^=  ) ")
                print("    (____)")
                return
                
            elif token_type == TokenType.CATNIP:
                i += 2  # Skip 'catnip' and '('
                condition, i = self.evaluate_condition(tokens, i)
                i += 2  # Skip ')' and '{'
                
                if condition:
                    # Execute the code block
                    while tokens[i][0] != TokenType.RBRACE:
                        i += 1
                else:
                    # Skip to matching '}'
                    while tokens[i][0] != TokenType.RBRACE:
                        i += 1
                        
            elif token_type == TokenType.TAIL:
                # Similar to catnip but with loop logic
                pass
                
            elif token_type == TokenType.MEOWMEOW:
                i = self.define_function(tokens, i)
                
            elif token_type == TokenType.ARRAY:
                i += 1  # Skip [
                array_value, i = self.create_array(tokens, i)
                i += 1  # Skip ]
                
            elif token_type == TokenType.NAP:
                i += 2  # Skip nap and (
                seconds = self.variables.get(tokens[i][1], tokens[i][1])
                self.nap(seconds)
                i += 2  # Skip ) and possible newline
                
            elif token_type in [TokenType.POUNCE, TokenType.SCRATCH, 
                              TokenType.MEOW_CONCAT, TokenType.LENGTH,
                              TokenType.SLICE, TokenType.REPEAT]:
                func = self.built_ins[value]
                i = self.execute_built_in(func, tokens, i)
                
            elif token_type == TokenType.LAND:
                try:
                    # Execute try block
                    i += 2  # Skip land and {
                    while tokens[i][0] != TokenType.RBRACE:
                        self.execute_statement(tokens[i])
                        i += 1
                except Exception as e:
                    print(self.lexer.ascii_cats['error'])
                    # Find and execute catch block
                    while tokens[i][0] != TokenType.FINALLY:
                        i += 1
                    i += 2  # Skip finally and {
                    while tokens[i][0] != TokenType.RBRACE:
                        self.execute_statement(tokens[i])
                        i += 1
                finally:
                    # Execute finally block if it exists
                    if i + 1 < len(tokens) and tokens[i+1][0] == TokenType.FINALLY:
                        i += 3  # Skip groom and {
                        while tokens[i][0] != TokenType.RBRACE:
                            self.execute_statement(tokens[i])
                            i += 1
            
            i += 1

# Example usage
if __name__ == "__main__":
    interpreter = MeowInterpreter()
    
    # Test program
    test_program = """
    %^ Define a function
    meowmeow add_treats(treats, more_treats) {
        nyaa treats +:3 more_treats
    }
    
    %^ Create an array
    meow toy_box ~= [^.^] ["mouse", "ball", "string"]
    
    %^ Do some math
    meow total_treats ~= 5 *:3 2
    
    %^ Create an array of toys
    meow toys ~= [^.^] ["mouse", "ball"]
    
    %^ Add a new toy
    pounce(toys, "yarn")
    
    %^ Remove last toy
    scratch(toys)
    
    %^ String operations
    meow greeting ~= "Meow"
    meow full_greeting ~= meow_concat(greeting, " World!")
    meow loud_meow ~= purr_repeat("MEOW ", 3)
    
    %^ Get array/string length
    meow toy_count ~= whiskers(toys)
    
    %^ Take a cat nap
    nap(1)
    
    %^ Slice an array
    meow some_toys ~= claw(toys, 0, 2)
    
    %^ File I/O
    pawwrite("meow.txt", "Hello from meow!")
    meow content ~= pawread("meow.txt")
    PURR content
    
    %^ Array operations
    meow numbers ~= [^.^] [3, 1, 4, 1, 5]
    meow sorted_nums ~= purr_sort(numbers)
    meow reversed_nums ~= flip_tail(numbers)
    
    %^ Math operations
    meow angle ~= 3.14159
    meow sine ~= purr_sin(angle)
    meow cosine ~= purr_cos(angle)
    meow square ~= root_meow(16)
    
    %^ Exception handling
    pounce {
        meow bad_file ~= pawread("nonexistent.txt")
    } land {
        PURR "Caught the error like a pro cat! 😺"
    } groom {
        PURR "Always clean up after playing! 🧹"
    }
    
    PURR total_treats
    PURR toy_box
    PURR toy_count
    PURR full_greeting
    PURR loud_meow
    PURR some_toys
    PURR content
    PURR sorted_nums
    PURR reversed_nums
    PURR sine
    PURR cosine
    PURR square
    
    HISSSS
    """
    
    interpreter.run(test_program) 