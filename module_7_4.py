def number_of_participants(a):

    if a % 10 == 1 and a % 100 != 11:
        return "%s участник" % a
    elif 2 <= a % 10 <= 4 and (a % 100 < 10 or a % 100 > 20):
        return "%s участника" % a
    else:
        return "%s участников" % a

def number_of_tasks(a):

    if a % 10 == 1 and a % 100 != 11:
        return "{} задача".format(a)
    elif 2 <= a % 10 <= 4 and (a % 100 < 10 or a % 100 > 20):
        return "{} задачи".format(a)
    else:
        return "{} задач".format(a)

def f(a):

    if a % 10 == 1 and a % 100 != 11:
       return f"{a} задача"
    elif 2 <= a % 10 <= 4 and (a % 100 < 10 or a % 100 > 20):
        return f"{a} задачи"
    else:
        return f"{a} задач"

def champion(num_a, num_b, time_a, time_b, a, b):

    if num_a > num_b or (num_a == num_b and time_a < time_b):
        return f"Сегодня победила команда {a}"
    elif num_a < num_b or (num_a == num_b and time_a > time_b):
        return f"Сегодня победила команда {b}"
    else:
        return "Сегодня ничья"

def time(t):

    if t % 10 == 1 and t % 100 != 11:
        t_str =  f"{t} секунда"
    elif 2 <= t % 10 <= 4 and (t % 100 < 10 or t % 100 > 20):
        t_str = f"{t} секунды"
    else:
        t_str = f"{t} секунд"

    return t_str

team1_num = 5
team2_num = 6
team1 = 'Мастера кода'
team2 = 'Волшебники данных'
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

print('Сегодня в команде ' + team1 + ' %s' % number_of_participants(team1_num))
print('Сегодня в команде ' + team2 + ' %s' % number_of_participants(team2_num))
print('Итого сегодня в командах %s' % number_of_participants(team1_num + team2_num))
print('------------------------------------------------')
print('Команда ' + team1 + ' решила {}'.format(number_of_tasks(score_1)))
print('Команда ' + team2 + ' решила {}'.format(number_of_tasks(score_2)))
print(f'Обе команды решили {f(score_1 + score_2)}')
print('------------------------------------------------')
print(champion(score_1, score_2, team1_time, team2_time, team1, team2))
print('------------------------------------------------')
print('Команда ' + team1 + 'решила задачи за ' + time(team1_time))
print('Команда ' + team2 + 'решила задачи за ' + time(team2_time))
print('Сегодня было решено ' + number_of_tasks(score_1 + score_2) +
      ' в среднем за ' + time((team1_time + team2_time) / (score_1 + score_2)))