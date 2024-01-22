# Задача №3 и 4. Целочисленное деление.
a, b = map(int, input().split())

b = a // b + b
c = a % b + a

print(c)
