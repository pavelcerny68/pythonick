# Zadejte několik čísel, ukončete nulou.
# Potom zadáte některé z předtím zadaných čísel.
# Program vypíše, kolikrát toto číslo předtím padlo.

seznam_cisel = []
while True:
    cislo = int(input("Zadejte číslo: "))
    if cislo == 0:
        break
    seznam_cisel.append(cislo)

hledane_cislo = int(input("Zadejte hledané číslo: "))
pocet_vyskytu = 0
for cislo in seznam_cisel:
    if cislo == hledane_cislo:
        pocet_vyskytu += 1

print("Číslo", hledane_cislo, "se v zadaném seznamu vyskytuje", pocet_vyskytu, "krát.")
