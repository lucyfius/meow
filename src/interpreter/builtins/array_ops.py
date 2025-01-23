"""Array operations for the Meow language."""
from typing import List, Any, Callable, TypeVar, Optional
from collections import deque

T = TypeVar('T')

class MeowArrayOps:
    def __init__(self, interpreter):
        self.interpreter = interpreter

    # Stack operations (LIFO)
    def furball(self, array: List[Any], item: Any) -> List[Any]:
        """Push item onto stack (LIFO).
        Like a cat coughing up a furball - it comes out last!"""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        array.append(item)
        print(f"😺 *coughed up a furball* {item}")
        return array
        
    def hairball(self, array: List[Any]) -> List[Any]:
        """Pop item from stack (LIFO).
        Like a cat bringing up a hairball - takes from the top!"""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        if array:
            item = array.pop()
            print(f"😺 *hacked up* {item}")
        else:
            print("😿 *dry heaves* Nothing to bring up!")
        return array

    # Queue operations (FIFO)
    def nhom(self, array: List[Any], item: Any) -> List[Any]:
        """Add item to queue (FIFO).
        Like a cat eating food - goes in first!"""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        array.insert(0, item)
        print(f"😺 *nom nom* ate {item}")
        return array
        
    def shit(self, array: List[Any]) -> List[Any]:
        """Remove item from queue (FIFO).
        Like a cat's digestion - first in, first out!"""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        if array:
            item = array.pop()
            print(f"😺 *used litterbox* disposed of {item}")
        else:
            print("😿 *empty tummy* Nothing to process!")
        return array

    def roll(self, array: List[T]) -> List[T]:
        """Reverse array order.
        Like a cat rolling over!"""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        return array[::-1]

    def purr_sort(self, array: List[T], reverse: bool = False) -> List[T]:
        """Sort array in ascending or descending order."""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        return sorted(array, reverse=reverse)

    def whiskers(self, collection: List[Any]) -> int:
        """Get length of array."""
        if not isinstance(collection, (list, str)):
            raise TypeError("😾 Can only count whiskers of strings and arrays!")
        return len(collection)

    def claw(self, collection: List[T], start: int, end: Optional[int] = None) -> List[T]:
        """Slice array."""
        if not isinstance(collection, (list, str)):
            raise TypeError("😾 Can only use claws on strings and arrays!")
        return collection[int(start):int(end) if end else None]

    def paw_map(self, array: List[T], func: Callable[[T], Any]) -> List[Any]:
        """Apply function to each element."""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        return [func(x) for x in array]
        
    def paw_filter(self, array: List[T], condition: Callable[[T], bool]) -> List[T]:
        """Filter array based on condition."""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        return [x for x in array if condition(x)]

    def paw_reduce(self, array: List[T], func: Callable[[T, T], T], initial: Optional[T] = None) -> T:
        """Reduce array to single value using function."""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        if initial is not None:
            result = initial
            for x in array:
                result = func(result, x)
            return result
        elif array:
            result = array[0]
            for x in array[1:]:
                result = func(result, x)
            return result
        raise ValueError("😿 Cannot reduce empty array without initial value!")

    def find_toy(self, array: List[T], item: T) -> Optional[int]:
        """Find index of item in array."""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        try:
            return array.index(item)
        except ValueError:
            return None

    def count_toys(self, array: List[T], item: T) -> int:
        """Count occurrences of item in array."""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        return array.count(item) 