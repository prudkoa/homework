"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    list = []
    for num in numbers:
        if (str(num).isdigit()):
            result = num ** 2
            list.append(result)
    return list


def is_prime(number):
    for divider in range(2, number):
        if number % divider == 0:
            return False
    return True

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(numbers, type):
    mylist = []
    if type == ODD:
        return list(filter(lambda num: num % 2 == 1, numbers))
    if type == EVEN:
        return list(filter(lambda num: num % 2 != 1, numbers))
    if type == PRIME:
        return list(filter(lambda num:  is_prime(num) , numbers))

