"""
Написать функцию на вход которой подается список с целыми числами
Результатом работы функции должен являться отсортированный по правилам список
Правила сортировки:
1 - количество объектов в входном списке
2 - значения в возрастающем порядке
например:
[3, 4, 11, 13, 11, 4, 4, 7, 3] >> [4, 4, 4, 3, 3, 11, 11, 7, 13]
[99, 99, 55, 55, 21, 21, 10, 10] >> [10, 10, 21, 21, 55, 55, 99, 99]
"""

def sort_list(data):
    if not data: return []
    return sorted(sorted(data), key=lambda num: data.count(num), reverse=True)


print(sort_list([3, 4, 11, 13, 11, 4, 4, 7, 3]))
print(sort_list([99, 99, 55, 55, 21, 21, 10, 10]))