# Заполнение массива случайными вещественными значениями (как я понял) от 22 до 23?
import random

custom_range_list = []

for _ in range(15):
    random_value = random.uniform(22, 23)
    custom_range_list.append(random_value)

print("Список вещественных чисел в диапазоне от 22 до 23:")
for value in custom_range_list:
    print(value)
