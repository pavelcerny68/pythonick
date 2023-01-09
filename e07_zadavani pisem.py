# Zadejte postupně do pole několik různých slov.
# Každé slovo přitom budete zadávat zvlášť.
# Poté znovu zadejte jedno z těchto slov.
# Program vypíše číslo pořadí, v jakém bylo
# toto slovo zadáno (na jaké pozici se vyskytuje v poli).


slova = []

while True:
    slovo = input("Zadejte slovo: ")
    if slovo == "":
        break
    slova.append(slovo)

hledane_slovo = input("Zadejte slovo, jehož pozici chcete zjistit: ")
pozice = -1
for i, w in enumerate(slova):
    if w == hledane_slovo:
        pozice = i
        break

if pozice == -1:
    print("Slovo se v seznamu nenachází.")
else:
    print(f"Slovo se v seznamu nachází na pozici {pozice + 1}.")
