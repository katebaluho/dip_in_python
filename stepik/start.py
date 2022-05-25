# подсчет точек в четвертях координат
def coord():
    check_func = {
        1: lambda x, y: True if x > 0 and y > 0 else False,
        2: lambda x, y: True if x < 0 and y > 0 else False,
        3: lambda x, y: True if x < 0 and y < 0 else False,
        4: lambda x, y: True if x > 0 and y < 0 else False,
    }

    result = {
        1: ['Первая четверть:', 0],
        2: ['Вторая четверть:', 0],
        3: ['Третья четверть:', 0],
        4: ['Четвертая четверть:', 0],
    }

    col = int(input(">"))
    coord = []
    for i in range(col):
        x, y = input('>').split()
        coord.append((int(x), int(y)))

    for pair in coord:
        x, y = pair
        for num, check in check_func.items():
            if check(x, y):
                result[num][1] += 1
                continue
    print()
    for info in result.values():
        title, num = info
        print(title, num)


def more_than_provous():
    numbers = list(map(int, input('>').split()))
    counter = 0
    for idx, num in enumerate(numbers[:len(numbers) - 1]):
        if num < numbers[idx + 1]:
            counter += 1
    print(counter)

    '''
    a = tuple(map(int, input().split()))
    print(sum(a[i - 1] < a[i] for i in range(1, len(a))))
    '''


'''
Напишите программу, 
которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.)
'''


def next_prevous():
    l = list(map(int, input().split()))
    for i in range(0, len(l) - 1, 2):
        l[i], l[i + 1] = l[i + 1], l[i]
    print(*l)


def sdvig():
    l = list(map(int, input().split()))
    print(*(l[-1:] + l[0:len(l) - 1]))
    print(*[l[-1]] + l[:-1])
    print(l.pop(), *l)


def multi():
    numbers = [int(input()) for _ in range(int(input()))]
    check = int(input())
    answer = ("НЕТ", "ДА")
    flag = 0
    for idx, x in enumerate(numbers):
        for y in numbers[idx + 1:]:
            print(x, y)
            if x * y == check:
                flag = 1
                break
    print(answer[flag])


def stone_paper():
    players = {
        'Тимур': input(),
        'Руслан': input(),
    }
    win_strategy = {
        'камень': 'ножницы',
        'ножницы': 'бумага',
        'бумага': 'камень',
    }

    if players['Тимур'] == players['Руслан']:
        print('ничья')
        exit()
    if win_strategy[players['Тимур']] == players['Руслан']:
        print('Тимур')
        exit()
    print('Руслан')


def stone_paper__with_add():
    players = {
        'Тимур': input(),
        'Руслан': input(),
    }
    win_strategy = {
        'камень': ['ножницы', 'ящерица'],
        'ножницы': ['бумага', 'ящерица'],
        'бумага': ['камень', 'Спок'],
        'ящерица': ['бумага', 'Спок'],
        'Спок': ['ножницы', 'камень'],
    }

    if players['Тимур'] == players['Руслан']:
        print('ничья')
        exit()
    if players['Руслан'] in win_strategy[players['Тимур']]:
        print('Тимур')
        exit()
    print('Руслан')


def o_r():
    s = input()
    if s.count('Р') == 0:
        print(0)
        exit()
    print(max([len(el) for el in s.split('О')]))


def anton():
    titles = [input() for _ in range(int(input()))]
    res = []
    for id, title in enumerate(titles, 1):
        counter = 0
        for letter in 'anton':
            if letter in title:
                title = title[title.index(letter) + 1:]
                counter += 1
        if counter == 5:
            res.append(str(id))
    print(' '.join(res))

    # for i in range(int(input())):
    #     s, virus, x = input(), 'anton', 0
    #     for sym in s:
    #         if sym == virus[x]:
    #             x += 1
    #         if x == 5:
    #             print(i + 1, end=' ')
    #             break

    # print(*[k + 1 for k in range(int(input()))
    #         if __import__('re').match(".*a.*n.*t.*o.*n.*", input())])

    # import re
    # sample = r'a.*n.*t.*o.*n'
    # result = []
    # n = int(input())
    # for k in range(n):
    #     if re.findall(sample, input()):
    #         result.append(k + 1)
    # print(*result)
    #
    # import re
    # num = int(input())
    # for i in range(num):
    #     if re.search(r'.*a.*n.*t.*o.*n', input()):
    #         print(i + 1, end=' ')


def ban_letter():
    word = input()+' запретил букву'
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    for letter in alphabet:
        if letter in word:
            print(word.replace('  ', ' ').strip() ,letter)
            word = ''.join([s for s in word.split(letter) if s])


def grow_list():
    n = int(input())
    res = []
    for li in range(n):
        print([el for el in range(1, n+1)])


def grow_list2():
    n = int(input())
    res = []
    counter = 2
    while counter <= n+1:
        print([el for el in range(1, counter)])
        counter += 1


# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)
# m = 3
# n = 4
# c = [[input() for _ in range(m)] for _ in range(n)]
# print(c)

def matr1():
    n , m = int(input()), int(input())
    c = [[input() for _ in range(m)] for _ in range(n)]
    [print(' '.join(row)) for row in c]
    print('')
    [print(' '.join(row)) for row in zip(*c)]

def matr2():
    n = int(input())
    c = [input().split(' ') for _ in range(n)]
    sum = 0
    for i in range(n):
         sum += int(c[i][i])
    print(sum)

def matr3():
     n = int(input())
     c = [input().split(' ') for _ in range(n)]

a = [[1,2], [3,4]]
def matr4():
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    B = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]
    print(list(zip(A, B)))
    [print(list(zip(*row))) for row in zip(A,B)]
    c = [ list(map(sum, zip(*row))) for row in zip(A,B)]
    print(c)
matr4()


