from typing import Protocol
from random import choice

from board import Board
from errors import ValidationTurnError


class Player(Protocol):
    def turn(self, board: Board) -> tuple[int, int]:
        """Return player turn row, col"""


class PlayerWithMark(Player):
    def __init__(self, mark: str):
        self.mark = mark


class HumanPlayer(PlayerWithMark):
    def turn(self, board: Board) -> tuple[int, int]:
        while True:
            player_turn = input('Enter your turn in following format <row>,<column>: ')
            try:
                turn = board.validate_turn(player_turn)
                board.check_turn_ability(turn)
            except ValidationTurnError as er:
                print(er)
            else:
                return turn


class ComputerPlayer(PlayerWithMark):
    def turn(self, board: Board) -> tuple[int, int]:
        turn = choice(board.get_free_cells())
        return turn
