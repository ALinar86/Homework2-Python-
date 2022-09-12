# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды)
#  - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)


from datetime import datetime

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

def rand_num(num_1, num_2):
    now = datetime.now()
    const = float(now.strftime('%f')) / 10**6
    if num_1 > num_2:
        delta = num_1 - num_2
        rnd = (const*delta) + num_2
    else:
        delta = num_2 - num_1 
        rnd = (const*delta) + num_1
    print(rnd)


num_1 = int(input('Enter 1 number: '))
num_2 = int(input('Enter 2 number: '))

rand_num(num_1, num_2)
