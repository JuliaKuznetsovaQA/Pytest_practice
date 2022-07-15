a = int(input("Введите число: "))
b = int(input("Введите второе число: "))

sum = a + b
print("Сумма чисел равна: " + str(sum))

sub = a - b
print("Разность чисел равна: " + str(sub))

mult = a * b
print("Произведение чисел равно: " + str(mult))

try:
    division = int(a / b)
except ZeroDivisionError:
    division = 0
    print("На ноль делить нельзя")
print("Результат деления чисел: " + str(division))