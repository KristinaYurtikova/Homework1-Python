#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

coordinates_XA = float(input('Введите координаты X точки A: '))
coordinates_YA = float(input('Введите координаты Y точки A: '))
coordinates_XB = float(input('Введите координаты X точки B: '))
coordinates_YB = float(input('Введите координаты Y точки B: '))
distance = round(((coordinates_XA - coordinates_XB)**2 + (coordinates_YA - coordinates_YB)**2)**0.5 ,2)
print(f'Расстояние от точки A до точки B = {distance}')