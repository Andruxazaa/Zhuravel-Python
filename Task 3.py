# Составить алгоритм: на входе есть числовой массив,
# необходимо вывести элементы массива кратные 3

massive = [i for i in range(int(input()))]
print(*[i for i in massive if i % 3 == 0])
