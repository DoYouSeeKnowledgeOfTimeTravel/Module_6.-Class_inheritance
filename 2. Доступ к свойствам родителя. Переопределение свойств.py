class Vehicle:
    __COLOR_VARIANTS = ['Жёлтый', 'Серебряный', 'Чёрный', 'Белый', 'Зелёный']
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color
    def get_model(self, __model):
        return f'Модель: {self.__model}'
    def get_horsepower(self, __engine_power):
        return f'Мощность двигателя: {self.__engine_power}'
    def get_color(self, __color):
        return f'Цвет: {self.__color}'
    def print_info(self):
        print(self.get_model(self))
        print(self.get_horsepower(self))
        print(self.get_color(self))
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        new_color_lower = new_color.lower()
        if new_color_lower not in map(str.lower, self.__COLOR_VARIANTS):
            print(f'Нельзя сменить цвет на {new_color}')
        else:
            self.__color = new_color

        #for color in self.__COLOR_VARIANTS:
        #    if new_color.lower() in color.lower():
        #        print(f'Нельзя сменить цвет на {new_color}')
        #self.__color = new_color

        # new_color_lower = new_color.lower()
        # for color in self.__COLOR_VARIANTS:
        #    if new_color_lower == color.lower():
        #        self.__color = color
        #        break
        # else:
        #    print(f'Нельзя сменить цвет на {new_color}')

             # print(f'Нельзя сменить цвет на {new_color}')

# Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS,
# в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['Жёлтый', 'Серебряный', 'Чёрный', 'Белый', 'Зелёный']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'Серебряный', 500)
vehicle1.print_info()

vehicle1.set_color('Синий')
vehicle1.set_color('ЧЁРНЫЙ')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()