# Vygenerujte několik hodů kostkou. Program vypíše,
# kolikrát padla jednotlivá čísla a vyjádří procentuálně.
# Jaký byl průměr? Návod: Dá se to udělat např. tak,
# že si deklaruji šest počitadel, např. pocet1, pocet2 až pocet6.
# A v druhé smyčce bude struktura If-Else s šesti větvemi
# kde se bude zvyšovat o jedničku počitadlo pocet1 nebo pocet2 atd.
# Pro kontrolu: jejich součet musí být roven počtu hodů.
# Až to bude chodit, tak místo šesti proměnných pocet1 až pocet6
# použít pole (nazvané např. pocty). Tedy jedná se o další pole.
# V jednom poli jsou všechny hody a v druhém poli je šest čísel
# s počtem četností jednotlivých hodnot.
# Druhá varianta:
# ověřte, že při zaokrouhlování pomocí Round padají krajní čísla (1 a 6)
# s poloviční četností. Přitom Int pracoval správně,
# všechny hodnoty mají kolem 100/6=16,6 %.

import random

pocet_hodu = int(input("Zadejte počet hodů kostkou: "))
hodnoty = [0, 0, 0, 0, 0, 0]
prumer = 0

for i in range(pocet_hodu):
    hod = round(random.uniform(1, 6))
    hodnoty[hod - 1] += 1
    prumer += hod

prumer = prumer / pocet_hodu
print("Průměrná hodnota hodů kostkou je:", prumer)
for i in range(6):
    procento = hodnoty[i] / pocet_hodu * 100
    print("Číslo", i + 1, "padlo", hodnoty[i], "krát, což je", procento, "%.")
import random
