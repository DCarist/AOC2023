
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