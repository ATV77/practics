k = int(input("Введите k: "))
m = int(input("Введите m: "))
n = int(input("Введите n: "))

for x in range(100):
    if x % 3 == k and x % 5 == m and x % 7 == n:
        print(f"Задуманное число: {x}")
        break
else:
    print("Число не найдено.")