# Zadejte první, druhy a poslední
# len lineární celočíselné posloupnosti
# (lineární posloupnost je taková, kde mezi jednotlivými
# členy jsou stejné odstupy, např. 12, 15, 18, 21...).
# Program zobrazí pod sebou všechny prvky posloupnosti.
# Pozn.: program musí fungovat, i kdyby třetí zadané číslo
# se nestrefilo do členů posloupnosti (tedy kdyby toto číslo nebylo
# v posloupnosti obsaženo). Takže je to třeba chápat spíše tak,
# že třetí zadané číslo je limit.Varianta: Zadá se první
# a druhy krok a počet prvku posloupnosti.


def posloupnost(prvni, druhy, pocet):
    rozdil = druhy - prvni
    posloupnost = []
    clen = prvni
    while len(posloupnost) < pocet:
        posloupnost.append(clen)
        clen += rozdil
    return posloupnost


prvni = 5
druhy = 7
pocet = 10
vysledek = posloupnost(prvni, druhy, pocet)
print(vysledek)
# tisk:  [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
