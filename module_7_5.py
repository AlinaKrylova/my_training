import os
import time

# Указываем директорию, которую будем обходить
print('Текущая директория: ', os.getcwd())
directory = "/Users/alinaabbosova/Desktop/PP/Module 7/m7p5"

# Используем os.walk для обхода каталога
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)

        # Форматируем время для удобного отображения
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        print(
            f'Обнаружен файл: {file}\n'
            f'Путь: {filepath}\n'
            f'Размер: {filesize}'' байт\n'
            f'Время изменения: {formatted_time}, '
            f'Родительская директория: {parent_dir}')