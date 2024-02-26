import pytest

from tic_tac_toe import (TicTacToe,
                         consol_display,
                         FormatTurnError,
                         RangeTurnError,
                         CellAlreadyFillError)


@pytest.mark.parametrize(('input_str', 'expected'), [
    ('1,1', (1, 1)),
    ('0,1', (0, 1)),
    ('0,0', (0, 0)),
])
def test__validate_turn__return_int_tuple_if_turn_correct(input_str: str, expected: tuple[int, int]):
    game = TicTacToe()

    assert game._validate_turn(input_str) == expected


@pytest.mark.parametrize('input_str', [
    ('1,1,1'),
    ('1'),
    (''),
    ('adsfsaf'),
])
def test__validate_turn__raise_FormatTurnError_if_turn_is_not_validformat(input_str: str):
    game = TicTacToe()

    with pytest.raises(FormatTurnError):
        game._validate_turn(input_str)


@pytest.mark.parametrize('input_str', [
    ('-1,0'),
    ('-1,-1'),
    ('3,3'),
    ('1,3'),
])
def test__validate_turn__raise_RangeTurnError_if_turn_is_out_the_FIELD_SIZE(input_str: str):
    game = TicTacToe()

    with pytest.raises(RangeTurnError):
        game._validate_turn(input_str)


@pytest.mark.parametrize(('input_str', 'field'), [
    ('0,0', [['0', '0', '0'],
             ['0', '0', '0'],
             ['0', '0', '0']]),
    ('1,1', [[' ', ' ', ' '],
             [' ', '0', ' '],
             [' ', ' ', ' ']]),
])
def test__validate_turn__raise_CellAlreadyFillError_if_turn_cell_is_fill(input_str: str, field: list[list[int]]):
    game = TicTacToe()
    game._field = field

    with pytest.raises(CellAlreadyFillError):
        game._validate_turn(input_str)


@pytest.mark.parametrize(('turn', 'field'), [
    ((0, 0), [
        [0, 1, 2],
        [0, 3, 4],
        [0, 5, 6]
    ]
     ),
    ((1, 1), [
        [1, 2, 5],
        [3, 5, 4],
        [5, 6, 7]
    ]
     ),
    ((1, 1), [
        [1, 2, 3],
        [4, 1, 5],
        [6, 7, 1]
    ]
     ),
    ((0, 0), [
        [1, 1, 1],
        [2, 3, 4],
        [5, 6, 7]
    ]
     ),
])
def test__check_winner_by_turn__return_true_if_is_winner(turn, field):
    game = TicTacToe()
    game._field = field

    assert game._check_winner_by_turn(turn) == True


def test__check_winner_by_turn__return_false_if_no_winner():
    game = TicTacToe()
    game._field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    turn = (1, 1)
    assert game._check_winner_by_turn(turn) == False


def test__get_free_cells__return_list_of_cells_if_free_cells_exist():
    game = TicTacToe()
    game._field = [[' ', 2, 3], [4, ' ', 6], [7, 8, ' ']]
    expexted = [(0, 0), (1, 1), (2, 2)]

    assert game._get_free_cells() == expexted


def test__get_free_cells__return_empty_list_of_cells_if_free_cells_not_exist():
    game = TicTacToe()
    game._field = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expexted = []

    assert game._get_free_cells() == expexted


def test__choose_computer_turn__return_random_free_cell():
    game = TicTacToe()
    game._field = [[' ', 1, 4], [1, 4, 1], [4, 1, 1]]
    assert game._choose_computer_turn() == (0, 0)

    game._field = [[1, 1, 4], [1, ' ', 1], [4, 1, 1]]
    assert game._choose_computer_turn() == (1, 1)


def test__console_display__return_str_representation_of_game_field():
    field = [[1, 1, 4], [1, ' ', 1], [4, 1, 1]]
    field_str = "|1|1|4|\n|1| |1|\n|4|1|1|\n"

    assert consol_display(field) == field_str
