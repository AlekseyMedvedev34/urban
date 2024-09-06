class House:
    pass
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors
    def go_to (self, new_floors):
        for i in range (1, new_floors+1):
            if new_floors > self.number_of_floors or new_floors < 1:
                print("Такого этажа не существует")
                break
            print(i)
pass


# class House:
#     pass
#     def __init__(self, name, floors):
#         self.name = name
#         self.number_of_floors = floors
#
#         def go_to(new_floor):
#             if new_floor in (1, new_floor):
#             else new_floor > self.number_of_floors or < 1("Такого этажа не существует"):
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(4)
h2.go_to(9)

print()
