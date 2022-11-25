#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#в которой находится эта точка (или на какой оси она находится).
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

coordinates_X = int (input('Введите координаты точки X '))
coordinates_Y = int (input('Введите координаты точки Y '))
if coordinates_X > 0 and coordinates_Y > 0 :
    print('Точка находится в 1-й четверти')
elif coordinates_X < 0 and coordinates_Y > 0:
    print('Точка находится во 2-й четверти')
elif coordinates_X < 0 and coordinates_Y < 0:
    print('Точка находится в 3-й четверти')
elif coordinates_X > 0 and coordinates_Y < 0:
    print('Точка находится в 4-й четверти')
else:
    print('Некорректно заданы координаты')   