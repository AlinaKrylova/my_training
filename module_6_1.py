class Animal: # родительский класс
    alive = True # живой
    fed = False # накормленный
    def __init__(self,name):
        self.name = name

class Plant:# родительский класс
    edible = False  # съедобность
    def __init__(self,name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food,Flower) or isinstance(food, Fruit):
            Animal.fed = True
            print(f"{self.name} съел {food.name}")

class Predator(Animal):# хищники
    def eat(self, food):
        if isinstance(food,Flower) or isinstance(food, Fruit):
            Animal.alive = False
            print(f"{self.name} не стал есть {food.name}")

class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)