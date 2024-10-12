
class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'white', 'black', 'green']

    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color if color.lower() in Vehicle.__COLOR_VARIANTS else 'unknown'

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность: {self.__engine_power}'

    def get_color(self):
        return f'Цвет:{self._color}'

    def print_info(self):
        print( self.__model )
        print( self.__engine_power )
        print( self.__color )
        print( f'Владелец: {self.owner}' )

    def set_color(self, new_color: str ):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print( f'Нельза сменить цвет на : {new_color}' )


class Sedan( Vehicle ):
    __PASSANGERS_LIMIT_ = 5

     def get_passangers_limit(self):
        return f'Лимит позажиров: {Sedan.__PASSANGERS_LIMIT_}'
        super().__init__( owner, model, engine_power, color )

   
car = Sedan( "Иван", "Toyota Camry", 150, "blue" )
car.print_info()

car.set_color( "green" )
car.print_info()

car.set_color( "yellow" )
car.print_info()
