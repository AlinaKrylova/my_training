first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(i) - len(w) for i, w in zip(first, second) if len(i) != len(w)]
second_result = [len(first[i]) == len(second[i]) for i in range(0, len(first))]

print(first_result)
print(second_result)
