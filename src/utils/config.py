"""Configuration settings for the Meow language."""

VERSION = "1.0.0"
DEBUG = False

# Token configuration
IDENTIFIER_PATTERN = r'[a-zA-Z_][a-zA-Z0-9_]*'
STRING_PATTERN = r'"[^"]*"'
NUMBER_PATTERN = r'\d+(\.\d+)?'
COMMENT_PATTERN = r'%\^.*$'

# File extensions
MEOW_EXTENSION = ".meow"
DEFAULT_ENCODING = "utf-8"

# REPL configuration
PROMPT = "😸 > "
EXIT_COMMAND = "HISSSS"
WELCOME_MESSAGE = "😺 Welcome to Meow REPL! Type HISSSS to exit."

# Error messages
SYNTAX_ERROR = "MEOWCH! Expected {expected} but found {found}"
NAME_ERROR = "😿 Variable '{name}' not found in the litter box!"
TYPE_ERROR = "😾 Can't perform {operation} on {type1} and {type2}" 