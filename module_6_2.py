class Vehicle:

    def __init__(self, owner: str,  __model: str, __engine_power: int, __color: str ):
        self.owner = owner # Владелец транспорта.(владелец может меняться)
        self.__model = __model # Модель (марка) транспорта.(мы не можем менять название модели)
        self.__engine_power = __engine_power # Мощность двигателя.(мы не можем менять мощность двигателя самостоятельно)
        self.__color = __color # Название цвета.(мы не можем менять цвет автомобиля своими руками)

    __COLOR_VARIANTS = 'Black, Red, White, Yellow, Purple, Green, Blue'

    def get_model(self):
        print(f"Модель: {self.__model}")

    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        print(f"Цвет: {self.__color}")

    def print_info(self):
        self.get_model(), self.get_horsepower(), self.get_color()
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS.lower():
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()

