#просто примеры


# Задачи на типы данных

# Задачи на типы данных

def get_odd_numbers(numbers): # Создаем функцию get_odd_numbers, которая принимает кортеж numbers в качестве аргумента.
    odd_numbers = [number for number in numbers if number % 2 != 0] # Генератор списка проверяет каждое число в numbers и добавляет в список odd_numbers только нечетные числа.
    return tuple(odd_numbers) # Преобразуем список odd_numbers в кортеж и возвращаем его.

numbers = (1, 2, 3, 4, 5, 6, 7) # Создаем кортеж numbers с числами.
odd_numbers = get_odd_numbers(numbers) #  Вызываем функцию get_odd_numbers с кортежем numbers в качестве аргумента и присваиваем результат переменной odd_numbers.
print(odd_numbers)


def get_colors_users(users_colors): # Создается функция get_colors_users, которая принимает входной словарь users_colors в качестве аргумента.

  colors_users = {} # Создается пустой словарь colors_users, который будет содержать результаты.
  for user, colors in users_colors.items(): # Начинается цикл for, который перебирает все пары “ключ-значение” в словаре users_colors.
    for color in colors: # Начинается вложенный цикл for, который перебирает все цвета в списке colors.
      if color not in colors_users: # Проверяется, существует ли уже ключ color в словаре colors_users. Если нет, то создается новый ключ color и соответствующее пустое значение (список).
        colors_users[color] = []
      colors_users[color].append(user) # Добавляется имя пользователя user в список, соответствующий цвету color.
  return colors_users # Возвращается новый словарь colors_users, где ключи — цвета, а значения — списки пользователей, которые любят этот цвет.

users_colors = {'Alice': ['Red', 'Green'], 'Bob': ['Blue', 'Green'], 'Charlie': ['Red', 'Yellow']}
print(get_colors_users(users_colors))



def get_difference(set1, set2): # Создается функция get_difference, которая принимает два множества set1 и set2 в качестве аргументов.

  return set1 - set2 # Используется оператор - для вычитания множеств. set1 - set2 возвращает новое множество, которое содержит элементы, присутствующие в set1, но отсутствующие в set2.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
difference_set = get_difference(set1, set2) # Вызывается функция get_difference с множествами set1 и set2 в качестве аргументов. Результат присваивается переменной difference_set.
print(difference_set)  # Вывод: {1, 2}


def reverse_and_sort(numbers):
    """Переворачивает и сортирует список."""
    reversed_numbers = numbers[::-1]  # Переворачиваем список
    sorted_numbers = sorted(reversed_numbers, reverse=True)  # Сортируем в порядке возрастания
    return sorted_numbers  # Возвращаем отсортированный список

numbers = [5, 2, 8, 1, 9]
result = reverse_and_sort(numbers)  # Вызываем функцию и сохраняем результат
print(result)  # Выводим результат



def get_average_grades(student_grades): #  Создается функция get_average_grades, которая принимает входной словарь student_grades в качестве аргумента.

  average_grades = {} # Создается пустой словарь average_grades, который будет содержать результаты.
  for student, grades in student_grades.items(): # Начинается цикл for, который перебирает все пары “ключ-значение” в словаре student_grades.
    average_grade = sum(grades) / len(grades) #  Вычисляется средний балл average_grade для студента student с помощью функций sum и len.
    average_grades[student] = round(average_grade, 2)  # Округление до 2 знаков после запятой. В словарь average_grades добавляется новая пара “ключ-значение”, где ключ — student (имя студента), а значение — round(average_grade, 2)
  return average_grades

student_grades = {'Alice': [85, 90, 75], 'Bob': [92, 88, 95], 'Charlie': [70, 80, 85]}
result = get_average_grades(student_grades)
print(result)


def get_common_words(set1, set2):
    new_set = set()
    for word in set1:
        if word in set2:
            new_set.add(word)
    return new_set
set1 = {'apple', 'banana', 'cherry', 'grape'}
set2 = {'banana', 'grape', 'orange', 'kiwi'}
new_set = get_common_words(set1, set2)
print(new_set)

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 and 17 in numbers:
    print('YES')
else:
    print('NO')
del numbers[0]
del numbers[-1]
print(numbers)


def f():
    return 3
def test_function():
    assert f() == 4


def find_or_insert_position(numbers, target):
    """
    Находит целевое число в отсортированном списке или возвращает позицию для вставки.

    Args:
        numbers: Отсортированный список уникальных целых чисел.
        target: Целевое число для поиска.

    Returns:
        Индекс целевого числа в списке, если оно найдено, иначе индекс, где его нужно вставить.
    """
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


# Пример использования:
numbers = [2, 5, 7, 8, 11, 12]
target = 3

position = find_or_insert_position(numbers, target)

if position < len(numbers) and numbers[position] == target:
    print("Целевое число найдено на индексе:", position)
else:
    print("Целевое число отсутствует, его нужно вставить на индекс:", position)





var = None
print(type(var))


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis
def greet():
    return 'Hello!'
print(greet())



list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)

print(list1)

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].append(', '.join(sub_list))
print(list1)



list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
rev=[]
for i in list1:
    i.reverse()
    rev.append(i)

print(rev)


#Decorator
# from functools import wraps +
def dec(func):
#   @wrape(func) или так +
    def qua(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    qua.__name__ = func.__name__ # или так -
    qua.__doc__ = func.__doc__ # -
    return qua

# или так
def say(name, lastname, age):
    print('hi', name, lastname, age)
say = dec(say)
say('Vas', 'bye', 30)

# или так
@dec
def say(age):
    print(age**2)
say(30)




def print_given(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)
print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3)


def decor(func):

    def zam(*args, **kwargs):

        print('test')
        func(*args, **kwargs)
    return zam

@decor
def qua(s, a, y):
    print('hello', s, a, y)
qua(5, 6, '= ...')


# ООП

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
def bark(self):
    print(f"{self.name} лает!")

my_dog = Dog("Рекс", "Овчарка")
print(my_dog.__dict__)


class Point:
    color = 'red'
    circle = 2

    def __init__(self, color, circle):
        print('__init__')
        self.color = color
        self.circle = circle

    def __del__(self):
        print('delete' + str(self))

    def new(self, color, circle):
        self.color = color
        self.circle = circle

    def new_2(self):
        return (self.color, self.circle)

pt = Point('yellow', 4)
pt.new('red', 3)
print(pt.__init__)



class Person:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def status(year_of_birth):
        if 2021 - year_of_birth >= 18:
            print('Вы можете смотреть все страницы сайта')
        else:
            print('Часть страниц вам не доступна')


student = Person('Петр')
# Тесты
student.status(2002)
Person.status(2011)







class Soda:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')


# Тесты
drink1 = Soda()
drink2 = Soda('малина')
drink3 = Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()


class TriangleChecker:
    def __init__(self, dlin=None):
        if dlin and len(dlin) == 3:
            self.dlin = dlin
        else:
            self.dlin = None
    def is_triangle(self):
        if self.dlin:
            print(f'Ура, можно построить треугольник!')
        else:
            print('Жаль, но из этого треугольник не сделать')



Tri0 = TriangleChecker()
Tri1 = TriangleChecker([1, 1, 2])
Tri2 = TriangleChecker([2, 3, 2])
Tri0.is_triangle()
Tri1.is_triangle()
Tri2.is_triangle()




############

class KgToPounds:

    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            raise ValueError('Килограммы задаются только числами')

    def get_kg(self):
        return self.__kg

    kg = property(get_kg, set_kg)



class Nikola:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
    def preo(self):
        if self.name is not None and self.name != 'Николай':
            print(f'Я не {self.name}, а Николай')
        else:
            print('Привет, Николай')

name = Nikola()
name1 = Nikola('Николай', 25)
name3 = Nikola('Макс', 24)
name.preo()
name1.preo()
name3.preo()



class RealString:

    def __init__(self, an=None, rus=None):
        self.an = an
        self.rus = rus
    def mat(self):
        if self.an and self.rus is not None:

            if self.an > self.rus:
                print(f'{self.an}')
            else:
                print(f'{self.rus}')

rew = RealString()
rew1 = RealString('Apple', 'Яблоко')
rew2 = RealString('Zoo', 'Азбука')
rew.mat()
rew1.mat()
rew2.mat()




class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def Busi(self, color='white'):
        self.color = color
        print(
            f'Цвет: {self.color}, Название автомобиля: {self.name}, Скорость: {self.max_speed}, Пробег: {self.mileage}')

class Car(Vehicle):
    def Cari(self, color='white'):
        self.color = color
        print(
            f'Цвет: {self.color}, Название автомобиля: {self.name}, Скорость: {self.max_speed}, Пробег: {self.mileage}')


School_bus = Bus("School Volvo", 180, 12)
Cari = Car("Audi", 280, 52)
School_bus.Busi()
Cari.Cari()



class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self):
        return self.capacity * 100 + (self.capacity * 100)//10

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())




class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))



class Circle:
    def __init__(self, r=None):
        self.r = r
    def s_p(self):
        if self.r is not None:
            S = 3.14 * self.r ** 2
            p = 2*3.14*self.r
            print(S, p, self.r)

sp = Circle(5)
sp.s_p()


class Person:

    def __init__(self, name1=None, country=None, hb=None):
        self.name1 = name1
        self.country = country
        self.hb = hb

    def search(self):
        if self.name1 and self.country and self.hb is not None:
            age = 2024 - self.hb
            return  f'{self.name1} из {self.country} родился в {self.hb} году и сейчас ему {age}'

rec = Person("Паша", "Уссурийск", 1999)
print(rec.search())



def qua(x, y):
    if x > y:
        return x
    else:
        return y

sea = qua(2, 5)
print(sea)



class Forma:

    def __init__(self, rad, a, b):
        self.rad = rad
        self.a = a
        self.b = b

class Krug(Forma):
    def s_p_krug(self):
        S = 3.14 * self.rad ** 2
        p = 2 * 3.14 * self.rad
        return f'Площадь круга {S} и его периметр {p}'

class Kvad(Forma):
    def s_p_kvad(self):
        S = self.a * self.b
        p = self.a * 2 + self.b * 2
        return f'Площадь квадрата {S} и его периметр {p}'


sea = Krug(5, 7, 8)
sea1 = Kvad(6, 6, 6)
print(sea.s_p_krug())
print(sea1.s_p_kvad())

class Node:
    # Initialize the Node object with a value, and set the left and right child pointers to None
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Define a custom __str__ method to convert the node's value to a string
    def __str__(self):
        return str(self.value)

# Define a class called BinarySearchTree to represent a binary search tree
class BinarySearchTree:
    # Initialize the BST with an empty root node
    def __init__(self):
        self.root = None

    # Insert a value into the BST
    def insert(self, value):
        # If the root is None, create a new node with the given value as the root
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    # Helper method to recursively insert a value into the BST
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Helper method to recursively search for a value in the BST and return the node if found
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

# Example usage
# Create an instance of BinarySearchTree
bst = BinarySearchTree()

# Insert values into the BST
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Search for elements in the BST and print the results
print("Searching for elements:")
print(bst.search(5))  # Found, returns the node (4)
print(bst.search(9))  # Not found, returns None


def revert_int_option_1(num):
    print('Option 1: Use reversed() method')
    return int(''.join(list(reversed(str(num)))))


def revert_int_option_2(num):
    print('Option 2: Use slices')
    return int(str(num)[::-1])


print(revert_int_option_1(12345))
print(revert_int_option_2(12345))

x = 123456
print(int(str(x)[::-1]))


xx = 371
digits = list(str(xx))  # Преобразуем число в строку и разбиваем на символы
digits = [int(digit) for digit in digits]
y = []
z = 0
for i in range(len(digits)):
    z+=digits[i]**(len(digits))
print(z)


num = [1, 2, 3, 333, 5, 6, 9, 77, 8, 5, 10, 73, 83, 113]
nums = []
for i in num:
    for j in range(1, len(num)):
        if i % j == 0:
            nums.append(i)


ui = 123456789
c = list(str(ui))
ran = ([int(r) for r in c])
print(ran)

'''
from math import *
class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def all(self):
        if self.b == 0:
            return 'NO bro'
        else:
            return f'{self.a}/{self.b}={self.a / self.b}'
    def all_(self):
        return f'{self.a}*{self.b}={self.a * self.b}'

ravn = Calc(int(input()), int(input()))
ravn.all()
ravn.all_()
print(ravn.all(), ravn.all_())


fun = (lambda x: x*2)
g = fun(12)
print(f'lambda func = {g}')
'''

class Iter:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.third = first
    def __iter__(self):
        return self

    def __next__(self):
        if self.third < self.second:
            val = self.third
            self.third += 1
            return val
        else:
            raise StopIteration

for nub in Iter(1, 20):
    print(nub)


'''
class Ai:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tet(self):
        print(f'Молодец {self.name}')

    def bot(self):
        print(f'Hello {self.name}, I`m Bot. Выбери что хочешь узнать. 1-свой возраст')
        choice = int(input())
        if choice == 1:
            print(f'Тебе сейчас - {self.age}')

name = input("Введите имя: ")
age = int(input("Введите возраст: "))
sea = Ai(name, age)

sea.tet()
sea.bot()
'''



def deco(func):
    def qua(*args, **kwargs):
        # Используем аргументы, переданные в sun
        x, y, z = args
        # Вызываем sun
        func(x, y, z)
        # Увеличиваем значения
        x += 20
        y += 20
        z += 20
        # Возвращаем обновленные значения
        return x, y, z
    return qua

@deco
def sun(x, y, z):
    print(f"больше на 20: x- {x}, y-{y}, z-{z}")


sea = sun(10, 20, 30)
print(sea)



class Car:
    def __init__(self, marka, podmarka):
        self.marka = marka
        self.podmarka = podmarka
    def start(self):
        Japan = ['Honda', 'Toyota']
        if self.marka in Japan:
            return 'From Japan'
        else:
            return 'huina'
    def stop(self):
        if self.podmarka == 'Civic':
            return 'Wooooow'
        else:
            return 'oh'

sea = Car('Honda', 'Civic')
print(f'Машина {sea.start()} начала движение')
print(f'Машина {sea.stop()} закончила движение')


def decorator_1(func):

    def pod(*args, **kwargs):

        x, y = args
        func(x, y)
        if x > 10 or y > 11:

            return f'Ты серьезно ввел {x}, ну даешь!'
        else:
            return 'lox'
    return pod

@decorator_1
def gua (x, y):
    if x == 10 or y == 11:
        print('you are the best')
    else:
        print('lox2')
sea = gua(10 , 10)
print(sea)



class Animal:
    def speak(self):
        print("Звук животного")

class Dog(Animal):
    def speak(self):
        print("Гав!")

class Cat(Animal):
    def speak(self):
        print("Мяу!")

def make_sound(animal):
    animal.speak()  # Полиморфизм: метод speak вызывается для разных типов животных

my_dog = Dog()
my_cat = Cat()
make_sound(my_dog)  # Вывод: Гав!
make_sound(my_cat)  # Вывод: Мяу!



def fibonacci(length):
    lst = [0, 1]
    for item, index in enumerate(range(2, length)):
        lst.append(lst[index-2] + lst[index-1])
    return lst

print(fibonacci(14))

'''
class Shop:

    def __init__(self, SSD, CPU):
        self.SSD = SSD

        self.CPU = CPU
        self.shopping = []

    def addshop(self):

        val = input()
        if val =='add':
            print('что вы хотите добавить?')
            comp = input()
            if comp == self.SSD:
                self.shopping.append(self.SSD)
                print('добавлено', self.shopping)
            if comp == self.CPU:
                self.shopping.append(self.CPU)
                print('добавлено', self.shopping)
            else:
                print('такой товар отсутствует')
        elif val == 'del':
            print('что вы хотите удалить?')
            comp = input()
            if comp == self.SSD:
                self.shopping.remove(self.SSD)
                print('удалено', self.shopping)
            if comp == self.CPU:
                self.shopping.remove(self.CPU)
                print('удалено', self.shopping)
            else:
                print('такой товар отсутствует')


sea = Shop('AMD', 'i7-12400')

sea.addshop()
'''


def decator(func):

    def qua(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()
    return qua
@decator
def sea(text):
    print('text up')
    return text
tea = sea(('okey, let`s go'))
print(tea)






def revert(x):
    pust = []
    y = list(str(x))
    for i in y[::-1]:
        pust.append(i)
    print(*pust)

print(revert((123456789)))



def prostoe(x):

    for i in range(2, x):
        if x % i ==0:
            return False
    return True


for p in [1,3,5,7,12,15,16,19,20,21,32]:
    print(f"{p}: {prostoe(p)}")


def fact(x):
    p = 1
    for i in range(1, x+1):
        p*=i
    return p

print(fact(5))


def palin(x):
    z = int(str(x)[::-1])
    y = int(str(x))
    if z == y:
        return 'palinom'
    else:
        return 'no'

print(palin(1212))

def mnog(x):
    sp = []
    pr = []
    for i in range(1, x+1):
        if x%i == 0:
            sp.append(i)
            for j in range(1, sp[-1]):
                for o in range(1, sp[-1]):
                    if j*o==x:
                        pr.append(j)
                        pr.append(o)

print(mnog(12))

import asyncio


async def f1(x):
    if x > 1:
        return f'{x} > 1'
    else:
        return 'lox'
    await asyncio.sleep(3)
    return 'f1 the end'


async def f2(y):
    if y < 1:
        return f'{y} < 1'
    else:
        return 'lox'
    await asyncio.sleep(3)
    return 'f2 the end'


async def qua():
    task1 = asyncio.create_task(f1(2))
    task2 = asyncio.create_task(f2(4))

    result1 = await task1  # Ожидаем завершения задачи 1
    result2 = await task2  # Ожидаем завершения задачи 2

    return result1, result2


async def main():
    result = await qua()
    print(result)


asyncio.run(main())



def rec(func):
    def su(*args, **kwargs):
        res = func(*args, **kwargs)
        x = int(str(res)[::-1])
        return x
    return su
@rec
def spis(y):
    print(f'{y} reversed -')
    return y
print(spis(1234567890))



import asyncio


# имитация  асинхронного соединения с некой периферией
async def get_conn(host, port):
    class Conn:
        async def put_data(self):
            print('Отправка данных...')
            await asyncio.sleep(2)
            print('Данные отправлены.')

        async def get_data(self):
            print('Получение данных...')
            await asyncio.sleep(2)
            print('Данные получены.')

        async def close(self):
            print('Завершение соединения...')
            await asyncio.sleep(2)
            print('Соединение завершено.')

    print('Устанавливаем соединение...')
    await asyncio.sleep(2)
    print('Соединение установлено.')
    return Conn()


class Connection:
    # этот конструктор будет выполнен в заголовке with
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # этот метод будет неявно выполнен при входе в with
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    # этот метод будет неявно выполнен при выходе из with
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()


async def main():
    async with Connection('localhost', 9001) as conn:
        send_task = asyncio.create_task(conn.put_data())
        receive_task = asyncio.create_task(conn.get_data())

        # операции отправки и получения данных выполняем конкурентно
        await send_task
        await receive_task


asyncio.run(main())