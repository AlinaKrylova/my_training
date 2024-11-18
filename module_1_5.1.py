immutable_var = (1, [2,3], "String", True)
print(immutable_var)

mutable_list = ['a','b','c']
print(mutable_list)
mutable_list.append('d')
print(mutable_list)
mutable_list.extend(['apple','1','2'])
print(mutable_list)
mutable_list.remove('a')
print(mutable_list)
