class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self._vin__ = vin
        self._numbers__ = numbers
        self.__is_valid_nambers(vin)
        self.__is_valid_numbers( numbers )


    @staticmethod
    def __is_valid_numbers(vin):
        if isinstance(vin, int):
            raise IncorrectVinNumber('Не корректный номер VIN')
        if not 1000000 < vin < 9999999:
            return True


    @staticmethod
    def __is_valid_nambers(numbers):
        if isinstance(numbers, int):
            raise IncorrectVinNumber('Не корректный номер ')
        if len(numbers) == 6:
            raise IncorrectVinNumber(' Не вернеый деапазон для VIN')
        return True




try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')