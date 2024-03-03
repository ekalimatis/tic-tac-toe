import pytest

from tic_tac_toe import TicTacToe


@pytest.mark.parametrize(('field', 'expected'), [
    ([
         ['0', None, None],
         ['0', None, None],
         ['0', None, None]
     ],
     '0'),
    ([
         [None, None, '0'],
         [None, '0', None],
         ['0', None, None]
     ],
     '0'),
    ([
         ['0', None, None],
         [None, '0', None],
         [None, None, '0']
     ], '0'
    ),
    ([
         ['0', '0', '0'],
         [None, None, None],
         [None, None, None]
     ],
     '0'),
])
def test__get_winner__return_winner_mark_if_is_winner(field, expected):
    game = TicTacToe()
    game._board._field = field

    assert game.get_winner() == expected


def test__get_winner__return_none_if_no_winner():
    game = TicTacToe()
    game._board._field = [[None, None, None], ['X', 'X', '0'], ['X', 'X', '0']]
    assert game.get_winner() is None
