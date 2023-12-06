

class Card():

    card_number:int
    winning_numbers:set[int]
    card_numbers:set[int]

    def __init__(self, string:str):
        string_list =  string.split(':')
        self.card_number = int(string_list[0][5:])
        string_list = string_list[1].split('|')
        win_string = string_list[0].split(' ')
        card_string = string_list[1].split(' ')
        self.winning_numbers = set(win_string)
        self.winning_numbers.discard('')
        self.card_numbers = set(card_string)
        self.card_numbers.discard('')

    def winning_value(self) -> int:
        val = 0
        for number in self.card_numbers:
            if number in self.winning_numbers and val==0:
                val = 1
            elif number in self.winning_numbers:
                val = val*2

        return val
    
    def duplicates_generated(self) -> int:
        return len(self.winning_numbers.intersection(self.card_numbers))
        
def day_4_part_1(string:str) -> int:
    string_list = string.split('\n')
    sum = 0
    for string in string_list:
        cur_card = Card(string)
        sum+= cur_card.winning_value()
    return sum

def day_4_part_2(string:str) -> int:
    pass

def main():
    with open('Day4/day_4_input.txt') as file:
        input = file.read()

    print(day_4_part_1(input))

if __name__ == "__main__":
    main()
    