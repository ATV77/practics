import math
x = int(input("Введите x: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))

num1 = ((x + 2) / (b - 3)) - (1 / (c**3 - 2))
num2 = (x + b**2 + 3 * c)/(2 - 5 * x * b)
k= abs(num1) + num2
print("k =",k)