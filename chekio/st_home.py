from datetime import datetime
import translate

'''
Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
затем перемножить эту сумму и последний элемент исходного массива. Не забудьте,
что первый элемент массива имеет индекс 0.
'''

def checkio(array: list) -> int:
    return sum(array[0::2])*array[-1] if array else 0

'''
Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). 
Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд . 
Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
'''

def checkio2(words: str) -> bool:
    check = 0
    for w in words.split(' '):
        if w.isalpha():
            check+=1
        else:
            check = 0
        if check == 3:
            return True
    return False

def first_word(text: str) -> str:
    return text.lstrip(',. ').split(' ')[0].split('.')[0].rstrip(',. ')

'''
У вас есть две даты в кортежах с тремя числами - год, месяц и день. Например, 19 апреля 1982 будет (1982, 4, 19). 
Вы должны найти разницу в днях между имеющимися датами.
'''

def days_diff(a, b):
    return abs((datetime(*b)-datetime(*a)).days)

#print(days_diff((2014, 8, 27), (2014, 1, 1)))

'''
you need to count the number of digits in a given string.
'''

def count_digits(text: str) -> int:
    res = 0
    for w in text:
        res += w.isdigit()
    return res



'''
Требуется обратить порядок букв в каждом слове предоставленной строки, так чтобы слова остались на своих местах.
backward_string_by_word('hello world') == 'olleh dlrow'
'''

def backward_string_by_word(text: str) -> str:


    return None

"""
 вы должны заменить все вхождения слова "right" на слова "left", 
 даже если это часть другого слова
"""

def left_join(phrases: tuple) -> str:
    if 0<len(phrases)<42:
        res = ''
        for word in phrases:
            res += word.replace('right', 'left')+','
        return res[:-1]

'''
In a given string you should reverse every word, 
but the words should stay in their places.
'''

def backward_string_by_word(text: str) -> str:
    if text == '' : return ""
    words = text.split(' ')
    res = ''
    for word in  words:
        res+= word[::-1]+' '
    return res[:-1]
'''
Ваша миссия тут - это найти ТОП самых дорогих товаров. Количество товаров, которые мы ищем, будет передано в первом аргументе, 
а сами данные по товарам будут переданы вторым аргументом.
'''
def bigger_price(limit: int, data: list) -> list:
    return sorted(data, key = lambda x: x['price'], reverse=True)[:limit]

# print(bigger_price(2, [
#     {"name": "bread", "price": 100},
#     {"name": "wine", "price": 138},
#     {"name": "meat", "price": 15},
#     {"name": "water", "price": 1}
# ]))


'''
You are given a string and two markers (the initial and final).
 You have to find a substring enclosed between these two markers. 
'''

def between_markers(text: str, begin: str, end: str) -> str:
    if begin not in text and end not in text:
        return text
    if text == '' or (end in text.split(begin)[0] and begin in text):
        return ''
    return text.split(begin)[-1].split(end)[0]


def checkio_un(data: list) -> list:
    return [num for num in data if data.count(num) > 1]


def popular_words(text: str, words: list) -> dict:
    if not text: return 0
    word_list = text.lower().split()
    d = {}
    for word in words:
        d.update({word: word_list.count(word.lower())})
    return d


def second_index(text: str, symbol: str) -> [int, None]:
    if text.count(symbol) < 2: return None
    first = text.index(symbol)+1
    return text[first:].index(symbol)+first


def frequency_sort(items):
    if not items: return []
    frequency_dict = {}
    for elem in items:
        frequency_dict.update({elem : items.count(elem)})
    s_list = sorted(frequency_dict.items(), key= lambda x: x[1], reverse=True)
    res_list = []
    for key, value in s_list:
        res_list.extend([key]*value)


# print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) )
# print(frequency_sort([4,6,2,2,2,6,4,4,4]))
# print(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) )


#You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements.
# If it has no elements, then two empty arrays should be returned.
def split_list(items: list) -> list:
    delim = len(items)//2 if not len(items)&1 else len(items)//2+1
    return [items[:delim], items[delim:]]


#In this mission you should check if all elements in the given list are equal.
from typing import List, Any
def all_the_same(elements: List[Any]) -> bool:
    if not elements or len(elements) == 1: return True
    first = elements[0]
    return all(map(lambda a: a==first, elements))

#print(all_the_same([1,1,1]))


MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code):
    words = code.split('   ')
    result = ''
    for word in words:
        result += ''.join([MORSE[letter] for letter in word.split()])+' '
    return result[0].upper()+result[1:-1]


def words_order(text: str, words: list) -> bool:
    if not all(map(lambda w : w in text.split(), words)): return False
    if len(words) == 1: return True

    prev = text.find(words[0])
    for word in words[1:]:
        f= text.find(word)
        if prev >= f or f == -1:
            return False
    return True



'''
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.
'''

def most_frequent(data: list) -> str:
    if not data: return []
    return sorted({elem:data.count(elem) for elem in data}.items(), key=lambda p:p[1], reverse=True)[0][0]

'''
Ваша цель сейчас — создать функцию, которая принимает на вход кортеж и возвращает кортеж из 3 элементов:
 первого, третьего и второго с конца элементов заданного массива.
'''
def easy_unpack(elements: tuple) -> tuple:
    return (elements[0],elements[2], elements[-2])

print(easy_unpack((6, 2, 9, 4, 3, 9)))

#Your task is simple - convert the input date and time from computer format into a "human" format.
# Обратите внимание, что слова "hour" и "minute" (в единственном числе) используются только когда время 01:mm (1 hour) или hh:01 (1 minute).
# Во всех остальных случаях следует использовать "hours" и "minutes".
# Для названий месяцев и остальных слов следует использовать их английские эквиваленты -
# January, February, March, April, May, June, July,
# August, September, October, November, December;
# year, hour/hours, minute/minutes
# Precondition :
# 0 < day <= 31
# 0 < month <= 12
# 0 < year <= 3000
# 0 <= hours < 24
# 0 <= minutes < 60

def date_time(time: str) -> str:
    from datetime import datetime
    t = datetime.strptime(time, "%d.%m.%Y %H:%M")
    result = str(t.day)+t.strftime(' %B %Y year ')
    result += str(t.hour) + ' hour ' if t.hour == 1 else str(t.hour) + ' hours '
    result += str(t.minute) + ' minute' if t.minute == 1 else str(t.minute) + ' minutes'
    return result

'''
Ваша задача - определить угол солнца над горизонтом, зная время суток. Исходные данные: 
солнце встает на востоке в 6:00, что соответствует углу 0 градусов. В 12:00 солнце в зените, 
а значит угол = 90 градусов. В 18:00 солнце садится за горизонт и угол равен 180 градусов. 
В случае, если указано ночное время (раньше 6:00 или позже 18:00), 
функция должна вернуть фразу "I don't see the sun!".
'''

from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    h, m = (map(int, time.split(':')))
    if h < 6 or (h >= 18 and m > 0):
        return "I don't see the sun!"
    return ((h-6)*60+m)*0.25

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("18:00") == 180
    assert sun_angle("18:01") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")



