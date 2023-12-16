from Day6 import day_6

TEST_STRING = """Time:      7  15   30
Distance:  9  40  200"""


def test_boat_creation():
    test_boat = day_6.Boat(2,7)

    assert test_boat.distance == 10

def test_race_constrution():
    test_race = day_6.Race(7, 9)
    distance_list = [10, 12, 12, 10]
    for distance in distance_list:
        current_boat = test_race.boats.pop(0)
        assert current_boat.distance == distance


def test_string_parse():
    times, distances= day_6.parse_string(TEST_STRING)

    assert list(times) == [7,15,30]
    assert list(distances) == [9, 40, 200]

def test_boats():

    assert day_6.run_possible_boats(TEST_STRING) == 288

def test_string_parse_2():

    assert day_6.part_two_string(TEST_STRING) == (71530,940200)
