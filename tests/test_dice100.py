import pytest
from unittest.mock import MagicMock

from apps.dice1000.utils import DiceUtils


@pytest.mark.parametrize(
    "dice_texts, expected_result",
    [
        (["1", "1", "1", "1", "1"], {"1": 5}),
        (["2", "2", "2", "2", "2"], {"2": 5}),
        (["1", "2", "3", "4", "5"], {"1": 1, "2": 1, "3": 1, "4": 1, "5": 1}),
        (["1", "1", "2", "2", "3"], {"1": 2, "2": 2, "3": 1}),
    ],
)
def test_dict_dice(dice_texts, expected_result):
    poker = DiceUtils()
    dices = []
    for text in dice_texts:
        dice = MagicMock()
        dice.text = MagicMock(return_value=text)
        dices.append(dice)
    result = poker.dict_dice(dices)
    assert result == expected_result


@pytest.mark.parametrize(
    "dice_texts, expected_result",
    [
        (["1", "1", "1", "1", "1"], 1000),
        (["2", "2", "2", "2", "2"], 2000),
        (["1", "2", "3", "4", "5"], 150),
        (["1", "1", "2", "2", "3"], 30),
    ],
)
def test_count_dice(dice_texts, expected_result):
    poker = DiceUtils()
    dices = []
    for text in ["1", "1", "1", "1", "1"]:
        dice = MagicMock()
        dice.text = MagicMock(return_value=text)
        dices.append(dice)
    result = poker.count_dice(dices)
    assert result == 1000
    dices = []
    for text in ["1", "1", "1", "1", "2"]:
        dice = MagicMock()
        dice.text = MagicMock(return_value=text)
        dices.append(dice)
    result = poker.count_dice(dices)
    assert result == 30
    dices = []
    for text in ["1", "1", "1", "1", "1"]:
        dice = MagicMock()
        dice.text = MagicMock(return_value=text)
        dices.append(dice)
    result = poker.count_dice(dices)
    assert result == 1000
    dices = []
    for text in ["1", "1", "1", "1", "1"]:
        dice = MagicMock()
        dice.text = MagicMock(return_value=text)
        dices.append(dice)
    result = poker.count_dice(dices)
    assert result == 1000
    dices = []
    for text in ["1", "1", "1", "1", "1"]:
        dice = MagicMock()
        dice.text = MagicMock(return_value=text)
        dices.append(dice)
    result = poker.count_dice(dices)
    assert result == 1000
    dices = []
    for text in ["1", "1", "1", "1", "1"]:
        dice = MagicMock()
        dice.text = MagicMock(return_value=text)
        dices.append(dice)
    result = poker.count_dice(dices)
    assert result == 1000
    dices = []
    for text in ["1", "1", "1", "1", "1"]:
        dice = MagicMock()
        dice.text = MagicMock(return_value=text)
        dices.append(dice)
    result = poker.count_dice(dices)
    assert result == 1000
    dices = []
    for text in ["1", "1", "1", "1", "1"]:
        dice = MagicMock()
        dice.text = MagicMock(return_value=text)
        dices.append(dice)
    result = poker.count_dice(dices)
    assert result == 100
