import random
k = 0
p = 0
while k != 3:
    ch1 = random.randint(0,100)
    ch2 = random.randint(0, 100)
    rez = ch1 + ch2
    otvet = input(str(ch1) + "+" + str(ch2) + "=")
    if rez == int(otvet):
        print("Правильно!")
        p += 1
    else:
        print("Ответ неверный")
        k += 1
print("Игра окончена. Правильных ответов: ", p)