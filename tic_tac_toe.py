import random
from enum import Enum


class Player(Enum):
    EMPTY = 0
    X = 1
    O = 4


class TicTacToe:
    cell_mask = {
        Player.EMPTY.value: ' ',
        Player.X.value: 'X',
        Player.O.value: 'O'
    }

    def __init__(self):
        self._field = [[Player.EMPTY.value for _ in range(3)] for _ in range(3)]
        self._turns_count = 0
        self.game_status = 'Next turn'
        self._is_over = False
        self._my_turn = random.choice([True, False])

    def __repr__(self):
        field_for_print = ''
        for row in self._field:
            row_for_print = ''
            for cell in row:
                cell_for_print = '|' + TicTacToe.cell_mask[cell]
                row_for_print += cell_for_print
            row_for_print += '|\n'
            field_for_print += row_for_print
        return field_for_print

    def set_turn(self, turn: tuple[int, int], player: Player) -> bool:
        try:
            row, col = int(turn[0]), int(turn[1])
        except ValueError:
            print('Wrong turn, col and row must be >= 0 and <= 2')
            return False
        if not 0 <= row <= 2 or not 0 <= row <= 2:
            print('Wrong turn, col and row must be >= 0 and <= 2')
            return False
        if self._field[row][col] == Player.EMPTY.value:
            self._field[row][col] = player
            return True
        print('Wrong turn, cell is fill!')
        return False

    def _check_position(self) -> None:
        colums_sum = [0, 0, 0]
        left_to_right = 0
        right_to_left = 0
        for col, row in enumerate(self._field):
            if sum(row) == 3:
                self._is_over = True
                self.game_status = 'X win!'
                return
            if sum(row) == 12:
                self._is_over = True
                self.game_status = '0 win!'
                return
            colums_sum[0] += row[0]
            colums_sum[1] += row[1]
            colums_sum[2] += row[2]
            left_to_right += row[col]
            right_to_left += row[len(row) - 1 - col]
        for sum_col in colums_sum:
            if sum_col == 3 or left_to_right == 3 or right_to_left == 3:
                self._is_over = True
                self.game_status = 'X win!'
                return
            if sum_col == 12 or left_to_right == 12 or right_to_left == 12:
                self._is_over = True
                self.game_status = '0 win!'
                return
        if self._turns_count == 9:
            self._is_over = True
            self.game_status = 'Game over. Draw.'
            return
        self.game_status = 'Next turn'
        return

    def _make_turn(self) -> tuple[int, int]:
        free_cells = []
        for row, _ in enumerate(self._field):
            for col, _ in enumerate(_):
                if self._field[row][col] == Player.EMPTY.value:
                    free_cells.append((row, col))
        turn = random.choice(free_cells)
        return turn

    def run(self) -> None:
        player = Player.X
        print('Game start')
        print(self)
        while not self._is_over:
            if self._my_turn:
                print('My turn!')
            else:
                print('Your turn!')
            if self._my_turn:
                self.set_turn(self._make_turn(), player.value)
            else:
                is_correct_turn = False
                while not is_correct_turn:
                    print('Enter your turn in following format <row>,<column>: ', end='')
                    is_correct_turn = self.set_turn(input().split(','), player.value)
            self._turns_count += 1
            self._check_position()
            self._my_turn = not self._my_turn
            if player == Player.X:
                player = Player.O
            else:
                player = Player.X
            print(self)
        print(self.game_status)


    def start_new_game(self):
        pass


if __name__ == '__main__':
    game = TicTacToe()
    game.run()
