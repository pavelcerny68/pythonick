# Funkce, které se předá číslo 1 až 7
# a vrací slovně den v týdnu. Vytvořte
# variantu s Else if i se Select Case.


def den_v_tydnu(cislo):
    if cislo == 1:
        return "Pondělí"
    elif cislo == 2:
        return "Úterý"
    elif cislo == 3:
        return "Středa"
    elif cislo == 4:
        return "Čtvrtek"
    elif cislo == 5:
        return "Pátek"
    elif cislo == 6:
        return "Sobota"
    elif cislo == 7:
        return "Neděle"
    else:
        return "Nezadal jsi správné číslo dne 1-7"


print(den_v_tydnu(1))  # vrátí "Pondělí"
print(den_v_tydnu(5))  # vrátí "Pátek"
print(den_v_tydnu(7))  # vrátí "Neděle"
print(den_v_tydnu(0))  # vrátí "Neplatný den"
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def den_v_tydnu(cisloDne):
    den = ""
    switcher = {
        1: "Pondělí",
        2: "Úterý",
        3: "Středa",
        4: "Čtvrtek",
        5: "Pátek",
        6: "Sobota",
        7: "Neděle",
    }
    den = switcher.get(cisloDne)
    return den


print(den_v_tydnu(1))
print(den_v_tydnu(7))
print(den_v_tydnu(0))  # špatné číslo dne
