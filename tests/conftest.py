from unittest import mock
import pytest


class Dice:
    def __init__(self, text: str):
        self._text = text

    def text(self) -> str:
        return self._text


@pytest.fixture
def mock_dice(request):
    """Creates a list of Dice objects based on the parameters passed to the test."""
    return [Dice(item) for item in request.param]
