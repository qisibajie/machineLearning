# map and reduce
from functools import reduce

list_a = [1, 2, 3, 4, 5]


def square_number(number):
    return number * number


def convert_to_string(number):
    return str(number)


def sum_number(x, y):
    return x * 10 + y


list_r = list(map(convert_to_string, list_a))
print(list_r)

result_number = reduce(sum_number, list_a)
print(result_number)
