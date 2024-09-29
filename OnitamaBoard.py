from Player import Player
from typing import List, Union
from Style import Style
from Pieces import Pieces


class InvalidSizeError(Exception):
    pass


class OnitamaBoard:
    """
    An OnitamaBoard class consisting of a game board, and keeping track of player token information and styles.
    It can set and clear the board and check if potential plays are valid through coordinate checking.

    === Attributes ===
    size : A board's width and height.
    player1 : Player object representing player who will play the G1 and M1 pieces.
    player2 : Player object representing player who will play the G2 and M2 pieces.
    styles :  A list of all possible play styles including: dragon, crab, horse, mantis, rooster.

    === Private Attributes ===
    _board :
        A nested list representing a grid layout for the board.

    === Representation Invariants ===
    - Size is always an odd number greater or equal to 5.
    - player1 has G1 and M1 pieces.
    - player2 has G2 and M2 pieces.
    """
    size: int
    player1: Player
    player2: Player
    styles: List[Style]
    _board: List[List[str]]

    def __init__(self, size: int, player1: Player, player2: Player, board: Union[List[List[str]], None] = None) -> None:
        """
        Constructs an empty Onitama board. Places four monks and one grandmaster
        on opposite sides of the board. Creates five Styles and distributes them
        among the players.
        """
        if (size % 2) == 0 or size < 5:
            raise InvalidSizeError
        self.size = size
        self.player1 = player1
        self.player2 = player2
        self.styles = []
        self.construct_styles()
        if board is None:
            mid = size // 2
            empty = []
            for _ in range(size):
                empty.append([])
            for item in empty:
                for _ in range(size):
                    item.append(Pieces.EMPTY)
            for i in range(size):
                empty[0][i] = Pieces.M1
            empty[0][mid] = Pieces.G1
            for i in range(size):
                empty[size - 1][i] = Pieces.M2
            empty[size - 1][mid] = Pieces.G2
            self._board = empty

        if board is not None:
            self._board = [row.copy() for row in board]

    def construct_styles(self) -> None:
        """
        Constructs the 5 movement styles of Onitama for this board. Normally,
        there are 16 movement styles and they are distributed randomly, however for
        this assignment, you are only required to use 5 of them (Dragon, Crab, Horse,
        Mantis, and Rooster).

        You can find the movement patterns for these styles under assets/{style}.png,
        where {style} is one of the five styles mentioned above. Additionally, you
        can also find the images in README.md.

        IMPORTANT: Additionally, we are going to distribute the styles at the start
        of the game in a static or consistent manner. Player 1 (G1) must get the Crab
        and Horse styles. Player 2 (G2) must get the Mantis and Rooster styles. Extra
        (EMPTY) must get the Dragon style.

        Please be sure to follow the distribution of styles as mentioned above as
        this is important for testing. Failure to follow this distribution of styles
        will result in the LOSS OF A LOT OF MARKS.

        >>> o = OnitamaBoard(5, Player(Pieces.G1), Player(Pieces.G2))
        >>> o.styles = []
        >>> o.styles
        []
        >>> o.construct_styles()
        >>> o.styles[0].name
        'crab'
        >>> o.styles[1].owner
        'X'
        >>> o.styles[4].owner
        ' '
        >>> o.styles[3].get_moves()
        [(0, 1), (0, -1), (-1, 1), (1, -1)]
        """
        # TODO: Your code goes here
        crab = Style([(-1, 0), (0, -2), (0, 2)], 'crab', Pieces.G1)
        horse = Style([(-1, 0), (1, 0), (0, -1)], 'horse', Pieces.G1)
        mantis = Style([(1, 0), (-1, -1), (-1, 1)], 'mantis', Pieces.G2)
        rooster = Style([(0, 1), (0, -1), (-1, 1), (1, -1)], 'rooster', Pieces.G2)
        dragon = Style([(1, -1), (1, 1), (-1, 2), (-1, -2)], 'dragon')
        self.styles.extend([crab, horse, mantis, rooster, dragon])

    def exchange_style(self, style: Style) -> bool:
        """
        Exchange the given <style> with the empty style (the style whose owner is
        EMPTY). Hint: Exchanging will involve swapping the owners of the styles.

        Precondition: <style> cannot be the empty style.
        >>> o = OnitamaBoard(5, Player(Pieces.G1), Player(Pieces.G2))
        >>> style1 = o.styles[0]
        >>> o.exchange_style(style1)
        True
        >>> style1.owner
        ' '
        >>> style2 = o.styles[2]
        >>> o.exchange_style(style2)
        True
        >>> style2.owner
        ' '
        >>> style1.owner
        'Y'
        >>> style2.owner = 'X'
        >>> o.exchange_style(style1)
        False
        """
        # TODO: Your code goes here
        for item in self.styles:
            if item.owner == Pieces.EMPTY:
                item.owner, style.owner = style.owner, Pieces.EMPTY
                return True
        return False

    def valid_coordinate(self, row: int, col: int) -> bool:
        """
        Returns true iff the provided coordinates are valid (exists on the board).
        >>> o = OnitamaBoard(7, Player(Pieces.G1), Player(Pieces.G2))
        >>> o.valid_coordinate(6, 6)
        True
        >>> o.valid_coordinate(5, 7)
        False
        >>> o.valid_coordinate(0, 0)
        True
        >>> o.valid_coordinate(-1, 4)
        False
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            return True
        return False

    def get_token(self, row: int, col: int) -> str:
        """
        Returns the player token that is in the given <row> <col> position, or the empty
        character if no player token is there or if the position provided is invalid.
        >>> o = OnitamaBoard(5, Player(Pieces.G1), Player(Pieces.G2))
        >>> o.get_token(0, 0)
        'x'
        >>> o.get_token(0, 2)
        'X'
        >>> o.get_token(2, 0)
        ' '
        >>> o.get_token(4, 2)
        'Y'
        >>> o.get_token(5, 0)
        ' '
        """
        if self.valid_coordinate(row, col):
            return self._board[row][col]

        return Pieces.EMPTY

    def set_token(self, row: int, col: int, token: str) -> None:
        """
        Sets the given position on the board to be the given player (or throne/empty)
        <token>.
        >>> o = OnitamaBoard(5, Player(Pieces.G1), Player(Pieces.G2))
        >>> o.get_token(0,4)
        'x'
        >>> o.set_token(0, 4, Pieces.EMPTY)
        >>> o.get_token(0, 4)
        ' '
        >>> o.get_token(4, 2)
        'Y'
        >>> o.set_token(4, 2, Pieces.G1)
        >>> o.get_token(4, 2)
        'X'
        >>> o.get_token(5, 0)
        ' '
        >>> o.set_token(5, 0, Pieces.G2)
        >>> o.get_token(5, 0)
        ' '
        """
        if self.valid_coordinate(row, col):
            self._board[row][col] = token
        return None

    def get_styles_deep_copy(self) -> List[Style]:
        """
        DO NOT MODIFY THIS!!!
        Returns a deep copy of the styles of this board.
        """
        return [style.__copy__() for style in self.styles]

    def deep_copy(self) -> List[List[str]]:
        """
        DO NOT MODIFY THIS!!!
        Creates and returns a deep copy of this OnitamaBoard's
        current state.
        """
        return [row.copy() for row in self._board]

    def set_board(self, board: List[List[str]]) -> None:
        """
        DO NOT MODIFY THIS!!!
        Sets the current board's state to the state of the board which is passed in as a parameter.
        """
        self._board = [row.copy() for row in board]

    def __str__(self) -> str:
        """
        Returns a string representation of this game board.
        """
        s = '  '
        for col in range(self.size):
            s += str(col) + ' '

        s += '\n'

        s += ' +'
        for col in range(self.size):
            s += "-+"

        s += '\n'

        for row in range(self.size):
            s += str(row) + '|'
            for col in range(self.size):
                s += self._board[row][col] + '|'

            s += str(row) + '\n'

            s += ' +'
            for col in range(self.size):
                s += '-+'

            s += '\n'

        s += '  '
        for col in range(self.size):
            s += str(col) + ' '

        s += '\n'
        return s
