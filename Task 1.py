# Составить алгоритм: если введенное число больше 7, то вывести "Привет"

d = int(input('Введите число: '))

while d <= 7:
    print('Введите число больше семи')
    d = int(input('Введите число: '))
else:
    print('Привет')
