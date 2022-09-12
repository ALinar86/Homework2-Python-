# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений
# (набор - это список) чисел от 1 до N. Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def check_num():
    try:
        num = int(input("Enter number: "))
        return num
    except ValueError:
        print('Error')
        return check_num()


def factor():
    number = check_num()
    if number < 0:
        print('Error')
    else:
        list_factorial = []
        factor = 1
        for i in range(2, number+2):
            list_factorial.append(factor)
            factor *= i
        print(list_factorial)


factor()
