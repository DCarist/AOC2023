from Day2 import day_2

def test_day_2p1():
    test_string = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    test_string = test_string.split('\n')
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
