from Day3 import day_3

TEST_STRING = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def test_day_3_part_1():
    #string_list = TEST_STRING.split('\n')
    assert day_3.day_3_part_1(TEST_STRING) == 4361

def test_compute_number():
    test_string = ['.......',
                    '...-...',
                    '..456..']


    test_engine = day_3.EngineSchematic(test_string)
    assert test_engine.find_symbol_code() == 456

def test_compute_number_2():
    test_string = ['.......',
                    '...-...',
                    '.45.65.']

    test_engine = day_3.EngineSchematic(test_string)
    assert test_engine.find_symbol_code() == 110


def test_gear():
    is_gear = ['.......',
                '...*...',
                '.45.65.']
    
    is_not_gear_1 = ['.......',
                     '...*...',
                     '.456...']
    is_not_gear_2 = ['...60..',
                     '...*...',
                     '.45.65.']
    test_engine = day_3.EngineSchematic(is_gear)
    non_gear_1 = day_3.EngineSchematic(is_not_gear_1)
    non_gear_2 = day_3.EngineSchematic(is_not_gear_2)
    assert test_engine.find_gears() == (45*65)
    assert non_gear_1.find_gears() == 0
    assert non_gear_2.find_gears() == 0

def test_symbol_list_generation():
    assert ['*', "#", "+", "$"] == day_3.return_symbol_list(TEST_STRING)

def test_day_3_part_2():
    string_list = TEST_STRING.split('\n')

    test_engine = day_3.EngineSchematic(string_list)

    assert test_engine.find_gears() == 467835