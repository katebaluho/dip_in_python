#создать плоский список из списка любой глубины

# from distutils.command.clean import clean
# from functools import wraps


# def flat_list(example):
#     result = []
#     while(example):
#         itm = example.pop(0)
#         print('111', itm)
#         if isinstance(itm, list):
#             itm.extend(example)
#             print('item' , itm)
#             print('ex', example)
#             example = itm
#         else:
#             result.append(itm)
#     return result

#print(flat_list([[1,2],[[3,5],[6,7]]]))

# a = [0]
# b = a
# b[0]=1
# print(a, b) #[1] [1]

# a = [0]
# b = a * 2
# b[0] = 2
# print(a, b) [0] [2, 0]

# row = [0]*2
# matrix = [row]*2
# print(matrix)
# matrix[0][0] = 2
# print(matrix)  [[2, 0], [2, 0]]

# a = [0]
# a += (1,)
# a += {2}
# a += 'ab'
# a += {1:2}
# print(a)   [0, 1, 2, 'a', 'b', 1]

# def appended(am):
#     am += [1]
#     return am

# a = [5]
# print(appended(a))  # -> [5, 1]
# print(a)            # -> [5, 1]

#Copy ###########
# import copy

# data = ['125698', [1,5] , 3]
# print(data is copy.copy(data))
# print(data[1] is copy.copy(data)[1])
# print(data[1] is copy.deepcopy(data)[1])

#аннтотация типов
# price: int = 5
# title: str

# def indent_right(s: str, width: int) -> str:
#     return " " * (max(0, width - len(s))) + s

# class Book:
#     title: str
#     author: str

#     def __init__(self, title: str, author: str) -> None:
#         self.title = title
#         self.author = author

# b: Book = Book(title='Fahrenheit 451', author='Bradbury')


# class Person:

#     def __init__(self, name):
#         self.name = name
    
#     @property
#     def name(self):
#         return name

#     def display_info(self):
#         print(f'Name {self.name}')


# class Employee(Person):

#     def work(self):
#         print(f'{self.name} works')


# class A:
#     def __init__(self):
#         self.x = 10


# class B(A):
#     def __init__(self):
#         super().__init__()  # <- не забудь!
#         self.y = self.x + 5
# print(B().y)  # 15


# class A:
#     def __init__(self, x):
#         self.x = x
# class B(A):
#     def __init__(self, x):
#         super(B, self).__init__(x)

#############decorators############
# import functools 
# def decorator(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         result = func(*args,**kwargs)
#         return result
#     return wrapper

# @decorator
# def some():
#     return 'Hello'

# @decorator
# def some2():
#     pass

# def some3():
#     pass

# res = decorator(some3)

#######################
# def outer(b = 1):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             result = func(*args,**kwargs)
#             return result
#         return wrapper
#     return decorator

# @outer(8)
# def some4():
#     pass

# some4()

# dec = outer(123)
# witout_sugar_result = dec(some4)
# print(witout_sugar_result)

# witout_sugar_result2 = outer(123)(some4)

##example decorator

# def uppercase(func):
#     @wraps(func)
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper


# def greet():
#     return 'hello'

# result=uppercase(greet)
# print(result())

#№№№№№№№№№№№№№№№№№№замыкание
# def mul(a):
#     def helper(b):
#         return a*b
#     return helper

# print(mul(5)(2))
# mul5 = mul(5)
# print(mul5(30))

# tpl = lambda a, b: (a, b)
# a = tpl(1, 2)
# b = tpl(3, a)
# c = tpl(a, b)
# print(c)

#№№№№№№№№№№№№№№№№№№абстрактные классы
# from abc import ABC, abstractclassmethod

# class A(ABC):
#     @abstractclassmethod
#     def greet():
#         pass

# class B(A):
#     def greet(self):
#         print('Hello')

# B().greet()

# example = {1:5,2:6, True:8}
# print(example[True])

#самый повторяющийся элемент в списке
# some_list = [10, 10, 23, 10, 123, 66, 78, 123] 

# result = {}
# for element in some_list:
#     result.update({element:some_list.count(element)})

# clean_dict = max({element:count for element, count in result.items() if count>1})

# print(clean_dict)

#№№№№№№№№№№№№№№самый дешевый и дорогой продукт
# prices = {
#     "banana": 1.20,
#     "pineapple": 0.89,
#     "apple": 1.57,
#     "grape": 2.45,
# }

# min(prices.items(), key=lambda item: item[1])
# ('pineapple', 0.89)

# max(prices.items(), key=lambda item: item[1])
# ('grape', 2.45)

#№№№№№№№№№№№№ проверка что два  числа взаимно просты
# def are_coprime(a, b):
#     for i in range(2, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             return False
#     return True


# are_coprime(2, 3)

# are_coprime(2, 4)

#№№№№№№№№№№№пример сортировки
# def reverse_word(word):
#     return word[::-1]

# words = ['banana', 'pie', 'Washington', 'book']
# sorted(words, key=reverse_word)

# print(sorted((1,13,6,9)))

#################итератор
# class SimpleIterator:
#     def __iter__(self):
#         return self

#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0

#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return 1
#         else:
#             raise StopIteration

# simple_iter = SimpleIterator(5)

# for i in simple_iter:
#     print(i)

#наследование
# class Animal(object):
#     def __init__(self, name):
#         self.name = name

#     def say(self):
#         print(self.name + " хочет что-то сказать")

#     def swim(self):
#         print(self.name + " подходит к воде")


# class Cat(Animal):
#     def say(self):
#         super(Cat, self).say()
#         print(self.name + " говорит Мяу")