

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
    
    def __repr__(self):
        return f' C: {self.card_number} WN:{self.duplicates_generated()}'
    
class Deck():

    deck:list[list[Card]]
    card_count:int
    current_card:int=0

    def __init__(self,deck:list[list[Card]]=[[]]):
        self.deck = deck
        self.card_count = len(self.deck)

    def append(self, card:Card) -> None:
        self.deck[self.card_count-1].append(card)
        self.deck.append([])
        self.card_count = len(self.deck)

    def copy_card(self,card:Card, position:int) -> None:
        self.deck[position].insert(position, card)
        self.card_count = len(self.deck)

    def process_cards(self):
        self.deck.pop(-1)
        for card_list in self.deck:
            self.cards_to_copy(card_list)

    def cards_to_copy(self, card_list:list[Card]):
        print(f'Starting Line: {card_list[0]}')
        for card in card_list:
            cards_copy = card.duplicates_generated()
            card_offset = self.current_card +1
            while cards_copy >0:
                self.copy_card(self.deck[card_offset][0], card_offset)
                cards_copy -= 1
                card_offset += 1
                
        self.current_card += 1

            #okay lol it works but I don't know why.
    def __len__(self):
        length = 0
        for card_list in self.deck:
            length += len(card_list)
        
        return length
    
    def return_location_of_next_card(self, cur_card:Card):
        index = cur_card.card_number   


def day_4_part_1(string:str) -> int:
    string_list = string.split('\n')
    sum = 0
    for string in string_list:
        cur_card = Card(string)
        sum+= cur_card.winning_value()
    return sum

def day_4_part_2(string:str) -> int:
    string_list = string.split('\n')
    part_2_deck = Deck()
    for string in string_list:
        part_2_deck.append(Card(string))

    part_2_deck.process_cards()

    return len(part_2_deck)
            

def main():
    with open('Day4/day_4_input.txt') as file:
        input = file.read()

    print(day_4_part_1(input))
    print(day_4_part_2(input))

if __name__ == "__main__":
    main()
    