# 4'. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2 
# Позиции: 0,1 -> 2
# f = open('file.txt','w')
with open('file.txt','r') as f:
    positions = f.read().split('\n')
positions = list(map(int, positions))
n = int(input("Введите число: "))
mult = 1
list_new = []
for i in range(-n,n+1):
    list_new.append(i)
# list_new = [i for i in range(-n,n+1) ]

for pos in positions:
    mult *= list_new[pos]
print("Позиции из файла: {}".format(positions))
print("Сгенерированный список: {}".format(list_new))
print("Произведение цифр с указанных в файле позиций: {}".format(mult))

# Для позиций введенных с клавиатуры:
# n = int(input("Введите число: "))
# position1 = int(input("Введите первую позицию: "))
# position2 = int(input("Введите вторуб позицию: "))
# mult = 1
# list_new = [i for i in range(-n,n+1) ]
# for i in list_new:
#     mult = list_new[position1] * list_new[position2]
# print(position1, position2)
# print(list_new)
# print(mult)

# Для позиций введенных с клавиатуры через мэп:
# n = int(input("Введите число: "))
# positions = list(map(int, input().split()))
# mult = 1
# list_new = [i for i in range(-n,n+1) ]
# for pos in positions:
#     mult *= list_new[pos]
# print(positions)
# print(list_new)
# print(mult)