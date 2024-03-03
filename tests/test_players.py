from playres import ComputerPlayer
from board import Board


def test__choose_computer_turn__return_random_free_cell():
    board = Board()
    board._field = [
        [None, '0', '0'],
        ['0', None, '0'],
        ['0', '0', None]]
    player = ComputerPlayer('X')

    assert player.turn(board) in [(0, 0), (1, 1), (2, 2)]

