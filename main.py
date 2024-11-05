import random
values = [-15, -4, -2, -7, 0, 3, 5, 12, 7]
height = int(input("Введи высоту матрицы:"))
width = int(input("Введи длину матрицы:"))
#Проверка высоты
if height>8 or height<4:
    print("Неправильный размер матрицы")
#Проверка длины  
if width>8 or width<4:
    print("Неправильный размер матрицы")
#Составление матрицы
matrix =[[random.choice(values) for i in range(width)] for k in range(height)] 
for arr in matrix:
    for num in arr:
        print(num,end=" ")
    print()
sum = 0
for i in matrix:
    for k in i:
        if k%2!=0:
         sum+=k
print("Сумма нечетных чисел: ",sum)