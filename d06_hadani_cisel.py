# Sestavte program, který si myslí (náhodně vygeneruje)
# celé číslo z intervalu <1,10>. Pak ho vy hádáte
# (zadáváte z klávesnice), dokud se nestrefíte.
# Počítač vypíše, na který pokus se to podařilo.


import random

cislo = random.randint(1, 10)
pocetPokusu = 0
while True:
    hadaneCislo = int(input("Zadejte hádané číslo: "))
    pocetPokusu += 1
    if hadaneCislo == cislo:
        print(f"Gratuluji, trefili jste se na {pocetPokusu}. pokus!")
        break
    else:
        print("Špatně, zkuste to znovu.")
