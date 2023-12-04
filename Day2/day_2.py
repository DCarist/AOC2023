from dataclasses import dataclass

R_MAX = 12
G_MAX = 13
B_MAX = 14

test_string = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]
@dataclass
class DiceRoll():
    """
    """
    number:int
    color:str

@dataclass
class Round():
    """
    """
    red_dice:DiceRoll = DiceRoll(0,'red')
    green_dice:DiceRoll =DiceRoll(0,'green')
    blue_dice:DiceRoll = DiceRoll(0,'blue')

    def possible_round(self,R_MAX:int, G_MAX:int, B_MAX:int) -> bool:
        if (self.red_dice.number > R_MAX or 
            self.green_dice.number > G_MAX or
            self.blue_dice.number > B_MAX
            ):
            return False
        else:
            return True



def create_diceroll(string:str):
    """
        Converts a string with # color into a DiceRoll
    """
    number, color = string.split()
    return DiceRoll(int(number), color) 

def create_round(string_list: list[str]) -> Round:
    """
        Creates a round from a list of strings with round Info.
    """   
    red_dice = DiceRoll(0,'red')
    green_dice = DiceRoll(0,'green')
    blue_dice = DiceRoll(0,'blue')
    for string in string_list:
        if 'red' in string:
            red_dice = create_diceroll(string)
        elif 'green' in string:
            green_dice = create_diceroll(string)
        elif 'blue' in string:
            blue_dice = create_diceroll(string)
    return Round(red_dice, green_dice, blue_dice)

def day_2_part_1(string_list: list[str]) -> int:
    #game_list = string.split('\n')
    total = 0
    for game in string_list:
        total += parse_line(game)

    return total
    
def return_min_cubes(dice_pulled_per_round:list[DiceRoll]):
    """
        Given a list of DiceRoll, return the minimum
        amount of dice that could be in the bag.
    """

    
def parse_line(game_string:str) -> int:
    """
        We need to split up the line into the requisite info
        Game #: Round{<DiceRoll>, <DiceRoll>, <DiceRoll> }; Round{<DiceRoll>, <DiceRoll>}; 
        Each Game has multiple rounds
        Each Round has up to 3 dice rolls, up to 1 of each color.

    """
    game_number , round_info = game_string.split(':')
    game_number = game_number[4:]
    round_list = round_info.split(';')
    possible_game = True
    for round in round_list:
        # Check each round if it is possible.
        dice_rolls = round.split(',')
        #dice_rolls should be a string list 
        cur_round = create_round(dice_rolls)
        #will be false if not possible.
        possible_game = cur_round.possible_round(R_MAX,G_MAX,B_MAX)
        if possible_game is False:
            break
    if possible_game:
        return int(game_number)
    else:
        return 0

if __name__ == '__main__':
    
    with open('Day2/day_2_input.txt') as file:
        input = file.readlines()
    
    print(day_2_part_1(input))

