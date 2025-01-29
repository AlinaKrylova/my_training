# Lambda-функция
first = 'Мама мыла раму'
second = 'Рамена мало было'

func = list(map(lambda i,w: i == w, first, second))
print(func)

# Замыкание
import json

def get_advanced_writer(file_name):

    def write_everything(*data_set):

        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(', '.join(json.dumps(data, ensure_ascii=False) for data in data_set))

    return write_everything  # Возвращаем функцию, а не вызываем ее

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__
import random

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())