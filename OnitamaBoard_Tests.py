import pytest
from OnitamaBoard import OnitamaBoard
from Pieces import Pieces
from Player import Player

board1 = [['x', ' ', 'X', 'x', 'x'],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', 'x', ' '],
          [' ', 'y', ' ', ' ', ' '],
          ['y', ' ', 'Y', 'y', 'y']]


def test_construct_styles():
    onitama = OnitamaBoard(5, Player(Pieces.G1), Player(Pieces.G2))
    onitama.styles = []
    assert onitama.styles == []
    onitama.construct_styles()
    assert onitama.styles != []
    for style in onitama.styles:
        if style.name == 'crab':
            assert style.owner == Pieces.G1
        if style.name == 'rooster':
            assert style.owner == Pieces.G2


def test_exchange_styles():
    onitama = OnitamaBoard(5, Player(Pieces.G1), Player(Pieces.G2))
    random = onitama.styles[0]
    assert onitama.exchange_style(random) == True
    assert random.owner == ' '


def test_exchange_styles_invalid():
    onitama = OnitamaBoard(5, Player(Pieces.G1), Player(Pieces.G2))
    random = onitama.styles[0]
    for sty in onitama.styles:
        if sty.owner == Pieces.EMPTY:
            sty.owner = Pieces.G1

    assert onitama.exchange_style(random) == False
    assert random.owner != ' '


def test_valid_coordinate():
    onitama = OnitamaBoard(9, Player(Pieces.G1), Player(Pieces.G2))
    assert onitama.valid_coordinate(0, 0) == True
    assert onitama.valid_coordinate(0, 9) == False
    assert onitama.valid_coordinate(-1, 1) == False


def test_get_token():
    onitama = OnitamaBoard(5, Player(Pieces.G1), Player(Pieces.G2), board1)
    assert onitama.get_token(0, 5) == ' '
    assert onitama.get_token(0, 2) == 'X'
    assert onitama.get_token(3, 3) == ' '


def test_set_token():
    onitama = OnitamaBoard(5, Player(Pieces.G1), Player(Pieces.G2), board1)
    assert onitama.set_token(0, 5, 'X') is None
    assert onitama.get_token(0, 2) == 'X'
    onitama.set_token(0, 2, 'Y')
    assert onitama.get_token(0, 2) == 'Y'


if __name__ == "__main__":
    pytest.main(['OnitamaBoard_Tests.py'])
