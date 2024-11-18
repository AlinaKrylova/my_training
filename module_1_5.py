example = 'Топинамбур'
print(example[0])
print(example[-1])

a = example
k=0
while a != '':
    i = 1
    n = -1
    a = a[i-1:n]
    k +=1

print(example[k//2:])
print(example[::-1])
print(example[1::2])