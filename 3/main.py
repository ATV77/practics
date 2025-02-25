import math
a = int(input("введите a: "))
b = int(input("введите b: "))
c = int(input("введите c: "))

if (a + b > c and b + c > a and c + a > b):
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p -c))
    print("Площадь треугольника: ", s)
else:
    s = "Стороны не подходят"
    print(s)