import math

class Figure:
    sides_count = 0

    def __init__(self, __color: list, *sides: int):
        self.__sides = self._initialize_sides(*sides)
        self.__color = __color
        self.filled = False

    def _initialize_sides(self, *sides):
        if len(sides) != self.sides_count:
            # Если передано одно значение, заполняем его для всех сторон
            if len(sides) == 1:
                return [sides[0]] * self.sides_count
            else:
                return [1] * self.sides_count  # Если сторон меньше или их количество больше, возвращаем 1
        elif all(isinstance(side, int) and side > 0 for side in sides):
            return list(sides)  # Возвращаем переданные корректные стороны
        else:
            return [1] * self.sides_count  # Если есть некорректные стороны, возвращаем 1

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        def is_valid(num):
            return isinstance(num, int) and 0 <= num <= 255

        return is_valid(r) and is_valid(g) and is_valid(b)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        return len(args) == self.sides_count and all(isinstance(item, int) and item > 0 for item in args)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color: list, *sides):
        super().__init__(__color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color: list, *sides):
        super().__init__(__color, *sides)

    def get_square(self):
        a, b, c = self.__sides
        p = sum(self.__sides) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return S


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color: list, *sides):
        super().__init__(__color, *sides)

        # Если передано одно значение, создаем 12 одинаковых сторон
        if len(self.get_sides()) == 1:
            self.__sides = [self.get_sides()[0]] * self.sides_count
        # Если передано 12 значений, устанавливаем их
        elif len(self.get_sides()) == self.sides_count:
            self.__sides = self.get_sides()

    def get_volume(self):
        return self.get_sides()[0] ** 3

# Примеры создания объектов
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)  # Передаем одно значение для ребра куба

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
