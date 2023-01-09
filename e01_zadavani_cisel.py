# Zadejte řadu čísel ukončenou nulou. Zjistěte nejmenší
# a vypište, kolikrát se v řadě opakuje. (návod: v druhé
# smyčce se najde minimum. A tentokrát bude i smyčka třetí,
# ve které se zjistí, kolikrát se v poli toto minimum vyskytuje).
# Pozn.: lze řešit i dvěma smyčkami, první a druhá se spojí do jedné.
# Tedy čísla se zadávají a hned se zjišťuje, zdali není menší,
# než dosavadní minimum. Pozn.: šlo by to i jednou smyčkou,
# ale to už je náročnější. A nebylo by v tom případě nutné pole.

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
seznam_cisel = []
minimum = float("inf")
pocet_minimum = 0

while True:
    cislo = int(input("Zadejte číslo: "))
    if cislo == 0:
        break
    seznam_cisel.append(cislo)

for cislo in seznam_cisel:
    if cislo < minimum:
        minimum = cislo

for cislo in seznam_cisel:
    if cislo == minimum:
        pocet_minimum += 1

print("Nejmenší číslo je:", minimum)
print("Počet výskytů nejmenšího čísla je:", pocet_minimum)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
