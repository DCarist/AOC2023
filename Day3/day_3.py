
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
        self.component_list: list[EngineComponent] = [[]]
        y=0
        self.symbol_list: list[EngineComponent] = []
        for line in input_list:
            x =0
            for char in line:
                self.schematic[y].append(char)
                #makes a simple nested list.
                is_symbol = char in SYMBOL_LIST
                cur_char = EngineComponent(char,x,y,is_symbol)
                self.component_list[y].append(cur_char)
                if is_symbol:
                    self.symbol_list.append(cur_char)
                x +=1 

            y +=1
            self.schematic.append([])
            self.component_list.append([])
        
        #print(self.component_list)
        #print(self.symbol_list)
        self.find_symbol_code()

    def find_symbol_code(self):
        
        for symbol in self.symbol_list:
            self._compute_number(symbol.x_pos,symbol.y_pos)
            #don't want out of index or other funny business

        #our components are in a list of lists [y][x]


    def _compute_number(self, x, y):
        """
            <- X-1,Y-1 X,Y-1, X+1, Y-1 ->
            <- X-1, Y  X,Y  , X+1, Y   ->
            <- X-1,Y+1 X,Y+1, X+1, Y+1 ->
        """
        
        #check up, down
        self._check_right(x,y-1)
        self._check_left(x,y+1)
        self._check_right(x,y+1)

    def _check_right(self, x,y):
        #start in the middle
        number_string:str = ''
        cur_pos = self.component_list[y][x].value
        while cur_pos != BLANK:

            number_string += cur_pos
            x+= 1
            cur_pos = self.component_list[y][x].value
        
        if number_string != '':
            return int(number_string)
        else:
            return
        
    def _check_left(self,x,y):
        number_string:str = ''
        cur_pos = self.component_list[y][x].value
        while cur_pos != BLANK:
            number_string = cur_pos + number_string
            x-= 1
            cur_pos = self.component_list[y][x].value
        
        print(number_string)
        if number_string != '':
            return int(number_string)
        else:
            return
        
    

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




