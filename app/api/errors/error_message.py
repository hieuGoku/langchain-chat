"""Error message for the API"""


class BaseErrorMessage:
    """Base error message class."""
    status_code: int
    message: str

    def __init__(self, *args):
        self.message = self.message.format(*args)
