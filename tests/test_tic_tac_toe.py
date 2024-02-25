import pytest

from tic_tac_toe import TicTacToe


# def test_check_position():
#     game = TicTacToe()
#     game._field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#     game._check_position()
#     assert game.game_status == 'Next turn'
#
#     game._field = [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
#     game._check_position()
#     assert game.game_status == 'X win!'
#
#     game._field = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
#     game._check_position()
#     assert game.game_status == 'X win!'
#
#     game._field = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
#     game._check_position()
#     assert game.game_status == 'X win!'
#
#     game._field = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
#     game._check_position()
#     assert game.game_status == 'X win!'
#
#     game._field = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
#     game._check_position()
#     assert game.game_status == 'X win!'
#
#     game._field = [[1, 1, 1], [4, 4, 0], [4, 4, 1]]
#     game._check_position()
#     assert game.game_status == 'X win!'
#
#     game._field = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
#     game._check_position()
#     assert game.game_status == '0 win!'
#
#     game._field = [[0, 4, 0], [0, 4, 0], [0, 4, 0]]
#     game._check_position()
#     assert game.game_status == '0 win!'
#
#     game._field = [[4, 0, 0], [0, 4, 0], [0, 0, 4]]
#     game._check_position()
#     assert game.game_status == '0 win!'
#
#     game._field = [[4, 0, 0],
#                    [0, 4, 0],
#                    [0, 0, 4]]
#     game._check_position()
#     assert game.game_status == '0 win!'
#
#     game._field = [[0, 0, 4],
#                    [0, 4, 0],
#                    [4, 0, 0]]
#     game._check_position()
#     assert game.game_status == '0 win!'
#
#     game._field = [[4, 1, 4],
#                    [1, 1, 4],
#                    [4, 4, 1]]
#     game._check_position()
#     assert game.game_status == 'Game over. Draw.'

def test_winner_by_turn():
    game = TicTacToe()
    game._field = [[3, 1, 4],
                   [1, 3, 4],
                   [4, 4, 3]]
    assert game._check_winner_by_turn((1,1)) == True

    game._field = [[0, 1, 4],
                   [0, 3, 4],
                   [0, 4, 1]]
    assert game._check_winner_by_turn((2,0)) == True

    game._field = [[9, 1, 5],
                   [7, 5, 4],
                   [5, 4, 1]]
    assert game._check_winner_by_turn((0,2)) == True



def test_make_turn():
    game = TicTacToe()
    game._field = [[' ', 1, 4], [1, 4, 1], [4, 1, 1]]
    assert game._computer_turn() == (0, 0)

    game._field = [[1, 1, 4], [1, ' ', 1], [4, 1, 1]]
    assert game._computer_turn() == (1, 1)

def test_console_display():
    pass

