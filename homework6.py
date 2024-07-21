# phone_book = {'Max': 46835115, 'Fedor': 1816811,}
# print(phone_book)
# phone_book.update({'Pet': 51651,
#                   'Ivan': 84666348,
#                    'zahar':54861})
# print(phone_book)
# print(phone_book.get('Pet'))
# print(phone_book.get('nasty', 'Нет такого контакта'))

my_dict = {'Vika': 1986, 'Alex':1978}
print(my_dict)

my_dict.update({'Mark': 2016, 'Yroslava':2014})
print(my_dict)
print({'Mark'})

print( my_dict.get('Mark'))
print( my_dict.get('Petr'))

del my_dict['Mark']
print(my_dict)

my_set = {1, 2, 3, 5, 5, 6, 2, 'Яблоко',(3, 2, 7, 9)}
print(my_set)

my_set.update({7, 9})
print(my_set)

my_set.discard(3)
print(my_set)

