# Úkolem je pro danou dvojici čísel x,y spočítat hodnotu výrazu
# Pokud by ale byl jmenovatel nulový, tak nepočítat (aby nedošlo
# k havárii programu), ale vypsat varovné hlášení

x = int(input("Zadej první číslo: "))
y = int(input("Zadej druhé číslo: "))

if x == 0 or y == 0:
    print("Pozor, jedno z čísel je nulové: x=", x, "y=", y)
else:
    print("Výsledek dělení je: ", x / y)
