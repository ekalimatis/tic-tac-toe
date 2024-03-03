class ValidationTurnError(Exception):
    pass


class FormatTurnError(ValidationTurnError):
    def __init__(self, user_input: str) -> None:
        super().__init__(f'Can not parse /{user_input}/')
        self.user_input = user_input


class RangeTurnError(ValidationTurnError):
    pass


class CellAlreadyFillError(ValidationTurnError):
    pass