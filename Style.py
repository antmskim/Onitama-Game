from __future__ import annotations
from typing import List, Tuple, Union
from Pieces import Pieces


class Style:
    """
    A Style class represents play styles in Onitama.
    Each style has a name including: dragon, crab, horse, mantis, rooster,
    an owner and pairs of possible moves.

    === Attributes ===
    name: the name of the Style
    owner: the owner of the Style

    === Private Attributes ===
    _moves: the list of move pairs the Style has
    """
    name: str
    owner: Union[str]
    _moves: List[Tuple]

    def __init__(self, pairs: List[Tuple], name: str, owner: Union[str, None] = Pieces.EMPTY) -> None:
        """
        Initialize a style.
        Sets the <_moves> to the copy of <pairs>
        """
        self.name = name
        self._moves = pairs.copy()
        self.owner = owner

    def get_moves(self) -> List[Tuple]:
        """
        Returns a deep copy of the list of this Style's move pairs.
        """
        return self._moves.copy()

    def __eq__(self, other: Style) -> bool:
        """
        Compares the Style with the <other> given Style.
        """
        return self.name == other.name and self.owner == other.owner

    def __copy__(self) -> Style:
        """
        Returns a deep copy of the Style.
        """
        return Style(self._moves.copy(), self.name, self.owner)
