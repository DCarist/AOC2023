from Day2 import day_2

DEFAULT_TEST_STRING = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

DEFAULT_RED_DICE = day_2.ColoredDice(6,'red')
DEFAULT_GREEN_DICE = day_2.ColoredDice(7,'green')
DEFAULT_BLUE_DICE = day_2.ColoredDice(8, 'blue')
DEFAULT_ROUND= day_2.Round(DEFAULT_RED_DICE,
                           DEFAULT_GREEN_DICE, 
                           DEFAULT_BLUE_DICE)

def test_day_2p1():

    test_string = DEFAULT_TEST_STRING.split('\n')
    assert day_2.day_2_part_1(test_string) == 8


def test_create_dataclass():
    test_dice = day_2.create_ColoredDice('4 red')
    assert day_2.ColoredDice(4, 'red') == test_dice

def test_create_round():
    red_dice = day_2.ColoredDice(6,'red')
    green_dice = day_2.ColoredDice(7,'green')
    blue_dice = day_2.ColoredDice(8, 'blue')
    test_round = day_2.Round(red_dice, green_dice, blue_dice)
    
    assert test_round.possible_round(12,13,14) is True
    assert test_round.possible_round(2,20,20) is False
    assert test_round.possible_round(20,2,20) is False
    assert test_round.possible_round(20,20,2) is False

def test_line_parse():
    test_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"

    assert day_2.parse_line_game_number(test_string) == 1

def test_line_parse_false():
    test_string = "Game 1: 3 blue, 40 red; 1 red, 2 green, 6 blue; 2 green"
    
    assert day_2.parse_line_game_number(test_string) == 0

    test_string = "Game 1: 3 blue, 4 red; 1 red, 20 green, 6 blue; 2 green"
    
    assert day_2.parse_line_game_number(test_string) == 0

    test_string = "Game 1: 3 blue, 4 red; 1 red, 2 green, 60 blue; 2 green"
    assert day_2.parse_line_game_number(test_string) == 0

def test_min_cubes():
    #test_string = DEFAULT_TEST_STRING[0]
    test_round = DEFAULT_ROUND

    assert test_round.minimum_possible_dice() == 0

def test_game_init():

    test_round_list = [DEFAULT_ROUND]
    day_2.Game(test_round_list)

def test_game_min():
    test_round_list = [DEFAULT_ROUND]
    test_game = day_2.Game(test_round_list)

    dice_tuple = test_game.minimum_dice_possible()
    assert DEFAULT_RED_DICE == dice_tuple[0]
    assert DEFAULT_GREEN_DICE == dice_tuple[1]
    assert DEFAULT_BLUE_DICE == dice_tuple[2]
