# Zadejte několik celých čísel, ukončete nulou. Program v MsgBoxu
# vypíše daná čísla,
# počet, součet, průměr, minimum, maximum. sudá čísla, a jejich počet,
# a vypíše čísla která jsou větší, než první číslo.


cisla = []
cislo = int(input("Zadejte číslo: "))
while cislo != 0:
    cisla.append(cislo)
    cislo = int(input("Zadejte číslo: "))

# Vypočítáme počet čísel
soucet = len(cisla)

# Vypočítáme součet čísel
celkem = sum(cisla)

# Vypočítáme průměr čísel
prumerCisel = celkem / soucet

# Najdeme minimum a maximum
min_cislo = min(cisla)
max_cislo = max(cisla)

# Vytiskneme všechna zadaná čísla
print("Zadaná čísla:", end=" ")
for cislo in cisla:
    print(cislo, end=" ")
print()

# Vytiskneme počet, součet, průměr, minimum a maximum
print(f"Počet: {soucet}")
print(f"Součet: {celkem}")
print(f"Průměr: {prumerCisel:.2f}")
print(f"Minimum: {min_cislo}")
print(f"Maximum: {max_cislo}")

# Vytiskneme sudá čísla a jejich počet
sudeCislo = [cislo for cislo in cisla if cislo % 2 == 0]
pocetSudychCisel = len(sudeCislo)
print(f"Sudá čísla: {sudeCislo}")
print(f"Počet sudých: {pocetSudychCisel}")

# Vytiskneme čísla větší, než první zadané
prvniCislo = cisla[0]
cisloVetsi = [cislo for cislo in cisla if cislo > prvniCislo]
print(f"Čísla větší než {prvniCislo}:   {cisloVetsi}")

# cisla vetsi nez prvni cislo
pocetCiselNadPrvnimCislem = len(cisloVetsi)
print(f"Počet čísel větších než 1. číslo: {pocetCiselNadPrvnimCislem}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
