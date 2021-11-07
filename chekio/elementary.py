import math

"""
1.Since every string is an instance of the string class, it's preferred to use its methods rather than implement
a new function which seems to be faster. It won't work faster in most of the cases.
"""


def first_word(text: str) -> str:
    return text.split(' ')[0]


def first_word_2(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text


# количество цифр в числе
def number_length(a: int) -> int:
    if not a: return 1

    s = 0
    a = abs(a)
    while a > 0:
        a = a // 10
        print(a)
        s += 1
    return s


def number_length(number: int) -> int:
    return len(str(number))


def number_length(a: int) -> int:
    return int(math.log10(a)) + 1 if a else 1

# Try to find out how many zeros a given number has at the end.
def end_zeros(num: int) -> int:
    if not num: return 1
    s = 0
    while num%10 == 0:
        s += 1
        num = int(num/10)
    return s


def remove_all_before(items: list, border: int):
    if border in items:
        return items[items.index(border):]
    return items

#Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.
import  string

def is_all_upper(text: str) -> bool:
    for letter in text:
        if letter not in string.ascii_uppercase + ' ' + string.digits:
            return False
    return True

#In a given list the first element should become the last one. An empty list or list with only one element should stay the same.

def replace_first(items: list):
    if len(items) <= 1:
        return items
    items.insert(len(items),items.pop(0))
    return items

print(replace_first([1,2,3,65,9]))