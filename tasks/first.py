"""На вход функции передается строка вида AAABBBEDDQQ функция должна сжать строку без потери информации и на выходе
ожидается строка вида A3B3ED2Q2, так же реализовать функцию обратного декодирования,
найти и предусмотреть ситуации когда сжатие не возможно и возбудить исключение"""

from itertools import groupby


def encode_string(text):
    try:
        if not text or any(map(lambda letter: letter.isdigit(), text)):
            raise ValueError

        return ''.join([k+str(len(list(g))) for k, g in groupby(text)])
    except ValueError:
        print('Text can\'t encode')
        return ''


print(encode_string('AAABBBEDDQQ')) #A3B3D2E1Q2
print(encode_string('AQ'))  #A1Q1
print(encode_string('AAABBAAA)))*ffff'))
print(encode_string('AAABB7AAA)))*ffff')) #A3B2A3)3*1f4
print(encode_string(''))


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
