# Upravte program pro Sportku (c3) tak, aby se tažená
# čísla nemohla opakovat. Testujte na větším počtu tahů,
# aby se opakování projevilo. Ještě lépe se projeví,
# pokud budete testovat na hodech kostkou (1-6),
# také nemá padnout stejné číslo dvakrát. Srovnejte s e2):
# tam se zjišťuje, kolikrát které číslo padlo. A nyní se má
# zajistit, aby vícekrát nepadlo. Pokud padne, hod se opakuje.
# Tento program je dost obtížný. Pokud zabere neúměrně hodně času,
# tak jej nechte až na druhou etapu přípravy, tedy po prvním vstupním testu.

import random

cisla = []
pocetCisel = 20

for cis in range(pocetCisel):
    cislo = random.randint(1, 49)
    if cislo not in cisla:
        cisla.append(cislo)
        print(cislo)
    else:
        continue
