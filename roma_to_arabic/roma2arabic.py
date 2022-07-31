# -*- coding: utf-8 -*-
import roman

# 2x budeš zadávat vstup z klávesnice
rok = int(input("Vlož české čísla = např. rok:  "))
print(roman.toRoman(rok))

rim = input("Vlož římské číslice = např. MDCLXI  ")
# pismena 'MDCL' v uvozovkach
pismena = rim.upper()
print(roman.fromRoman(pismena))
