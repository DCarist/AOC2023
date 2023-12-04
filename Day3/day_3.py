
from dataclasses import dataclass 
#define some constants
SYMBOL_LIST = ['#', "$", "*", "+"]
BLANK = '.'
DEFAULT_WIDTH = 10

@dataclass
class EngineComponent():
    """
        Holds position, value of each engine component
    """
    value:str
    x_pos:int
    y_pos:int
    is_symbol:bool

    def __str__(self):
        return f'{self.value}:({self.x_pos},{self.y_pos}) {self.is_symbol}'

class EngineSchematic():
    """

    """

    def __init__(self,input_list:list[str], width=DEFAULT_WIDTH):
        #Assume we've taken the full string and split it into Y already (list)
        self.schematic:list[list[str]] =[[]]
        #schematic [x][y][value]
        self.component_list: list[EngineComponent] = []
        y=0
        for line in input_list:
            x =0
            for char in line:
                self.schematic[y].append(char)
                #makes a simple nested list.
                is_symbol = char in SYMBOL_LIST
                cur_char = EngineComponent(char,x,y,is_symbol)
                self.component_list.append(cur_char)
                x +=1 

            y +=1
            self.schematic.append([])
    
        print(self.schematic[1][3])
        print(self.component_list)

def day_3_part_1(input:str):
    
    string_list = input.split('\n')
    engine = EngineSchematic(string_list)


if __name__ == '__main__':
    input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    day_3_part_1(input)




