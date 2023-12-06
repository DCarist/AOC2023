
from dataclasses import dataclass 
#define some constants
SYMBOL_LIST_TEST = ['#', "$", "*", "+"]
SYMBOL_LIST = ['*', '&', '@', '/', '+', '-', '%', '$', '=', '#']
BLANK = '.'


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

    def __init__(self,input_list:list[str]):
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

    def find_symbol_code(self) -> int:
        
        sum = 0
        for symbol in self.symbol_list:
            sum+= self._compute_number(symbol.x_pos,symbol.y_pos)
            #don't want out of index or other funny business
        return sum
        #our components are in a list of lists [y][x]

    def find_gears(self) -> int:

        sum =0
        for symbol in self.symbol_list:
            if symbol.value == '*':
                sum += self._return_gear_ratio(symbol.x_pos, symbol.y_pos)

        return sum
    
    def _return_gear_ratio(self,x,y):
        """
            a gear is the * symbol with 2 sets of numbers around it.
            I believe we can re-use check_right, check_left
        """

        numbers = []
        numbers.append(self._check_right(x,y-1,True))
        num = len(numbers)
        if numbers[0] == 0 or self.component_list[y-1][x].value is BLANK:
            numbers.append(self._check_right(x+1,y-1))
            num += 1

        if self._check_left(x-1,y) != '':
            numbers.append(int(self._check_left(x-1,y)))
        numbers.append(self._check_right(x+1,y))

        numbers.append(self._check_right(x,y+1,True))
        #check the last entry to see if its non-zero
        if numbers[len(numbers)-1] == 0 or self.component_list[y+1][x].value is BLANK:
            numbers.append(self._check_right(x+1,y+1))
        
        non_zero = []
        for number in numbers:
            if number > 0:
                non_zero.append(number)

        if len(non_zero) ==2:
            return non_zero[0] * non_zero[1]
        else:
            return 0


    def _compute_number(self, x, y):
        """
            <- X-1,Y-1 X,Y-1, X+1, Y-1 ->
            <- X-1, Y  X,Y  , X+1, Y   ->
            <- X-1,Y+1 X,Y+1, X+1, Y+1 ->
        """
        num = 0
        #check up
        top_row = 0
        top_row +=self._check_right(x,y-1,True)
        if top_row == 0 or self.component_list[y-1][x].value is BLANK:
            top_row+=self._check_right(x+1,y-1)

        #check current line
        mid_row = 0
        if self._check_left(x-1,y) != '':
            mid_row+= int(self._check_left(x-1,y))
        mid_row+=self._check_right(x+1,y)

        #check down
        bottom_row = 0
        bottom_row+=self._check_right(x,y+1,True)
        if bottom_row == 0 or self.component_list[y+1][x].value is BLANK:
            bottom_row+=self._check_right(x+1,y+1)
        num = top_row + mid_row + bottom_row
        return num
    
    def _check_right(self, x,y, check_reverse=False):
        #start in the middle
        number_string:str = ''
        cur_pos = self.component_list[y][x-1].value
        if cur_pos != BLANK and check_reverse is True:
            #if the number before is not blank, go in reverse first.
            number_string = self._check_left(x-1,y)
        cur_pos = self.component_list[y][x].value
        while cur_pos != BLANK:

            number_string += cur_pos
            x+= 1
            if x == len(self.component_list[y] or x<0):
                break
            cur_pos = self.component_list[y][x].value
        
        if number_string != '':
            return int(number_string)
        else:
            return 0
        
    def _check_left(self,x,y) -> str:
        number_string:str = ''
        cur_pos = self.component_list[y][x].value
        while cur_pos != BLANK:
            number_string = cur_pos + number_string
            x-= 1
            cur_pos = self.component_list[y][x].value
        
        #print(number_string)
        if number_string != '':
            return number_string
        else:
            return number_string
        
def return_symbol_list(input:str) -> list[str]:
    symbol_list: list[str] = []
    for char in input:
        if char.isdigit():
            pass
        elif char == '.':
            pass
        elif char == '\n':
            pass
        elif char not in symbol_list:
            symbol_list.append(char)
    return symbol_list

def day_3_part_1(input:str) -> int:
    string_list = input.split('\n')
    engine = EngineSchematic(string_list)
    return engine.find_symbol_code()

def day_3_part_2(input:str) -> int:
    string_list = input.split('\n')
    engine = EngineSchematic(string_list)
    return engine.find_gear_ratio()

def main():
    with open('Day3/day_3_input.txt') as file:
        input = file.read()

    print(return_symbol_list(input))
    print(day_3_part_1(input))
    print(day_3_part_2(input))

if __name__ == '__main__':

    main()



