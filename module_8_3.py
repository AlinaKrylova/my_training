class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__(message)

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)

class Car:
    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model

        # Проверка VIN перед присваиванием
        self.__is_valid_vin(vin)
        self.__vin = vin

        # Проверка номеров перед присваиванием
        self.__is_valid_numbers(numbers)
        self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        """ Проверяет, является ли VIN-номер корректным и выбрасывает исключение при ошибке """
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип VIN-номера')
        if not (1000000 <= vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для VIN-номера')

    def __is_valid_numbers(self, numbers):
        """ Проверяет, является ли номерной знак корректным и выбрасывает исключение при ошибке """
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

# Тестирование
cars = [
    ("Model1", 1000000, "f123dj"),  # Должен создаться успешно
    ("Model2", 300, "т001тр"),  # Ошибка VIN
    ("Model3", 2020202, "нет номера")  # Ошибка номера
]

for model, vin, numbers in cars:
    try:
        car = Car(model, vin, numbers)
        print(f"{car.model} успешно создан")
    except (IncorrectVinNumber, IncorrectCarNumbers) as exc:
        print(f"Ошибка при создании {model}: {exc}")
