import random
from enum import Enum

class ValidationTurnError(Exception):
    pass

class FormatTurnError(ValidationTurnError):
    pass

class RangeTurnError(ValidationTurnError):
    pass

class CellAlreadyFillError(ValidationTurnError):
    pass

class Player:
    EMPTY = ' '
    X = 'X'
    O = '0'

def consol_display(field: list[list]) -> None:
    field_for_print = ''
    for row in field:
        row_for_print = ''
        for cell in row:
            cell_for_print = '|' + cell
            row_for_print += cell_for_print
        row_for_print += '|\n'
        field_for_print += row_for_print
    print(field_for_print)

class TicTacToe:
#     cell_mask = {
#         Player.EMPTY.value: ' ',
#         Player.X.value: 'X',
#         Player.O.value: 'O'
#     }

    def __init__(self) -> None:
        self._field = [[Player.EMPTY for _ in range(3)] for _ in range(3)]
        self._turns_count = 0
        self.game_status = 'Next turn'
        self._is_over = False
        self._my_turn = random.choice([True, False])

    def _validate_turn(self, turn: str) -> tuple[int, int]:
        try:
            row, col = list(int(_) for _ in turn.split(','))
        except ValueError:
            raise FormatTurnError
        if not 0 <= row <= 2 or not 0 <= row <= 2:
            raise RangeTurnError
        if self._field[row][col] != Player.EMPTY:
            raise CellAlreadyFillError
        return row, col

    def set_turn(self, turn: tuple[int, int], player: Player) -> None:
        row, col = turn
        self._field[row][col] = player

    def _check_winner_by_turn(self, turn: tuple[int, int]) -> bool:
        row, col = turn
        if len(set(self._field[row])) == 1:
            return True

        if len(set([_[col] for _ in self._field])) == 1:
            return True

        if row == col and len(set([self._field[n][n] for n, _ in enumerate(self._field)])) == 1:
            return True

        if row + col == len(self._field) - 1 and len(set([self._field[n][len(self._field) - n - 1] for n, _ in enumerate(self._field)])) == 1:
            return True

        return False

    def _get_free_cells(self):
        free_cells = []
        for row, _ in enumerate(self._field):
            for col, _ in enumerate(_):
                if self._field[row][col] == Player.EMPTY:
                    free_cells.append((row, col))
        return free_cells

    def _computer_turn(self) -> tuple[int, int]:
        turn = random.choice(self._get_free_cells())
        return turn

    def _player_turn(self):
        is_correct_turn = False
        while not is_correct_turn:
            player_turn = input('Enter your turn in following format <row>,<column>: ')
            try:
                turn = self._validate_turn(player_turn)
            except (FormatTurnError, RangeTurnError):
                print('Wrong turn, col and row must be >= 0 and <= 2')
            except CellAlreadyFillError:
                print('Cell already fill, choose another turn.')
            else:
                is_correct_turn = True
        return turn

    def run(self) -> None:
        player = Player.X
        print('Game start')
        consol_display(self._field)
        while not self._is_over:
            if self._my_turn:
                print('My turn!')
            else:
                print('Your turn!')
            if self._my_turn:
                turn = self._computer_turn()
            else:
                turn = self._player_turn()
            self.set_turn(turn, player)
            consol_display(self._field)
            if self._check_winner_by_turn(turn):
                print(f'{player} win!')
                break
            if not self._get_free_cells():
                print('Draw!')
            # self._turns_count += 1
            self._my_turn = not self._my_turn
            if player == Player.X:
                player = Player.O
            else:
                player = Player.X

def main():
    one_more_game = True
    while one_more_game:
        game = TicTacToe()
        game.run()
        answer = input('One more game y/n?')
        if answer != 'y':
            one_more_game = False

if __name__ == '__main__':
    main()
