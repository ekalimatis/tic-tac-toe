from random import shuffle
from itertools import cycle

from board import Board
from playres import PlayerWithMark, HumanPlayer, ComputerPlayer

FIELD_SIZE = 3
MARK_X = 'X'
MARK_O = '0'


class TicTacToe:
    def __init__(self) -> None:
        self._board = Board(FIELD_SIZE)
        self.players: list[PlayerWithMark] = self._get_players()

    @staticmethod
    def _get_players() -> list[PlayerWithMark]:
        players = [HumanPlayer, ComputerPlayer]
        shuffle(players)
        players_with_mark = []
        for player, mark in zip(
                players,
                (MARK_X, MARK_O)
                ):
            players_with_mark.append(player(mark))
        return players_with_mark

    @staticmethod
    def _get_liner_winner(line: list[str | None]) -> str | None:
        if len(set(line)) == 1:
            return line[0]
        return None

    def get_winner(self) -> str | None:
        for line in self._board.get_all_lines():
            winner_mark = self._get_liner_winner(line)
            if winner_mark:
                return winner_mark
        return None

    def run(self) -> None:
        print('Game start!\n')
        print(self._board)

        is_game_over = False
        while not is_game_over:
            for player in cycle(self.players):
                print(f"Player {player.mark} turn!")
                turn = player.turn(self._board)
                self._board.set_turn(turn, player.mark)
                print(self._board)
                if self.get_winner():
                    print(f'{player.mark} win!')
                    is_game_over = True
                    break
                if not self._board.get_free_cells():
                    print('Draw!')
                    is_game_over = True
                    break


def main():
    while True:
        game = TicTacToe()
        game.run()
        answer = input('One more game yes(y)?')
        if answer != 'y':
            break


if __name__ == "__main__":
    main()
