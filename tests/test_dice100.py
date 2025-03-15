from unittest.mock import MagicMock

import pytest

from apps.dice1000.utils import DiceUtils


@pytest.mark.parametrize(
    "mock_dice,expected_result",
    [
        (["1", "1", "1", "1", "1"], (1000, {})),
        (["2", "2", "2", "2", "2"], (200, {})),
        (["1", "2", "3", "4", "5"], (15, {'2': 1, '3': 1, '4': 1})),
        (["1", "1", "2", "2", "3"], (20, {'2': 2, '3': 1})),
        (["1"], (10, {})),
        (["1", "1"], (20, {})),
        (["3", "3", "3", "3", "3"], (300, {})),
        (["4", "4", "4", "4", "4"], (400, {})),
        (["5", "5", "5", "5", "5"], (500, {})),
        (["6", "6", "6", "6", "6"], (600, {})),
        (["2", "3", "4", "5", "6"], (5, {'2': 1, '3': 1, '4': 1, '6': 1})),
        (["2", "3", "4", "6", "6"], (0, {'2': 1, '3': 1, '4': 1, '6': 2})),
        (["1", "1", "1", "2", "2"], (100, {'2': 2})),
    ],
    indirect=["mock_dice"],  # Important! Tells pytest this is a fixture, not a parameter
)
def test_count_dice(mock_dice, expected_result):
    poker = DiceUtils(mock_dice)
    result = poker.count_dice()
    assert result == expected_result
