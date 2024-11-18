my_dict = {'Alina':2000, 'Max': 2001, 'Polina': 1998}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alina'])
print('Not existing value: ', my_dict.get('Alex'))
my_dict.update({'Gleb':2008, 'Nikita':2005})
a = my_dict.pop('Max')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

print('')

my_set = {1, 3, 6, 2, 2 ,6 ,4 ,5, 'apple', 3.14, 'apple'}
print('Set: ',my_set)
my_set.update(['cat',5.6])
my_set.remove(2)
print('Modified set:', my_set)

