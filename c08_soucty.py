# Zadej celé kladné číslo a pak program vypíše 
# součet celých čísel od jedné do udaného čísla
cis = int(input("Zadej kladné číslo: "))
soucty = 0

for i in range(1, cis + 1):
    soucty = soucty + i
print(f"součet čísel 1 až", cis, "\nje = ", soucty)

 