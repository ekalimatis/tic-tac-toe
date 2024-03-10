import pytest

from board import Board
from tic_tac_toe import FIELD_SIZE
from errors import (FormatTurnError,
                    RangeTurnError,
                    CellAlreadyFillError)


@pytest.mark.parametrize(('input_str', 'expected'), [
    ('1,1', (1, 1)),
    ('0,1', (0, 1)),
    ('0,0', (0, 0)),
    ('0,   0', (0, 0)),
])
def test__validate_turn__return_int_tuple_if_turn_correct(input_str: str, expected: tuple[int, int]):
    board = Board(FIELD_SIZE)

    assert board.validate_turn(input_str) == expected


@pytest.mark.parametrize('input_str', [
    ('1,1,1'),
    ('1'),
    (''),
    ('adsfsaf'),
])
def test__validate_turn__raise_format_turn_error_if_turn_is_not_valid_format(input_str: str):
    board = Board(FIELD_SIZE)

    with pytest.raises(FormatTurnError):
        board.validate_turn(input_str)


@pytest.mark.parametrize('input_str', [
    ('-1,0'),
    ('-1,-1'),
    ('3,3'),
    ('1,3'),
])
def test__validate_turn__raise_range_turn_error_if_turn_is_out_the_FIELD_SIZE(input_str: str):
    board = Board(FIELD_SIZE)

    with pytest.raises(RangeTurnError):
        board.validate_turn(input_str)


@pytest.mark.parametrize(('turn', 'field'), [
    ((0, 0), [['X', None, None],
              [None, None, None],
              [None, None, None]]),
    ((1, 1), [[None, None, None],
              [None, 'X', None],
              [None, None, None]]),
])
def test__validate_turn__raise_cell_already_fill_error_if_turn_cell_is_fill(turn, field):
    board = Board(FIELD_SIZE)
    board._field = field

    with pytest.raises(CellAlreadyFillError):
        board.check_turn_ability(turn)


def test__console_display__return_str_representation_of_game_field():
    board = Board(FIELD_SIZE)
    board._field = [[None, None, None], [None, 'Х', None], [None, None, None]]
    field_str = "| | | |\n| |Х| |\n| | | |\n"

    assert board.console_display() == field_str


def test__get_free_cells__return_list_of_cells_if_free_cells_exist():
    board = Board(FIELD_SIZE)
    board._field = [[None, '0', '0'], ['0', None, '0'], ['0', '0', None]]
    expected = [(0, 0), (1, 1), (2, 2)]

    assert board.get_free_cells() == expected


def test__get_free_cells__return_empty_list_of_cells_if_free_cells_not_exist():
    board = Board(FIELD_SIZE)
    board._field = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
    expected = []

    assert board.get_free_cells() == expected
