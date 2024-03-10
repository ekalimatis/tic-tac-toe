from errors import (FormatTurnError,
                    RangeTurnError,
                    CellAlreadyFillError, )

EMPTY = None
EMPTY_STR = ' '


class Board:
    def __init__(self, field_size: int = 3) -> None:
        self._field = self._make_field(field_size)
        self.field_size: int = field_size

    @staticmethod
    def _make_field(field_size: int) -> list[list[str | None]]:
        field: list = []
        for row in range(field_size):
            field.append([])
            for col in range(field_size):
                field[-1].append(EMPTY)
                # self._free_cells.append((row, col))
        return field

    def get_cell(self, row: int, col: int) -> str | None:
        return self._field[row][col]

    def get_row(self, row_index: int) -> list[str | None]:
        return self._field[row_index]

    def get_col(self, col_index: int) -> list[str | None]:
        return [row[col_index] for row in self._field]

    def get_left_diagonal(self) -> list[str | None]:
        return [self._field[n][n] for n in range(self.field_size)]

    def get_right_diagonal(self) -> list[str | None]:
        return [self._field[n][self.field_size - n - 1] for n in range(self.field_size)]

    def get_all_lines(self) -> list[list[str | None]]:
        lines = []
        for n in range(self.field_size):
            lines.append(self.get_col(n))
            lines.append(self.get_row(n))
        lines.append(self.get_left_diagonal())
        lines.append(self.get_right_diagonal())
        return lines

    def set_turn(self, turn: tuple[int, int], mark: str | None) -> None:
        try:
            self.check_turn_ability(turn)
        except CellAlreadyFillError:
            raise CellAlreadyFillError
        row, col = turn
        self._field[row][col] = mark

    def get_free_cells(self) -> list[tuple[int, int]]:
        free_cells = []
        for row, _ in enumerate(self._field):
            for col, _ in enumerate(_):
                if self._field[row][col] == EMPTY:
                    free_cells.append((row, col))
        return free_cells

    def validate_turn(self, turn: str) -> tuple[int, int]:
        try:
            row, col = [int(row_col) for row_col in turn.split(',')]
        except ValueError:
            raise FormatTurnError(turn)

        if not 0 <= row <= self.field_size - 1:
            raise RangeTurnError(f"Row = {row}, is not between 0 and {self.field_size - 1}.")

        if not 0 <= col <= self.field_size - 1:
            raise RangeTurnError(f"Col = {col}, is not between 0 and {self.field_size - 1}.")

        return row, col

    def check_turn_ability(self, turn: tuple[int, int]) -> None:
        if self.get_cell(*turn) != EMPTY:
            raise CellAlreadyFillError(f"Cell {turn} is fill!")

    def console_display(self) -> str:
        field_for_print = ''
        for row in self._field:
            row_for_print = ''
            for cell in row:
                cell_for_print = '|' + (str(cell) if cell != EMPTY else EMPTY_STR)
                row_for_print += cell_for_print
            row_for_print += '|\n'
            field_for_print += row_for_print
        return field_for_print

    def __str__(self):
        return self.console_display()
