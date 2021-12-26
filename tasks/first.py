"""На вход функции передается строка вида AAABBBEDDQQ функция должна сжать строку без потери информации и на выходе
ожидается строка вида A3B3ED2Q2
, так же реализовать функцию обратного декодирования,
найти и предусмотреть ситуации когда сжатие не возможно и возбудить исключение"""

from itertools import groupby


def encode_string(text):
    try:
        if not text or any(map(lambda letter: letter.isdigit(), text)):
            raise ValueError

        result = ''
        for letter, group in groupby(text):
            count_repeat = len(list(group))
            result += letter+str(count_repeat) if count_repeat != 1 else letter
        return result
    except ValueError:
        pass


def decode_string(text):
    try:
        if not text:
            raise ValueError

        group = [''.join(list(group)) for is_digit, group in groupby(text, str.isdigit)]
        result = ''
        for index in range(0, len(group), 2):
            count = int(group[index+1]) if index != len(group)-1 else 1
            result +=group[index]+group[index][-1]*(count-1)
        return result

    except ValueError:
        pass


print(decode_string('AKL3B13ED2Q2PU')) #AKLLLBBBBBBBBBBBBBEDDQQPU

