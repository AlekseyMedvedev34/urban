


def divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return first/second
        first = int( input( 'Ввидите число 1: ' ) )
        second = int( input( 'Введите число 2: ' ) )

# math.nextafter( x, math.inf )

print(divide(69, 3))
print(divide(3, 0))

