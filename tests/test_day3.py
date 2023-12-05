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

