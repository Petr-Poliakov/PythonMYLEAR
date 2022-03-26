# #Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
# for x in range(0,2):
#     for y in range(0,2):
#         if not(x or y) == ((not x) and (not y)):
#             print(f'При X = {x}  Y = {y}    Истинно')
#         else:
#             print(f'При X = {x}  Y = {y}    Ложь')

#Задать номер четверти, показать диапазоны для возможных координат
# coord = ['X>0 ; Y>0', 'X<0 ; Y>0', 'X<0 ; Y<0', 'X>0 ; Y<0']
# quarter = int(input('Введите номер четверти  '))
# if 0<quarter<5:
#     print(coord[quarter - 1])
# else:
#     print('Шутник!')

#Найти расстояние между точками в пространстве 2D/3D
# print('Введите координаты точек (X1;Y1;Z1) и (X2;Y2;Z2)')
# x1 = float(input('X1 = '))
# y1 = float(input('Y1 = '))
# z1 = float(input('Z1 = '))
# x2 = float(input('X2 = '))
# y2 = float(input('Y2 = '))
# z2 = float(input('Z2 = '))
# dx = x2 - x1
# dy = y2 - y1
# dz = z2 - z1
# print(f'Расстояние между точками равно {round((dx**2 + dy**2 + dz**2)**0.5, 2)}')

#Найти кубы чисел от 1 до N
# n = 5
# for i in range (1,n+1):
#     n=n**3


#26 Возведите число А в натуральную степень B используя цикл
a = 2 #int (input())
b = 5 #int (input())
result = a
for i in range(1,b+1):
    result=a**i
    # result=result*a
    print(result)
    print(i)




#28 Подсчитать сумму цифр в числе
# a = int (input())
# sum=0
# while a>=1:
#     sum = sum + a%10
#     a=a//10
#     #print(a)
# print(sum)

#30 Показать кубы чисел, заканчивающихся на четную цифру и не 
