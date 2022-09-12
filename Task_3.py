# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково,
# но есть одно "но". Если перевернутое число не равно исходному, то они складываются и проверяются
#  на палиндром еще раз. Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.


def check_num():
    try:
        num = int(input("Enter number: "))
        return num
    except ValueError:
        print('Error')
        return check_num()


def palindrom():
    count = 0
    num = check_num()
    if num < 0:
        print('Error')
    else:
        while True:
            num = str(num)
            revers_num = num[::-1]
            if int(num) == int(revers_num):
                print(f'Number {num} is palindrome')
                break
            else:
                num = int(num) + int(revers_num)
                count += 1
        print(f'The number of palindromes after {count} iterations')


palindrom()
