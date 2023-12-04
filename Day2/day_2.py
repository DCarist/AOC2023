from dataclasses import dataclass

R_MAX = 12
G_MAX = 13
B_MAX = 14

test_string = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]
@dataclass
class ColoredDice():
    """
        number:int
        color:str
    """

    number:int
    color:str

    def __lt__(self, other):
        return self.number < other.number

@dataclass
class Round():
    """
        RGB_dice: ColoredDice
        
    """
    red_dice:ColoredDice = ColoredDice(0,'red')
    green_dice:ColoredDice =ColoredDice(0,'green')
    blue_dice:ColoredDice = ColoredDice(0,'blue')

    def possible_round(self,R_MAX:int, G_MAX:int, B_MAX:int) -> bool:
        if (self.red_dice.number > R_MAX or 
            self.green_dice.number > G_MAX or
            self.blue_dice.number > B_MAX
            ):
            return False
        else:
            return True

class Game():
    round_list:list[Round]

    def __init__(self, round_list:list[Round]):
        self.round_list =round_list

    def minimum_dice_possible(self) -> (ColoredDice, ColoredDice, ColoredDice):
        
        min_red = ColoredDice(0,'red')
        min_green = ColoredDice(0,'green')
        min_blue = ColoredDice(0,'blue')

        for round in self.round_list:
            if min_red < round.red_dice:
                min_red.number = round.red_dice.number
            if min_green < round.green_dice:
                min_green.number = round.green_dice.number
            if min_blue < round.blue_dice:
                min_blue.number = round.blue_dice.number
            
        return (min_red, min_green, min_blue)

    def power(self) -> int:
        """
            Returns the power (minR * minG * minB) of a Game.
        """
        color_tuple:tuple(ColoredDice, ColoredDice, ColoredDice) = self.minimum_dice_possible()

        return color_tuple[0].number * color_tuple[1].number * color_tuple[2].number



def create_ColoredDice(string:str):
    """
        Converts a string with # color into a ColoredDice
    """
    number, color = string.split()
    return ColoredDice(int(number), color) 

def create_round(string_list: list[str]) -> Round:
    """
        Creates a round from a list of strings with round Info.
    """   
    red_dice = ColoredDice(0,'red')
    green_dice = ColoredDice(0,'green')
    blue_dice = ColoredDice(0,'blue')
    for string in string_list:
        if 'red' in string:
            red_dice = create_ColoredDice(string)
        elif 'green' in string:
            green_dice = create_ColoredDice(string)
        elif 'blue' in string:
            blue_dice = create_ColoredDice(string)
    return Round(red_dice, green_dice, blue_dice)

def day_2_part_1(string_list: list[str]) -> int:
    #game_list = string.split('\n')
    total = 0
    for game in string_list:
        total += parse_line_game_number(game)

    return total
    
def day_2_part_2(string_list: list[str]) -> int:
    total = 0

    for game in string_list:
        total+= parse_line_game_power(game)
    return total

def return_min_cubes(dice_pulled_per_round:list[Round]):
    """
        Given a list of Rounds, return the minimum
        amount of dice that could be in the bag.

        List = [CD1, CD2, CD3]

        CD1 -> has Number, color. 
    """

def parse_line_game_power(game_string:str) -> int:
    """
        Creates a Game from a string, and returns its power.
        where power is the minR * minG * minB
    """
    game_number , round_info = game_string.split(':')
    game_number = game_number[4:]
    string_list_rounds = round_info.split(';')
    round_list:list[Round] = []
    for string in string_list_rounds:
        dice_pulled = string.split(',')
        cur_round = create_round(dice_pulled)
        round_list.append(cur_round)
    current_game = Game(round_list)

    return current_game.power()

def parse_line_game_number(game_string:list[str]) -> int:
    """
        We need to split up the line into the requisite info
        Game #: Round{<ColoredDice>, <ColoredDice>, <ColoredDice> }; Round{<ColoredDice>, <ColoredDice>}; 
        Each Game has multiple rounds
        Each Round has up to 3 colored dice, up to 1 of each color.

    """
    game_number , round_info = game_string.split(':')
    game_number = game_number[4:]
    round_list = round_info.split(';')
    possible_game = True
    for round in round_list:
        # Check each round if it is possible.
        dice_pulled = round.split(',')
        #dice_rolls should be a string list 
        cur_round = create_round(dice_pulled)
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
    print('--------')
    print(day_2_part_2(input))

