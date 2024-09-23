class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

class Plant:
    edibel = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food

        if food.edibel:
            fed = True
            return f'{self.name} съел {food.name}.'
        else:
            alive = False
            return f'{self.name} не стал есть.'
        



class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    pass


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