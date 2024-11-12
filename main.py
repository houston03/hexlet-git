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
