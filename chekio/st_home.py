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
