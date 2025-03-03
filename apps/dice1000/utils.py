class DiceUtils:

    def __init__(self, dices):
        self.count: int = 0
        self.dices: list = dices
        self.dices_dict: dict[str, int] = {}
        self._dict_dice()

    def _dict_dice(self) -> dict[str, int]:
        ''' Create a dictionary with the count of each dice '''
        for dice in self.dices:
            if dice.text() == "1":
                self.dices_dict["10"] = self.dices_dict.get("10", 0) + 1
            else:
                self.dices_dict[dice.text()] = self.dices_dict.get(dice.text(), 0) + 1
        return self.dices_dict

    def count_dice(self) -> int:
        ''' Rules for counting dice:
        1= 10 points, 5= 5 points, all other - 0 points
        5 of a kind = 100 * dice value
        3 of a kind = 10 * dice value
        4 of a kind = 20 * dice value
        5 of a kind = 100 * dice value
        counting dices removed from the list
        '''

        # check if all dice are the same
        if len(self.dices_dict) == 1:  # Only one unique value
            key = list(self.dices_dict.keys())[0]  # Get the first (and only) key
            return int(key) * 100, {}
        # Check if 4s
        elif len(self.dices_dict) == 2:
            max_key = max(self.dices_dict, key=self.dices_dict.get)
            # max_value = self.dices_dict[max_key]
            if self.dices_dict[max_key] == 4:
                self.count += int(max_key) * 20
            elif self.dices_dict[max_key] == 3:
                self.count += int(max_key) * 10
            # delete used dices
            del self.dices_dict[max_key]
            self._count_rest()
        elif len(self.dices_dict) == 3:
            max_key = max(self.dices_dict, key=self.dices_dict.get)
            if self.dices_dict[max_key] == 3:
                self.count += int(max_key) * 10
                # delete used dices
                del self.dices_dict[max_key]
                self._count_rest()
            else:
                self._count_rest()      
        else:
            self._count_rest()

        return self.count, self.dices_dict
        # count 5s
        # count += sum(5 for d in dices if d.text() == "5")
        # count 10
        # sum(int(dice.text()) for dice in dices)
    
    def _count_rest(self):
        rest_dict = self.dices_dict.copy()
        for key, value in rest_dict.items():
            if key in ["10", "5"]:
                self.count += int(key) * int(value)
                del self.dices_dict[key]
        return self.count


class Dice:
    def __init__(self, text: str):
        self._text = text

    def text(self) -> str:
        return self._text


if __name__ == "__main__":
    dices = [Dice(str(6)), Dice(str(6)), Dice(str(6)), Dice(str(5)), Dice(str(1))]

    util = DiceUtils(dices)

    print(util.dices_dict)
    print(util.count_dice())
