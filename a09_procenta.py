# Z klávesnice se zadá očekávaný a skutečný příjem. Počítač oznámí, kolika procent bylo dosaženo

o = int(input("Zadej očekávaný příjem peněz: "))
r = int(input("Zadej reálný příjem peněz: "))
procent = ((r - o) / o) * 100

print("Nárust byl v procentech", abs(procent))
