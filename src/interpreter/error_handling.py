class MeowError(Exception):
    """Base class for Meow language errors."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class MeowSyntaxError(MeowError):
    """Raised when there's a syntax error in the Meow code."""
    pass

class MeowRuntimeError(MeowError):
    """Raised when there's a runtime error in the Meow code."""
    pass

class MeowNameError(MeowError):
    """Raised when a variable or function is not found."""
    pass

class MeowTypeError(MeowError):
    """Raised when an operation is performed on incompatible types."""
    pass 