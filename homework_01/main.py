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


def filter_numbers(numbers, filter):
    mylist = []
    if filter == ODD:
        for num in numbers:
            if num % 2 == 1:
                mylist.append(num)
        return mylist
    if filter == EVEN:
        for num in numbers:
            if num % 2 != 1:
                mylist.append(num)
                print(mylist)
        return mylist
    if filter == PRIME:
        for num in numbers:
            if is_prime(num):
                mylist.append(num)
                print(mylist)
        return mylist