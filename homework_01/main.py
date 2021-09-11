"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    for num in numbers:
        if (str(num).isdigit()):
            result = num ** 2
        return result



def is_prime(*n):
    for num in n:
        if (num == 3):
            print(num)
        if (num == 2):
            print(num)
        if (num != 1 and num % 2 != 0):
            if (num != 1 and num % 3 != 0):
                print(num)


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(n, filter):
    if filter == ODD:
        for num in n:
            if num % 2 == 1:
                print(num)
    if filter == EVEN:
        for num in n:
            if num % 2 != 1:
                print(num)
    if filter == PRIME:
        for num in n:
            is_prime(num)


filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], PRIME)
