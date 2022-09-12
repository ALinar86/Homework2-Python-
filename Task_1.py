# 1 - Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

def real_num():
    try:
        num = float(input("Enter real number: "))
        return num
    except ValueError:
        print('Error')
        return real_num()


def find_sum():
    num = real_num()
    if num < 0:
        num = abs(float(num))
    sum = 0
    num_str = str(num)
    num_list = list(num_str)
    for i in num_list:
        if i != ".":
            sum += int(i)
    print(sum)


find_sum()
