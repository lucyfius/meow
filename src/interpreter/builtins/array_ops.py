"""Array operations for the Meow language."""
from typing import List, Any, Callable, TypeVar, Optional

T = TypeVar('T')

class MeowArrayOps:
    def __init__(self, interpreter):
        self.interpreter = interpreter

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

    def purr_sort(self, array: List[T], reverse: bool = False) -> List[T]:
        """Sort array in ascending or descending order."""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        return sorted(array, reverse=reverse)

    def flip_tail(self, array: List[T]) -> List[T]:
        """Reverse array order."""
        print(self.interpreter.lexer.ascii_cats['array_op'])
        return array[::-1]

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