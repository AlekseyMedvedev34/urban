# food = ['apple','banana','coconut']
# food.append(True)
# print(food)
# food.extend(['string',2])
# print(food)
# print(food)
# print('coconut' not in food)
# print(food[0:2:2])


immutable_var = 2, 'food', 3, 5
print( immutable_var, type( immutable_var ) )
immutable_var = 1, 2,'food', 3, 4 # кортеж не изменяемы структура данных.Так же как списки они могут
# состоять из элементов разных типов, перечисленных через запятую.Кортежи заключаются в круглые, а не квадратные скобки.
print( immutable_var )

mutable_list = [1,'cola',5,'apple']
print(mutable_list)
mutable_list[0] = 9
print(mutable_list)


