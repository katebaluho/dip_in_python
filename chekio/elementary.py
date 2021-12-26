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


def number_length1(number: int) -> int:
    return len(str(number))


def number_length2(a: int) -> int:
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


#You have a number and you need to determine which digit in this number is the biggest.

def max_digit(number: int) -> int:
    # your code here
    return max([int(i) for i in str(number)])


#Split the string into pairs of two characters. If the string contains an odd number of characters,
# then the missing second character of the final pair should be replaced with an underscore ('_').

def split_pairs(a):
    if len(a) & 1:
        a = a +'_'
    return [a[i:i+2] for i in range(0,len(a),2)]


#You have a string that consist only of digits. You need to find
# how many zero digits ("0") are at the beginning of the given string.

def beginning_zeros(number: str) -> int:
    counter = 0
    for idx, num in enumerate(number,0):
        if number[idx] != '0':
            break
        counter = idx+1
    return counter


def beginning_zeros1(number: str) -> int:
    return len(number) - len(number.lstrip('0'))


def nearest_value(values: set, one: int) -> int:
    if one in values:
        return one
    if max(values) < one:
        return max(values)
    if min(values) > one:
        return min(values)
    numbers = list(values)
    numbers.append(one)
    numbers.sort()
    idx = numbers.index(one)
    if idx == 0: return one
    return numbers[idx-1] if numbers[idx] - numbers[idx-1] <= numbers[idx+1] - numbers[idx] else numbers[idx+1]


def nearest_value1(values: set, one: int) -> int:
    return min(sorted(values), key=lambda i: abs(i - one))

'''
Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, 
заключенный между двумя этими маркерами. Но есть несколько важных условий.

Это упрощенная версия миссии Between Markers .

Начальный и конечный маркеры всегда разные.
Начальный и конечный маркеры всегда размером в один символ.
Начальный и конечный маркеры всегда есть в строке и идут один за другим.
'''

def between_markers(text: str, begin: str, end: str) -> str:

    return text[text.index(begin)+1:text.index(end)]

print(between_markers('What is >apple<', '>', '<'))

'''
На вход Вашей функции будет передано одно предложение.
 Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.'''

def correct_sentence(text: str) -> str:
    if text[-1] != '.':
        text += '.'

    return text[0].upper()+text[1:]

'''Проверить является ли число четным или нет. 
Ваша функция должна возвращать True если число четное, и False если число не четное.'''

def is_even(num: int) -> bool:
    return num & 1 == 0


'''Вам дан текст в котором нужно просуммировать числа, но только разделенные пробелом. 
Если число является частью слова, то его суммировать не нужно.'''

def sum_numbers(text: str) -> int:
    res = 0
    for words in text.split(' '):
        if words.isdigit():
            res += int(words)
    return res
