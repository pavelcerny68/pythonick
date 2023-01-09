# Zadejte dvě celá čísla x a y. Zjistěte, zda číslo x je beze zbytku dělitelné číslem y

x = int(input("Zadej první číslo: "))
y = int(input("Zadej druhé číslo: "))

if x // y:
    print("x", x, "//", y, "Je beze zbytku dělitelné")
else:
    print("x", x, "// y", y, "Je dělitelné se zbytkem", x % y)
