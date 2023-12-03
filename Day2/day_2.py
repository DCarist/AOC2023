from dataclasses import dataclass

R_MAX = 12
G_MAX = 13
B_MAX = 14

@dataclass
class DiceRoll():
    """
    """
    number:int
    color:int

@dataclass
class Round():
    """
    """
    red_dice:DiceRoll
    green_dice:DiceRoll
    blue_dice:DiceRoll
    info: list[DiceRoll]

@dataclass
class Game():
    """
    """
    round_info:list[Round]
    game_id:int

    def create_Game(self,input_line:str):
        input_line.split(';')


def day_2_part_1(string:str):
    game_list = string.split('\n')
    game_info = []
    game_id, game_info = game_list[0].split(':',1)
    
    print(game_info)
    

def day_2_p1_line(string_list:list[str]) -> int:
    game_info = []
    for string in string_list:
        game_number = 0

def test_day_2p1():
    test_string = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    day_2_part_1(test_string)

if __name__ == '__main__':
    test_day_2p1()