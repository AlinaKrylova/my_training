summa = []
sum_ = 0

def a(*args):

	global summa, sum_
	new = []

	for item in args:
		for i in item:
			if isinstance(i,list):
				new.extend(i)
			elif isinstance(i,dict):
				new.extend(i.items())
			elif isinstance(i,set):
				new.extend(i)
			elif isinstance(i,tuple):
				new.extend(element for element in i)
			elif isinstance(i,str):
				new.extend([len(i)])
			elif isinstance(i, int):
				summa.append(i)
			else:
				summa.append(0)
		if all(isinstance(i,int) for i in item):
			sum_ = sum(summa)
		else:
			return a(new)
	return sum_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(a(data_structure))