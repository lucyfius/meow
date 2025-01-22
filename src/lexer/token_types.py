from enum import Enum, auto

class TokenType(Enum):
    # Variable and Control Flow
    MEOW = auto()        # Variable declaration
    PURR = auto()        # Print statement
    HISS = auto()        # Exit program
    TAIL = auto()        # Loop keyword
    CATNIP = auto()      # If statement
    ELSE = auto()        # Else statement
    
    # Basic Types
    IDENTIFIER = auto()  # Variable names
    STRING = auto()      # String literals
    NUMBER = auto()      # Numbers
    
    # Operators
    EQUALS = auto()      # ~= operator
    GREATER = auto()     # >:3 operator
    LESS = auto()        # <:3 operator
    INCREMENT = auto()   # ^^ operator
    
    # Math Operators
    MULTIPLY = auto()    # *:3 operator
    DIVIDE = auto()      # /:3 operator
    PLUS = auto()        # +:3 operator
    MINUS = auto()       # -:3 operator
    POW = auto()        # **:3 operator
    MOD = auto()        # %:3 operator
    
    # Function Related
    MEOWMEOW = auto()   # Function declaration
    RETURN = auto()      # nyaa keyword
    
    # Syntax Elements
    COMMA = auto()      # ,
    LPAREN = auto()     # (
    RPAREN = auto()     # )
    LBRACE = auto()     # {
    RBRACE = auto()     # }
    LBRACKET = auto()   # [
    RBRACKET = auto()   # ]
    NEWLINE = auto()    # Line endings
    COMMENT = auto()    # %^ comments
    
    # Data Structures
    ARRAY = auto()      # [^.^]
    
    # Built-in Functions
    NAP = auto()        # Sleep function
    POUNCE = auto()     # Array push
    SCRATCH = auto()    # Array pop
    
    # String Operations
    MEOW_CONCAT = auto() # String concatenation
    LENGTH = auto()      # Array/string length
    SLICE = auto()       # Array/string slice
    REPEAT = auto()      # String repeat
    SPLIT = auto()       # yarn_split
    JOIN = auto()        # yarn_join
    REPLACE = auto()     # yarn_replace
    UPPER = auto()       # loud_meow
    LOWER = auto()       # quiet_meow
    
    # Math Functions
    SIN = auto()        # purr_sin
    COS = auto()        # purr_cos
    TAN = auto()        # purr_tan
    SQRT = auto()       # root_meow
    LOG = auto()        # log_meow
    ABS = auto()        # paw_abs
    FLOOR = auto()      # floor_paw
    CEIL = auto()       # ceiling_paw
    
    # Array Operations
    MAP = auto()        # paw_map
    FILTER = auto()     # paw_filter
    REDUCE = auto()     # paw_reduce
    FIND = auto()       # find_toy
    COUNT = auto()      # count_toys
    SORT = auto()       # purr_sort
    REVERSE = auto()    # flip_tail
    
    # Random Operations
    RANDOM = auto()     # random_paw
    CHOICE = auto()     # pick_toy
    SHUFFLE = auto()    # mix_toys
    
    # Error Handling
    LAND = auto()       # catch
    FINALLY = auto()    # finally (groom) 