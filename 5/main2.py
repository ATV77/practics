import math
p = int(input("Введите p: "))
q = int(input("Введите q: "))

a = [i for i in range(1, q + 1) if q % i == 0]

b = [d for d in a if math.gcd(d, p) == 1]

print(f"Делители числа {q}, взаимно простые с {p}: {b}")