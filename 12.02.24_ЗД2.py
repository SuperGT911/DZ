# Сколько чисел оканчивается на 4?
# Вводим количество чисел в последовательности
N = int(input("Введите количество чисел: "))

# Инициализируем переменную для подсчета
count_ending_4 = 0

# Вводим числа и проверяем, оканчиваются ли они на 4
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    if num % 10 == 4:
        count_ending_4 += 1

print(f"Чисел, оканчивающихся на 4: {count_ending_4}")
