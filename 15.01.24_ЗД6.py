# Задача №6 Целочисленное деление.
a, b = map(int, input().split())

c = a // b 
d = a % b

# Выводим результат в нужном формате
print(f"{a}//{b}={c}") # f-строка позволяет подставлять значения переменных внутри фигурных скобок
print(f"{a}%{b}={d}")
