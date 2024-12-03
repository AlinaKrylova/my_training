def password(n):

    password_ =[]

    for i in range (1, n+1):
        for j in range (1, n+1):
            if i !=j and n % (i + j) == 0:
                a = int(str(i) + '0' * len(str(j)))+ j
                password_.append(a)
                for item in password_:
                    if item == int(str(a)[::-1]):
                        password_.remove(a)

    return password_

b = int(input('Введите число ( 3 .. 20 ) : '))

print('Пароль: ',*password(b), sep="" )
