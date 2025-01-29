def all_variants(text):
    for length in range(1, len(text) + 1):  # Перебор длин последовательностей
        for start in range(len(text) - length + 1):  # Перебор начальных позиций
            substring = text[start:start + length]  # Извлечение подстроки
            yield substring

# Вывод всех последовательностей
a = all_variants("abc")

for i in a:
    print(i)
