# Zadejte, kolik je tříd ve škole. Potom postupně zadávejte, 
# kolik je v každé třídě žáků. Program spočítá, kolik je žáků v celé škole 
# a průměrný počet žáků ve třídě.
#-*- coding: utf-8 -*-

pocetTrid = int(input("Zadej počet tříd ve škole: "))
pocetZaku = 0
soucetZaku = 0
i=0
while i <= pocetTrid:
    pocetZaku = int(input("Zadej počet žáků: "))
    soucetZaku += pocetZaku
    i = i + 1
    if i == pocetTrid:
        break

print("V celé škole je:  ", soucetZaku, "žáků \na průměrný počet žáků ve třídě je: ", soucetZaku/pocetTrid)
    
    

