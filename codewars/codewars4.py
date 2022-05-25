'''
Create a function to determine whether or not two circles are colliding. You will be given the position of both circles in addition to their radii:
def collision(x1, y1, radius1, x2, y2, radius2):
  # collision?
If a collision is detected, return true. If not, return false.
Here's a geometric diagram of what the circles passed in represent:
'''

import math

def collision(x1, y1, radius1, x2, y2, radius2):
    return math.hypot((x2-x1),(y2-y1)) < radius1+radius2

# print(collision(1, 1, 1, 1.1, 1.1, 0.1))
# print(collision(-1, 1, 10, -10.1, 1.1, 1))

#####################
'''
Given an array/list [] of integers , 
Construct a product array Of same size Such That prod[i] is equal to The Product 
of all the elements of Arr[] except Arr[i].
'''

def product_array(numbers):
    res = []
    for i in numbers:
        test_list = numbers.copy()
        test_list.pop(numbers.index(i))
        res.append(math.prod(test_list))
    return res

# def product_array(numbers):
#     p = math.prod(numbers)
#     return [p // i for i in numbers]

'''
Challenge:
Given a two-dimensional array of integers, return the flattened version of the array 
with all the integers in the sorted (ascending) order.
Example:
Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].
'''

def flatten_and_sort(array):
    new=[]
    for i in array:
        new.extend(i)
    return sorted(new)

# print(flatten_and_sort([[], [], [6]]))
#
# def flatten_and_sort(array):
#     return sorted(sum(array, []))

'''
Incrementer
Given an input of an array of digits, return the array with each digit incremented by its position in the array:
the first digit will be incremented by 1, the second digit by 2, etc. 
Make sure to start counting your positions from 1 (and not 0).

[1, 2, 3]  -->  [2, 4, 6]   #  [1+1, 2+2, 3+3]
[4, 6, 9, 1, 3]  -->  [5, 8, 2, 5, 8]  #  [4+1, 6+2, 9+3, 1+4, 3+5]
                                       #  9+3 = 12  -->  2
'''
def incrementer(nums):
    return [sum(pair)%10 for pair in zip(nums, range(1, len(nums)+1))]

#################
'''
Multiples of 3 or 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
Additionally, if the number is negative, return 0 (for languages that do have them).
Note: If the number is a multiple of both 3 and 5, only count it once.
'''
def solution(number):
    if number < 0:
        return 0
    return sum(i for i in range(number) if not i%3 or not i%5)

########
'''
Stop gninnipS My sdroW!
spinWords("Hey fellow warriors") => "Hey wollef sroirraw" 
'''

def spin_words(sentence):
    res = ''
    words = sentence.split()
    for one_word in words:
        res += ''.join([one_word[::-1]+' ' if len(one_word) >= 5 else one_word+' '])
    return res[-1]

def spin_words2(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

####################

'''
Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, 
что один любой символ (в том числе пробел) стоит 6060 копеек. 
Ответ дайте в рублях и копейках в соответствии с примерами.
'''
# cost = round(len(st)*0.6,2)
# print(f'{int(cost)} р. {round(cost%1*100)} коп.')


number = 2020%12
years = ['Обезьяна', 'Петух', 'Собака', 'Свинья', 'Крыса', 'Бык', 'Тигр', 'Заяц', 'Дракон', 'Змея', 'Лошадь', 'Овца']
#print(years[number])

list1 = [
  { 'firstName': 'Gabriel', 'lastName': 'X.', 'country': 'Monaco', 'continent': 'Europe', 'age': 49, 'language': 'PHP' },
  { 'firstName': 'Odval', 'lastName': 'F.', 'country': 'Mongolia', 'continent': 'Asia', 'age': 38, 'language': 'Python' },
  { 'firstName': 'Emilija', 'lastName': 'S.', 'country': 'Lithuania', 'continent': 'Europe', 'age': 19, 'language': 'Python' },
  { 'firstName': 'Sou', 'lastName': 'B.', 'country': 'Japan', 'continent': 'Asia', 'age': 49, 'language': 'PHP' },
]
def sor():
    sorted_array = sorted(list1,key=lambda d:d['age'], reverse=True)
    return list(filter(lambda d:d['age'] == sorted_array[0]['age'],sorted_array))


def decompose(n):
    goal = 0
    result = [n]
    while result:
        current = result.pop()
        goal += current ** 2
        print(goal)
        for i in range(current - 1, 0, -1):
            if goal - (i ** 2) >= 0:
                goal -= i ** 2
                result.append(i)
                print('res', result)
                if goal == 0:
                    result.sort()
                    return result
    return None


def wave_sort(a):
    a.sort()
    for i in range(0,len(a)-1,2):
        a[i], a[i + 1] = a[i + 1], a[i]


def from_nb_2_str(n, modsys):
    res = [n%m for m in modsys]
    print(res)
    res_check = res
    while res:
        elem = res.pop()
        print(elem)
        if elem!= 0 and any(map(lambda k: k%elem==0, res)):
            return "Not applicable"

    return '-'+'--'.join(res)+'-'

'''
Complete the solution so that it strips all text that follows any of a set 
of comment markers passed in. Any whitespace at the end of the line 
should also be stripped out.
'''

def solution(string,markers):
    import re
   # pattern = '(#|!)(.*?)(\\n|$)'
    pattern = '#[\s\S]*?\\n|![\s\S]*?$'
    s = re.split(pattern, string)

    return s

#print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
#print(solution("a #b\nc\nd $e f g", ["#", "$"]))

def find_uniq(arr):
    s = list(set(arr))
    return s[0] if arr.count(s[0])==1 else s[1]

#print(find_uniq([ 0, 0, 0.55, 0, 0 ]))





