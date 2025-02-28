class DiceUtils:
    
    @staticmethod
    def dict_dice(dices):
        dice_dict = {}
        for dice in dices:
            dice_dict[dice.text()] = dice_dict.get(dice.text(), 0) + 1
        return dice_dict
    
    @staticmethod
    def count_dice(dices: dict)-> int: 
        count = 0
        # check if all dice are the same
        if len(set(dices)) == 1:
            if dices[0].text() == '1':
                return 1000
            return int(dices[0].text() * 30)
        # Check if 4s
        if len(set(dices)) == 2:
            if dices[0].text() == dices[1].text():
                if dices[0].text() == '1':
                    return 400
                return int(dices[0].text()) * 200
        # count 5s
        count += sum(5 for d in dices if d.text() == '5')
        # count 10
        count += sum(10 for d in dices if d.text() == '1')   
        return count
        sum(int(dice.text()) for dice in dices)
    