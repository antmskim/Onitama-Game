from typing import List, Tuple, Optional
from Style import Style


class OnitamaStack:
    """An OnitamaStack class.

    Stores data in a last-in, first-out order. When removing an item from the
    stack, the most recently-added item is the one that is removed.

    === Private Attributes ===
    _item: a list of elements in the stack.
           The end of the list represents the top of the stack.
    """
    _items: List

    def __init__(self) -> None:
        """Initialize a new empty stack."""
        self._items = []

    def empty(self) -> bool:
        """Return whether this stack contains no items.
        >>> s = OnitamaStack()
        >>> s.empty()
        True
        """
        return self._items == []

    def push(self, board: List[List[str]], style: List[Style]) -> None:
        """Add a new element to the top of this stack.
        >>> s = OnitamaStack()
        >>> s.empty()
        True
        >>> b = [['x', 'x', 'X', 'x', 'x'], [' ', ' ', ' ', ' ', ' '],\
         [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],\
         ['y', 'y', 'Y', 'y', 'y']]
        >>> sty = [Style([(-1, 0), (0, -2), (0, 2)], 'crab', 'X')]
        >>> s.push(b, sty)
        >>> s.empty()
        False
        """
        self._items.append((board, style))

    def pop(self) -> Optional[Tuple]:
        """
        Remove and return the element at the top of this stack.
        Returns None if this stack is empty.
        >>> s = OnitamaStack()
        >>> s.pop()
        >>> b = [['x', 'x', 'X', 'x', 'x'], [' ', ' ', ' ', ' ', ' '],\
         [' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' '],\
         ['y', 'y', 'Y', 'y', 'y']]
        >>> sty = [Style([(-1, 0), (0, -2), (0, 2)], 'crab', 'X')]
        >>> s.push(b, sty)
        >>> s.pop() == (b, sty)
        True
        >>> s.empty()
        True
        """
        if not self.empty():
            return self._items.pop()
