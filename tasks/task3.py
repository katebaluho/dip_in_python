"""
Написать функцию декоратор печатающую в файл дату и время момента декорирования функции и имя функции, и при каждом
вызове функции печатать дату и время момента вызова функции и имя функции
"""
from datetime import datetime
from itertools import groupby


def write_time(func):
    def wrapper(*args, **kwargs):
        info = func.__name__ +'-'+ str(datetime.now())
        try:
            with open('info.txt', 'a') as file:
                file.write(info+'\n')
        except OSError:
            print('Error write data in file')
        print(info)
        return func(*args, **kwargs)
    return wrapper


@write_time
def example(text):
    return 'How are you, '+text

print(example('Pavel'))


@write_time
def decode_string(text):
    try:
        if not text:
            raise ValueError

        letter = [s for s in text if not s.isdigit()]
        count = [int(''.join(i)) for is_digit, i in groupby(text, str.isdigit) if is_digit]

        if len(letter)!= len(count):
            raise ValueError

        return ''.join(list(map(lambda pair: pair[0]*pair[1] , zip(letter, count))))
    except ValueError:
        print('Text can\'t decode')
        return ''

print(decode_string('A10B3D2E1Q2'))
print(decode_string('A3B2A3)3*1f4'))
print(decode_string('A1Q1'))
print(decode_string('A14Q'))