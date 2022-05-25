"""
Написать функцию декоратор печатающую в файл дату и время момента декорирования функции и имя функции, и при каждом
вызове функции печатать дату и время момента вызова функции и имя функции
"""

from datetime import datetime
from itertools import groupby

def write_message(func):
    message = func.__name__ + '-' + str(datetime.now())
    try:
        with open('info.txt', 'a') as file:
            file.write(message + '\n')
    except OSError:
        message = 'Error write data in file'
    print(message)

def write_time(func):
    write_message(func)
    def wrapper(*args, **kwargs):
        write_message(func)
        return func(*args, **kwargs)
    return wrapper

@write_time
def example(text):
    return 'How are you, '+text

print(example('Pavel'))


