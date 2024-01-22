# Задача №5 Пирожки | Целочисленное деление.
a, b, n = map(int, input().split())

total = (a * 100 + b) * n
rub = total // 100 # целая часть - рубли
kop = total % 100 # остаток - копейки

print(f"{rub}rub. {kop}kop.")
