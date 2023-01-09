# Vypište klesající posloupnost čísel od 8 do -8.
# Varianta: vypište stejnou posloupnost,
# ale pouze každé druhé (sudé) číslo. (Nepoužívejte if.)

l = list(range(8, -9, -1))
print(l)
li = list(range(8, -9, -2))
print(li)

print("-----------------")
for x in range(8, -9, -1):
    print(x)
print("-----------------")

# sude
for y in range(8, -9, -2):
    print(y)
