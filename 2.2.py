m = int(input("Введите номер места от 1 до 54 "))
if m in range(1,37):
    bn = "Небоковое"
    if m % 2 == 0:
        vn = "Верхнее"
    else:
        vn = "Нижнее"
    print("Номер места: ", m, vn, bn )
elif m in range(36,55):
    bn = "Боковое"
    if m % 2 == 0:
        vn = "Верхнее"
    else:
        vn = "Нижнее"
    print("Номер места: ", m, vn, bn)
else:
    print("Номер введен некорректно")
