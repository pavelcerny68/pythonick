a = []
n = int(input("Zadej počet čísel: "))

for i in range(1, n + 1):
    b = int(input("Vlož číslo: "))
    a.append(b)
a.sort()
print("Největší číslo je: ", a[n - 1])
print("Druhé nejvěší číslo je: ", a[n - 2])
