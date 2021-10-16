"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""


def user_time():
    time_in_seconds = int(input("Enter time in seconds: "))
    housr = time_in_seconds // 3600
    minute = (time_in_seconds - housr * 3600) // 60
    second = time_in_seconds - housr * 3600 - minute * 60
    return f'{housr}:{minute}:{second}'


#output
# print(user_time())
# Enter time in seconds: 8000
# 2:13:20

######################
"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""


def user_number():
    number = list(input("Enter number: "))
    print('number', number)

    max = number[0]
    i = 0
    while i < len(number):
        if number[i] > max:
            max = number[i]
        i += 1
    return max

###############
#Waiting room

def last_chair(n):
    return n-1

def stray(arr):
    for i in set(arr):
        if arr.count(i) == 1:
            return i

def stray2(arr):
    return [x for x in set(arr) if arr.count(x) == 1][0]


####################
'''
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters 
after it in the alphabet. ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as
 they are. Only letters from the latin/english alphabet should be shifted, 
like in the original Rot13 "implementation".
'''

def rot13(message):
    part1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    part2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

    message_rot13 = ''
    for i in message:
        if part1.find(i) != -1:
            message_rot13 += part2[part1.find(i)]
        elif part2.find(i) != -1:
            message_rot13 += part1[part2.find(i)]
        else:
            message_rot13 += i
    return message_rot13


# def rot13(message):
#     return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))
#####################


'''
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in this way until a
 single-digit number is produced. The input will be a non-negative integer.
'''

def digital_root(n):
    str_n = str(n)
    print(str_n)
    if len(str_n) == 1:
        return n
    else:
        return digital_root(sum(map(int,str_n)))

# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))

#######################
'''
Your task is to add up letters to one letter.

The function will be given a variable amount of arguments, 
each one being a letter to add.

Notes:
Letters will always be lowercase.
Letters can overflow (see second to last example of 
the description)
If no letters are given, the function should return 'z'
'''


def add_letters(*letters):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not letters:
        return 'z'
    index_new_letter = sum([alphabet.index(i) + 1 for i in list(letters)]) - 1
    print(index_new_letter%26)
    if index_new_letter > 26:
         index_new_letter = index_new_letter % 26
    elif index_new_letter == 26:
        index_new_letter = 0
    return alphabet[index_new_letter]

# print(add_letters("o", "n", "u", "y", "l", "u", "o"))
# print(add_letters('y', 'c', 'b'))
# print(add_letters(add_letters("n", "r", "u", "q", "v", "m", "q", "w", "g")))

'''
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
'''
def row_sum_odd_numbers(n):
    col_piramide = sum([i+1 for i in range(n)])
    odd_list = [i for i in range(col_piramide*2 - n*2, col_piramide*2) if i%2 != 0]
    return sum(odd_list)

#ecsellent!
# def row_sum_odd_numbers(n):
#     #your code here
#     return n ** 3




