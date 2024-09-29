import pytest
from OnitamaGame import OnitamaGame
from typing import List
from Pieces import Pieces


def move(board: List[List[str]], row_o: int, col_o: int, row_d: int, col_d: int):
    """
    Move a token on the board.
    Assume all moves are valid.
    """
    token = board[row_o][col_o]
    board[row_o][col_o] = Pieces.EMPTY
    board[row_d][col_d] = token


board1 = [['x', ' ', 'X', 'x', 'x'],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', 'x', ' '],
          [' ', 'y', ' ', ' ', ' '],
          ['y', ' ', 'Y', 'y', 'y']]

board2 = [['x', ' ', 'X', 'x', 'x'],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', 'x', ' '],
          [' ', 'y', ' ', ' ', ' '],
          ['y', ' ', ' ', 'y', 'y']]

board3 = [['x', 'x', 'X', 'x', 'x'],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '],
          ['y', 'y', 'Y', 'y', 'y']]

board4 = [['x', ' ', ' ', 'x', 'x'],
          [' ', 'Y', ' ', ' ', ' '],
          [' ', ' ', ' ', 'x', ' '],
          [' ', 'y', ' ', ' ', ' '],
          ['y', ' ', 'X', 'y', 'y']]

board5 = [['x', ' ', ' ', 'x', 'x'],
          [' ', 'Y', ' ', ' ', ' '],
          [' ', ' ', ' ', 'x', ' '],
          [' ', ' ', ' ', ' ', ' '],
          ['y', ' ', ' ', 'y', 'y']]

board6 = [[' ', 'x', ' ', 'x', 'x'],
          [' ', 'Y', ' ', ' ', ' '],
          [' ', ' ', ' ', 'x', ' '],
          [' ', ' ', 'X', ' ', ' '],
          ['y', ' ', ' ', 'y', 'y']]


def test_move_valid():
    onitama = OnitamaGame()
    onitama.set_board(5, board3)

    test = onitama.get_board()

    assert onitama.move(0, 2, 1, 2, 'crab') == True
    move(test, 0, 2, 1, 2)
    assert test == onitama.get_board()


def test_move_invalid_style():
    onitama = OnitamaGame()
    onitama.set_board(5, board2)

    test = onitama.get_board()
    assert onitama.move(2, 3, 2, 4, 'mantis') == False
    move(test, 2, 3, 2, 4)
    assert test != onitama.get_board()


def test_move_invalid_dest():
    onitama = OnitamaGame()
    onitama.set_board(5, board1)
    test = onitama.get_board()
    assert onitama.move(0, 3, 0, 4, 'horse') == False
    move(test, 0, 3, 0, 4)
    assert test != onitama.get_board()


def test_other_player():
    onitama = OnitamaGame()
    onitama.set_board(5, board3)
    assert onitama.other_player(onitama.player1) is onitama.player2
    assert onitama.other_player(onitama.player2) is onitama.player1


def test_get_token_size_seven():
    onitama = OnitamaGame(7)
    assert onitama.get_token(0, 3) == Pieces.G1
    assert onitama.get_token(0, 2) == Pieces.M1
    assert onitama.get_token(1, 2) == Pieces.EMPTY


def test_get_token_invalid_cor():
    onitama = OnitamaGame()
    onitama.set_board(5, board5)
    assert onitama.get_token(0, 5) == Pieces.EMPTY
    assert onitama.get_token(7, 7) == Pieces.EMPTY


def test_is_legal_move_invalid_token():
    onitama = OnitamaGame()
    onitama.set_board(5, board2)
    assert onitama.is_legal_move(3, 1, 3, 2) == False


def test_is_legal_move_valid():
    onitama = OnitamaGame()
    assert onitama.is_legal_move(0, 1, 1, 1) == True


def test_is_legal_move_invalid_dest():
    onitama = OnitamaGame()
    assert onitama.is_legal_move(0, 4, 0, 5) == False


def test_get_winner():
    onitama = OnitamaGame()
    onitama.set_board(5, board4)
    assert onitama.get_winner() is onitama.player1


def test_get_winner_another():
    onitama = OnitamaGame()
    onitama.set_board(5, board6)
    assert onitama.get_winner() is None
    assert onitama.move(0, 1, 1, 1, 'crab') == True
    assert onitama.get_winner() is onitama.player1


def test_undo_no_move():
    onitama = OnitamaGame()
    onitama.set_board(5, board3)
    test = onitama.get_board()
    onitama.undo()
    assert test == onitama.get_board()


def test_undo_move():
    onitama = OnitamaGame()
    onitama.set_board(5, board6)
    test = onitama.get_board()
    assert onitama.move(0, 1, 1, 1, 'crab') == True
    assert test != onitama.get_board()
    onitama.undo()
    assert test == onitama.get_board()


if __name__ == "__main__":
    pytest.main(['OnitamaGame_Tests.py'])
