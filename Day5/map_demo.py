import re

def example_1_2():
    numbers = [1,2,3,4]
    squared = []

    for num in numbers:
        squared.append(num ** 2)

    print(squared)

    def square(number):
        return number ** 2

    squared2 = map(square, numbers)

    print(list(squared2))

    str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

    int_nums = map(int, str_nums)
    print(list(int_nums))

def example_3():
    numbers = [-2, -1, 0, 1, 2]

    abs_values = list(map(abs, numbers))
    print(abs_values)

    print(list(map(float,numbers)))


def string_example():
    words = ['Welcome', 'to', 'Real', 'Python']

    print(list(map(len,words)))

def multi_example():
    """
        Goes through the shorter of the two iterables..
    """
    first_it = [1,2,3]
    second_it = [4,5,6,7]

    print(list(map(pow,first_it,second_it)))

    #and some lambda examples.. spooky 
    print(list(map(lambda x,y: x-y, [2,4,6], [1,3,5])))

    print(list(map(lambda x,y,z: x+y+z, [2,4], [1,3], [7,8])))

def string_examples():
    string_it = ["processing", "strings", "with", "map"]
    print(list(map(str.capitalize, string_it)))

    print(list(map(str.upper, string_it)))

    with_dots = ["processing..", "...strings", "with....", "..map.."]

    print(list(map(lambda s: s.strip("."), with_dots)))


def parse_example():
    string = '48 52 2'.split(' ')
    print(list(map(int,string)))     

def re_example():
    example_string = 'This! has a, bunch.. of extra?? punctuation. Does[] count?'
    example_string = example_string.split(' ')
    print(list(map(remove_punctuation,example_string)))
    # No longer!! nice. 
def remove_punctuation(word:str) -> str:
    return re.sub('[!?.:;,"()-]',"", word)

def rotate_chr(c:str):
    rot_by = 3
    c = c.lower()
    alphabet= 'abcdefghijklmnopqrstuvwxyz'

    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    return chr(rotated_pos - len(alphabet))

def caesars_example():
    string = 'My secret message goes here.'

    print("".join(map(rotate_chr,string)))

    
if __name__ == "__main__":
    #string_examples()

    parse_example()
    re_example()
    caesars_example()