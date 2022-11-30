# 3.Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

# numbers = []  
# n = int(input("Введите число:"))
# sum = 0
# for i in range(n):  
#     new_element = (1+1/n)**n
#     n-=1
#     numbers.append(new_element)
#     sum = sum + new_element
# print(f"Список для последовательности элементов: {numbers};")
# print(f"Сумма элементов: {sum}.")


numbers = []  
n = int(input("Введите число: "))
sum = 0
for i in range(1, n+1):  
    new_element = (1+1/i)**i
    numbers.append(new_element)
    sum = sum + new_element
print(f"Список из последовательности элементов: {numbers};")
print(f"Сумма элементов: {sum}.")


# n = int(input('Number:'))
# sequence = [(1+1/i)**i for i in range (1,n+1)]
# print(f"The listed sequence : {sequence}")
# print(f"Sum of all elements of the sequence: {sum(sequence)}")



