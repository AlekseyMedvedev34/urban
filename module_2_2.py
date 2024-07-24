first = int(input('Ввидите число 1: '))
second = int(input('Введите число 2: '))
third = int(input('Введите число 3: '))
print()

if first == second == third:
    print(3)
# Если все числа равны между собой, то вывести 3

elif first == second or first == third:
    print(2)
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2


else:
    print(0)
 # Если равных чисел среди 3-х вообще нет, то вывести 0



# first = [123]
# second = [456]
# third = [789]
# print([])
#
# int =  1, 2 , 3
