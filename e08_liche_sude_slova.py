# Zadejte postupně do pole několik různých slov.
# Každé slovo přitom budete zadávat zvlášť. Poté
# znovu zadejte jedno z těchto slov. Program vypíše
# číslo pořadí, v jakém bylo toto slovo zadáno
# (na jaké pozici se vyskytuje v poli).
# Řadu slov z předchozího příkladu vypište
# v obráceném pořadí, a pak vypište pouze sudá
# a pak pouze lichá slova.


### SUDÉ I LICHÉ SLOVO JE URČOVÁNO POZICI (PRVNÍ, TŘETÍ..HODNOTY)
slova = []

while True:
    slovo = input("Zadejte slovo: ")
    if slovo == "":
        break
    slova.append(slovo)

print("Seznam slov:", slova)
hledane_slovo = input("Zadejte slovo pro vyhledání: ")

for i, slovo in enumerate(slova):
    if slovo == hledane_slovo:
        print("Pořadí slova '%s' je %d." % (hledane_slovo, i + 1))
        break

print("Seznam slov v obráceném pořadí:", slova[::-1])
print("Sudá slova:", [slovo for i, slovo in enumerate(slova) if i % 2 == 1])
print("Lichá slova:", [slovo for i, slovo in enumerate(slova) if i % 2 == 0])
