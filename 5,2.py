class House:
    pass
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors
    # def go_to (self, new_floors):
    #     for i in range (1, new_floors+1):
    #         if new_floors > self.number_of_floors or new_floors < 1:
    #             print("Такого этажа не существует")
    #             break
    #         print(i)

    def __len__(self):
        return  self.number_of_floors


    def __str__( self):
        return  f"Название: {self.name}, количество этажей: {self.number_of_floors}"


pass
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# h1.go_to(4)
# h2.go_to(9)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
