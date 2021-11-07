'''
Write a function that checks whether all elements in an array are square numbers. The function should be able
to take any number of array elements.
Your function should return true if all elements in the array are square numbers and false if not.
An empty array should return undefined / None / nil. You can assume that all array elements will be positive integers.
is_square([1, 4, 9, 16]) --> True
is_square([3, 4, 7, 9]) --> False
is_square([]) --> None
'''

def is_square(arr):
    if not arr: return None

    for number in arr:
        print(number % (number ** 0.5))
        if number % (number ** 0.5):
            return False
    return True

#The all() function is an inbuilt function in Python
# which returns true if all the elements of a given iterable
# ( List, Dictionary, Tuple, set, etc) are True else it returns False.
def is_square2(arr):
    if arr:
        return all((a ** 0.5).is_integer() for a in arr)

'''
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
'''

def likes(names):
    templates = (
        'no one likes this',
        '{names[0]} likes this',
        '{names[0]} and {names[1]} like this',
        '{names[0]}, {names[1]} and {names[2]} like this',
        '{}, {} and {} others like this'
    )

    if len(names) >= 4:
        template_index =4
        return templates[template_index].format(names[0], names[1], len(names)-2)
    else:
        template_index = len(names)
        return templates[template_index].format(names = names)

def likes2(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

def likes3(names):
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }
    length = len(names)
    return d[min(4, length)].format(*names, others=length - 2)




