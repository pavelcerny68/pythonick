# Určete, zda dvě zadaná čísla x,y čísla splňují nerovnost x+3<5y-1
x = int(input("Zadej první číslo: "))
y = int(input("Zadej druhé číslo: "))

rovnice_x = x + 3
rovnice_y = (5 * y) - 1

if rovnice_x == rovnice_y:
    print(rovnice_x, "a", rovnice_y, "splňují rovnost")
else:
    print(rovnice_x, "a", rovnice_y, "nesplňují rovnost")
