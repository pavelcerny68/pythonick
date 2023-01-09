# Sestavte program, který postupně načte jméno a výšku prvního žáka,
# a jméno a výšku druhého žáka. Poté zobrazí jméno vyššího z nich.

jm1 = input("Zadej jmeno žáka")
vys1 = input("Zadej výšku žáka")
jm2 = input("Zadej jmeno žáka")
vys2 = input("Zadej výšku žáka")

if vys1 > vys2:
    print("Vyšší z nich je: ", jm1)
else:
    print("Vyšší z nich je: ", jm2)
