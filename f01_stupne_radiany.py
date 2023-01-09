# Napište funkci, která převádí stupně a minuty na radiány.
# Proměnné se předávají přes parametry podprogramu,
# v hlavním programu použijte jiné názvy proměnných
# než v podprogramu. Návod: řešte trojčlenkou.
# Plnému kruhu odpovídá 360 stupňů nebo 2 pí radiánů
# přibližně 6,28 radiánů.

import math


def stupne_na_radiany(stupne, minuty):
    # Trojčlenka: převádí stupně a minuty na radiány
    radiany = (stupne + minuty / 60) * (2 * math.pi / 360)
    return radiany


stupne = 180
minuty = 30
vysledek = round(stupne_na_radiany(stupne, minuty), 2)
print(vysledek)
