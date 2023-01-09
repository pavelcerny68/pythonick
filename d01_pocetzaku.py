# 1) Zadejte postupně, kolik je v každé třídě žáků
# (0=konec). Program spočítá, kolik je žáků v celé
# škole a průměrný počet žáků ve třídě. Ověřte,
# že nula do platných dat nepatří. Nesmí se tedy stát,
# že při zadání 30 a 0 (tedy jen jedna třída
# a to s 30 žáky) vyjde průměrný počet žáků 15
# (omylem se uvažovaly dvě třídy,
#  jedna má 30 a druhá 0 žáků)

# -*- coding: utf-8 -*-

pocetTrid = int(input("Zadej počet tříd ve škole: "))
pocetZaku = 0
soucetZaku = 0
i = 0
while i <= pocetTrid:
    pocetZaku = int(input("Zadej počet žáků: "))
    soucetZaku += pocetZaku
    i = i + 1
    if i == pocetTrid and pocetZaku == 0:
        pocetTrid -= 1
        oprava_pocetTrid = pocetTrid
        break

print("V celé škole je:  ", soucetZaku, "žáků"),
print("průměrný počet žáků ve třídě je: ", soucetZaku / oprava_pocetTrid)
