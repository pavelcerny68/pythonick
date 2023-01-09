# Uživatel zadá znak, program odpoví, zda se jedná o velké písmeno,
# malé písmeno, číslici nebo jiný znak. Řešte pomocí else if.
# (nebo je možno řešit i složenou podmínkou). U písmen uvažujte
# jen písmena anglické abecedy (tedy bez háčků a čárek).
# Řešte intervalem (čili od-do), tedy využijte toho,
# že číslice jsou v ASCII za sebou seřazeny podle hodnoty
# (podobně velká písmena seřazená podle anglické abecedy
# a stejně tak i malá písmena). Tedy neřešte výčtem
# (vyjmenováním jednotlivých písmenek)

z = input("Zadej písmeno abecedy -malé či velké: ")
znak = ord(z)
# print(znak)

if znak > 96 and znak < 123:
    print("zadal jste malé písmeno", z)
else:
    print("zadal jste velké písmeno", z)
