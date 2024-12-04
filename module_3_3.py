def print_params(a = 1, b = 'строка', c = True):
   print(a, b, c)

print_params()
print_params('Август')
print_params(10,2)
print_params(c = 16)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [[1, 2], (4,5,6), 'A']
values_dict = {'a':'A', 'b':1, 'c':('B',4)}

print_params(values_list)
print_params(*values_list)
print_params(**values_dict)
print_params(values_dict)
print_params(*values_list[0:2], values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)







