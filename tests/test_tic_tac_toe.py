import pytest

from tic_tac_toe import TicTacToe


def test_check_position():
    game = TicTacToe()
    game._field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    game._check_position()
    assert game.game_status == 'Next turn'

    game._field = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
    game._check_position()
    assert game.game_status == 'X win!'

    game._field = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    game._check_position()
    assert game.game_status == 'X win!'

    game._field = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    game._check_position()
    assert game.game_status == 'X win!'

    game._field = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    game._check_position()
    assert game.game_status == 'X win!'

    game._field = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
    game._check_position()
    assert game.game_status == 'X win!'

    game._field = [[1, 1, 1], [4, 4, 0], [4, 4, 1]]
    game._check_position()
    assert game.game_status == 'X win!'

    game._field = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
    game._check_position()
    assert game.game_status == '0 win!'

    game._field = [[0, 4, 0], [0, 4, 0], [0, 4, 0]]
    game._check_position()
    assert game.game_status == '0 win!'

    game._field = [[4, 0, 0], [0, 4, 0], [0, 0, 4]]
    game._check_position()
    assert game.game_status == '0 win!'

    game._field = [[4, 0, 0],
                   [0, 4, 0],
                   [0, 0, 4]]
    game._check_position()
    assert game.game_status == '0 win!'

    game._field = [[0, 0, 4],
                   [0, 4, 0],
                   [4, 0, 0]]
    game._check_position()
    assert game.game_status == '0 win!'

    game._field = [[4, 1, 4],
                   [1, 1, 4],
                   [4, 4, 1]]
    game._check_position()
    assert game.game_status == 'Game over. Draw.'

def test_make_turn():
    game = TicTacToe()
    game._field = [[0, 1, 4], [1, 4, 1], [4, 1, 1]]
    assert game._make_turn() == (0, 0)

    game._field = [[1, 1, 4], [1, 0, 1], [4, 1, 1]]
    assert game._make_turn() == (1, 1)

