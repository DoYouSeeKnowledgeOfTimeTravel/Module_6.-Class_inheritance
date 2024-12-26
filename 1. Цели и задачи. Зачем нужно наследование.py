class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False



class Mammal(Animal):
    pass

class Predator(Animal):
    pass



class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


predator = Predator('Волк с Уолл-Стрит')
mammal = Mammal('Хатико')
flower = Flower('Цветик семицветик')
fruit = Fruit('Заводной апельсин')

print(predator.name)
print(flower.name)

print(predator.alive)
print(mammal.fed)

predator.eat(flower)
mammal.eat(fruit)

print(predator.alive)
print(mammal.fed)

