# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

print ('Введите координаты (X, Y) точки \n X =')
x = int(input())
print ('Y =')
y = int(input())
if x == 0 and y == 0: print('Точки находится в центре координатной плоскости')
elif x == 0: print('Точка находится на оси Х')
elif y == 0: print('Точка находится на оси Y')
elif x>0 and y>0: print ('Точка находится в 1 четверти')
elif x>0 and y<0: print ('Точка находится в 2 четверти')
elif x<0 and y<0: print ('Точка находится в 3 четверти')
elif x>0 and y<0: print ('Точка находится в 4 четверти')