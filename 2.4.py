import random
#  красный-1; синий-2; желтый-3")
z1 = random.randint(1,4)
z2 = random.randint(1,4)
if z1 == z2:
    print("Смешиваются два одинаковых цвета")
elif (z1 == 1 and z2 == 2) or (z2 == 1 and z1 == 2):
    print("Красный+синий=фиолетовый")
elif (z1 == 1 and z2 == 3) or (z2 == 1 and z1 == 3):
    print("Красный+желтый=оранжевый")
elif (z1 == 3 and z2 == 2) or (z2 == 3 and z1 == 2):
    print("Желтый+синий=зеленый")
else:
    print("Ошибка: такого цвета нет")
print(z1, z2)