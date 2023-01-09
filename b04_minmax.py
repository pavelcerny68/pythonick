# Zadejte tři čísla, počítač zjistí, které je největší a které nejmenší.
# Aby program nebyl příliš dlouhý, tak nemusíte uvažovat případy,
# že by nějaká dvě čísla byla stejně velká.
# Tento program je těžší, můžete jej nechat na později.

x = int(input("Zadej první číslo: "))
y = int(input("Zadej první číslo: "))
z = int(input("Zadej první číslo: "))

mini = min(x, y, z)
maxi = max(x, y, z)

print(mini)
print(maxi)

print("############################")

pole = [x, y, z]
pole.sort()
print(pole)

print("max = ", pole[2])
