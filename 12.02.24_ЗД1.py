# Сколько чисел кратных 5 и какова их сумма?
# Вводим количество чисел в последовательности
N = int(input("Введите количество чисел: "))

# Инициализируем переменные для подсчета
count_5 = 0
sum_5 = 0

# Вводим числа и проверяем, кратны ли они 5
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    if num % 5 == 0:
        count_5 += 1
        sum_5 += num

print(f"Чисел, кратных 5: {count_5}")
print(f"Их сумма: {sum_5}")
