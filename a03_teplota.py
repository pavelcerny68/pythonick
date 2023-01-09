# Zadejte teplotu v 6, 12 a 18 hodin. Zobrazí se průměrná denní teplota
t6 = 0
t12 = 0
t18 = 0
prum_teplota = 0

t6 = int(input("Zadej naměřenou teplotu v 6h: "))
t12 = int(input("Zadej naměřenou teplotu ve 12h: "))
t18 = int(input("Zadej naměřenou teplotu v 18h: "))
prum_teplota = (t6 + t12 + t18) / 3

print("Průměrná naměřená teplota je: ", prum_teplota)
