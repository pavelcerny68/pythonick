# Napište funkci, které se předá rok (čtyřciferný)
# a která vrací logickou hodnotu „True“, pokud je rok
# přestupný (má 366 dní místo 365). Pro jednoduchost
# stačí řešit podle Juliánského kalendáře a také podle
# gregoriánského kalendáře  Potřebná teorie:
# Podle Juliánského kalendáře jsou přestupné roky ty,
# které jsou dělitelné čtyřmi Modifikace programu:
# funkce, která místo True-False bude vracet přímo
# délku roku (tedy 365 nebo 366), tedy celočíselný datový typ.

# juliánský kalendář
def je_prestupny(rok):
    if rok % 4 == 0:
        return 366
    else:
        return 365


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(je_prestupny(2023))
print(je_prestupny(2020))
print(je_prestupny(2021))
print(je_prestupny(1900))
print(je_prestupny(1600))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# gregoriánský kalendář
def je_prestupny(rok):
    if rok % 400 == 0:
        return 366
    elif rok % 100 == 0:
        return 365
    elif rok % 4 == 0:
        return 366
    else:
        return 365


print(je_prestupny(2023))
print(je_prestupny(2020))
print(je_prestupny(2021))
print(je_prestupny(1900))
print(je_prestupny(1600))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 365
# 366
# 365
# 366
# 366
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 365
# 366
# 365
# 365
# 366
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
