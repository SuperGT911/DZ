# Сколько чисел, сумма цифр которых чётная?
# Вводим количество чисел в последовательности
N = int(input("Введите количество чисел: "))

# Инициализируем переменную для подсчета
count_even_digit_sum = 0

# Вводим числа и проверяем, четная ли сумма их цифр
for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    
    # Вычисляем сумму цифр числа
    digit_sum = 0
    for digit in str(num):
        digit_sum += int(digit)
    
    if digit_sum % 2 == 0:
        count_even_digit_sum += 1

print(f"Чисел с четной суммой цифр: {count_even_digit_sum}")
