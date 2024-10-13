# Словари и множества

my_dict = {'Igor': 1973, 'Egor': 1998, 'Anastasia': 2000}       #создали словарь
print('Dict: ', my_dict)                                        #распечатали словарь
name1='Egor'
name2='Denis'
print('Год рождения ', name1, '-', my_dict.get(name1))           #вывести год рождения выбранного имени1
print('Год рождения ', name2, '-', my_dict.get(name2), ' - Нет в словаре')  #вывести год рождения выбранного имени2

my_dict.update({'Alsu': 1994, 'Aidar': 1987})                   #добавили в словарь 2 имени
print('Dict: ', my_dict)                                        #распечатали словарь

name_del = 'Igor'
print()
print('Удалаем из словаря: ' + name_del, my_dict.get(name_del))  # удаляем 1 элемент из словаря
del my_dict[name_del]
print('Dict: ', my_dict)                                        #распечатали новый словарь

