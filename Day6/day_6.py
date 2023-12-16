

class Boat():
    ACCELERATION = 1
    INITIAL_SPEED = 0

    def __init__(self, accel_time, tot_time):
        """
            On init, calculate the boats velocity and distance traveled.
        """
        self.velocity = accel_time * self.ACCELERATION + self.INITIAL_SPEED
        
        self.distance = (tot_time - accel_time) * self.velocity

    def beats_record(self, record:int):

        if self.distance > record:
            return True
        else:
            return False

class Race():

    def __init__(self, race_time:int, record_distance:int):
        self.boats = [Boat(x,race_time) for x in range(race_time+1) if Boat(x,race_time).distance > record_distance]

        #self.winning_boats = 

class Smart_Race():

    def __init__(self, race_time:int, record_distance:int):
        x = 1
        y = race_time - 1
        cur_boat = Boat(x,race_time)

        while not cur_boat.beats_record(record_distance):
            x += 1
            cur_boat = Boat(x,race_time)
        cur_boat = Boat(y, race_time)
        while not cur_boat.beats_record(record_distance):
            y -= 1
            cur_boat = Boat(y, race_time)
        
        self.possible_solution = y - x +1

def run_possible_boats(string:str):
    race_list = []
    time_list, distance_list = parse_string(string)
    for time, distance in zip(time_list, distance_list):
        race_list.append(Race(time, distance))

    val = 1
    for race in race_list:
        val *= len(race.boats)

    return val

def parse_string(string:str):
    string = string.split('\n')

    times = string[0].split(':')[1]
    times = times.split()
    
    distances = string[1].split(':')[1]
    distances = distances.split()
    


    return map(int, times) , map(int, distances)

def part_two_string(string:str):
    string = string.split('\n')

    times = string[0].split(':')[1]
    times = times.split()

    distances = string[1].split(':')[1]
    distances = distances.split()
    race_time = ''
    race_distance = ''
    for time, distance in zip(times,distances):
        race_time += time
        race_distance += distance

    return (int(race_time),int(race_distance))

def day_5_part_1():
    string = """Time:        41     66     72     66
Distance:   244   1047   1228   1040"""

    print(run_possible_boats(string))

def day_5_part_2():
    string = """Time:        41     66     72     66
Distance:   244   1047   1228   1040"""

    time, distance = part_two_string(string)
    race = Smart_Race(time,distance)
    print(race.possible_solution)

def main():
    day_5_part_1()
    day_5_part_2()

if __name__ == "__main__":
    main()