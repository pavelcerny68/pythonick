# Uživatel bude zadávat postupně teploty vody
# s přesností na desetinu stupně. Zadávání ukončí
# zadáním teploty přesahující 100°
# (tato teplota je ale také součástí dat!).
# Zadávání končí, protože pak už voda vyvřela.
# Program zobrazí zadané teploty, minimální teplotu
# a kolikátá v pořadí tato teplota byla.
# A také průměr teplot


teploty = []
while True:
    teplota = float(input("Zadejte teplotu vody: "))
    if teplota > 100:
        break
    teploty.append(teplota)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Zadané teploty:", teploty)
print("Průměrná teplota:", sum(teploty) / len(teploty))

for i, t in enumerate(teploty):
    if t == min(teploty):
        print("Minimální teplota je:", min(teploty), "a byla", i + 1, "v pořadí")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
