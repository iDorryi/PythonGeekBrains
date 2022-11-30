import random
first_list = [random.randint(0,10) for i in range(5)]
print("Рандомный список :{}".format(first_list))
random.shuffle(first_list)
print("Перемешанный список: {}".format(first_list))

# mass = list(map(int,input().split()))
# print("Рандомный список :{}".format(mass))
# random.shuffle(mass)
# print("Перемешанный список: {}".format(mass))

