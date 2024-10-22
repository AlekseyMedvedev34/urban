class Animal:
    alive = True
    fed = False
    def eat(self, food):
        if isinstance( food, Plant ):
            if food.edible:
                print( f'{self.name} съел {food.name}' )
                self.fed = True
            else:
                print( f'{self.name} не стал есть  {food.name}' )
                self.alive = False

        else:
            print( f"{self.name} не может есть это!" )


    def __init__(self, name):
        self.name = name


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Mammal( Animal ):
    def __init__(self, name):
        super().__init__( name )


class Predator( Animal ):
    def __init__(self, name):
        super().__init__( name )


class Flower( Plant ):
    def __init__(self, name):
        super().__init__( name )


class Fruit( Plant ):
    def __init__(self, name):
        super().__init__( name )


mammal = Mammal( "Кролик" )
predator = Predator( "Лев" )

flower = Flower( "Роза" )
fruit = Fruit( "Яблоко" )

mammal.eat( fruit )
predator.eat( flower )
predator.eat( fruit )
