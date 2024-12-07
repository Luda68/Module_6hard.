"""Задание "Они все так похожи":
Давайте попробуем реализовать простейшие классы для некоторых таких фигур и при
этом применить наследование (в будущем, изучая сторонние библиотеки, вы будете
замечать схожие классы, уже написанные кем-то ранее):
Общее ТЗ:
Реализовать классы Figure(родительский), Circle, Triangle и Cube, объекты которых
будут обладать методами изменения размеров, цвета и т.д.
Многие атрибуты и методы должны быть инкапсулированны и для них должны быть написаны
интерфейсы взаимодействия (методы) - геттеры и сеттеры.
Подробное ТЗ:
Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список
цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет
корректность переданных значений перед установкой нового цвета. Корректным цвет:
все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на
соответствующие значения, предварительно проверив их на корректность. Если введены
некорректные данные, то цвет остаётся прежним.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает
True если все стороны целые положительные числа и кол-во новых сторон совпадает с
текущим, False - во всех остальных случаях.
Метод get_sides должен возвращать значение я атрибута __sides.
Метод __len__ должен возвращать периметр фигуры.
Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество
не равно sides_count, то не изменять, в противном случае - менять.
Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и
через радиус).
Атрибуты класса Triangle: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
Атрибуты класса Cube: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.
ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон
не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое
требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его
стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его
стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны
будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его
стороны будут - [1, 1, 1, ....., 1]
"""


class Figure:
    __sides = []
    __color = []
    filled = False  # изначально незакрашена

    def __init__(self, rgb, *side):  # палитра и стороны
        self.color = list(rgb)
        self.side = side[0]  # берём только первое значение
        self.filled = True  # принята палитра (rgb), фигура закрашена

    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color

    def _is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self.color = [self.r, self.g, self.b]

    def __is_valid_sides(self, *args):
        for side in self.sides:
            if len(self.sides) == self.sides_count and side > 0 and type(side) == int:
                return True
            else:
                return False

    def set_sides(self, *args):
        massive_lst = []
        self.sides = list(args)
        if self.__is_valid_sides(self, *args):
            self.get_sides()
        else:
            for i in range(self.sides_count):
                massive_lst.append(self.side)  # если делать как указано в примере выполнения задания (вывод на консоль)
                # massive_lst.append(1)       # если делать как в ТЗ, где выводится массив из 1 числом в кол-во сторон
            self.sides = massive_lst
            self.get_sides()

    def get_sides(self):
        self.__sides = self.sides
        return self.__sides

    def __len__(self):
        return self.side * self.sides_count


class Circle(Figure):
    sides_count = 1
    __radius = None

    def set_radius(self):
        self.__radius = self.__len__() / (2 * 3.141569)
        return self.__radius

    def get_square(self):
        self.set_radius()
        return (self.__radius ** 2) * 3.141569  # как в школе через радиус
        # return ((self.side)**2)/(4 * 3.141569) # через длину окружности


class Triangle(Figure):
    sides_count = 3
    __height = None

    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

    def set_height(self):
        self.__height = self.side * (3 ** 0.5) / 2
        return self.__height


class Cube(Figure):
    sides_count = 12

    def set_side_lst(self):
        set_side_lst = []
        for element in range(self.sides_count):
            set_side_lst.append(self.side)
        self.__sides = set_side_lst
        return self.__sides

    def get_volume(self):
        return self.side ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
triangle1 = Triangle((200, 200, 100), 10, 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# print(cube1.set_side_lst())
# print(triangle1.get_square())
# print(circle1.get_square())
# print(triangle1.set_height())
# print(cube1.set_side_lst())

