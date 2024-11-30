Students = input('Введите имена учеников через запятую: ')
Students = Students.replace(' ','').split(',')
Students = sorted(Students)
print()

List_= {}

print('Введите оценки через запятую:')

for item in Students:
    Grades = []
    Average_Grades = []
    Grades += (input(item + " -> ",  )).split(',')
    Average_Grades +=  [round(sum(int(s) for s in Grades if s.isdigit()) / len(Grades),2)]
    List_.update({item: float(s) for s in Average_Grades})

print(List_)







