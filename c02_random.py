# Program vygeneruje deset náhodných celých čísel (např. od -90 do 100).
# Zjistěte, kolik z nich je v určitém intervalu (např. od 10 do 50)
# S algoritmizací tohoto programu si někteří účastníci nevědí rady.
# Pokud je to i váš případ, tak příklad zkuste nejprve vyřešit bez počítače.

# Vezměte deset malých papírků na poznámky a napište na ně náhodně čísla
# od -90 do +100. Nachystejte si i papír, který nadepíšete např. pocetCiselVIntervalu.
# Potom vezměte první papírek, přečtěte jej,  a pokud je v rozsahu
# mezi 10 a 50, pak na papír nadepsaný pocetCiselVIntervalu napíšete čárku.
# Toto proveďte 10x (tedy na jiný papír, nazvaný index, si děláte čárky
#   a až jich bude 10, tak skončíte). Poté slavnostně oznamte,
# kolik máte čárek na papíru pocetCiselVIntervalu.

import random

nahoda = [random.randrange(-90, 101, 1) for _ in range(10)]
interval = [x for x in nahoda if x > 9 and x < 51]
print(nahoda, "\nIntervalu odpovídají tyto čísla: ", interval)
