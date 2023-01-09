# Zadejte v jednom cyklu řadu čísel. V dalších cyklech program poté
# spočítá jejich součet, průměr, maximum, minimum.
# Pak se program ještě zeptá, zda chcete zobrazit
# součet druhých mocnin.


cisla = []

while True:
    cislo = input("Zadejte číslo (pro ukončení zadávání zadejte 'konec'): ")
    if cislo.lower() == "konec":
        break
    else:
        cisla.append(int(cislo))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
sum = 0
for cislo in cisla:
    sum += cislo
print(f"Součet zadaných čísel je: {sum}")

prumer = sum / len(cisla)
print(f"Průměr zadaných čísel je: {prumer:.2f}")

max = cisla[0]
for cislo in cisla:
    if cislo > max:
        max = cislo
print(f"Maximum čísla je: {max}")

min = cisla[0]
for cislo in cisla:
    if cislo < min:
        min = cislo
print(f"Minimum čísla je: {min}")

soucetDruhychMocnin = 0
for cislo in cisla:
    soucetDruhychMocnin += cislo**2
print(f"Součet druhých mocnin všech zadaných čísel je: {soucetDruhychMocnin}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
