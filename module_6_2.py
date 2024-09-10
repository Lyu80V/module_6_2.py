class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'grey', 'black', 'white']
    def __init__(self,  __model,  __engine_power, __color, owner):
        self.__model =__model
        self.__engine_power = __engine_power
        self.__color = __color
        self.owner = owner


    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self.__COLOR_VARIANTS:
           self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def get_limit(self):
        return self.__PASSENGERS_LIMIT


m1 = Sedan('Fedor', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
m1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
m1.set_color('Pink')
m1.set_color('BLACK')
m1.owner = 'Alexandr'

# Проверяем что поменялось
m1.print_info()

print(m1.get_limit())
