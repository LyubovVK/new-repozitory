#Задача "Все ли равны?":

print('Необходимо ввести 3 числа для сравнения')
print()
print('Вы хотите ввести числа для проверки самостоятельно? или воспользоваться предопределенным набором?')
i=int(input('Введите 1 - если самостоятельно, или 0 - если предопределенный набор: '))
if i == 1:
    print('Необходимо ввести 3 числа через пробел: ')
    first, second,  third = map(int, input().split())
else:
    first = 98
    second = 55
    third = 98
print()
print('Имеется набор чисел: ', first, second, third)
print()
print('Результат сравнения чисел')
if first == second and second == third:
    print(3, '.Все числа равны.')
elif first == second or second == third or first == third:
    print(2, '.Два из трех чисел равны.')
else:
    print(0,'.Нет одинаковых чисел.')