# Заполнение массива случайными вещественными значениями от 0 до 1
import random

real_numbers_list = []

for _ in range(15):
    random_value = random.uniform(0, 1)
    real_numbers_list.append(random_value)

print("Список вещественных чисел от 0 до 1:")
for value in real_numbers_list:
    print(value)
