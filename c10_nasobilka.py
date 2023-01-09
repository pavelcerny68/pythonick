# Vytvořte program pro zkoušení malé násobilky.
# Program zadává náhodně násobení čísel od 1 do 10,
# např. 5*6=, 8*4= atd. Uživatel napíše výsledek.
# Pokud to je špatně, napíše počítač správný výsledek.
# Celkem 10 příkladů, nakonec se zobrazí počet chyb.


nasob = {}
priklady = (
    "5*3=",
    "8*6=",
    "9*9=",
    "6*2=",
    "2*2=",
    "3*4=",
    "7*7=",
    "5*5=",
    "6*7=",
    "3*9=",
)
vysledky = ("15", "48", "81", "12", "4", "12", "49", "25", "42", "27")


def pocitej():
    for i in priklady:
        while True:
            if i == priklady[0]:
                inp = input(f"kolik je {i} ")
                if inp == vysledky[0]:
                    print("vysledek je OK je to =", vysledky[0])
                    break
                else:
                    print("nachovňo je to =", vysledky[0])
            if i == priklady[1]:
                inp = input(f"kolik je {i} ")
                if inp == vysledky[1]:
                    print("vysledek je OK je to =", vysledky[1])
                    break
                else:
                    print("nachovňo je to =", vysledky[1])
            if i == priklady[2]:
                inp = input(f"kolik je {i} ")
                if inp == vysledky[2]:
                    print("vysledek je OK je to =", vysledky[2])
                    break
                else:
                    print("nachovňo je to =", vysledky[2])
            if i == priklady[3]:
                inp = input(f"kolik je {i} ")
                if inp == vysledky[3]:
                    print("vysledek je OK je to =", vysledky[3])
                    break
                else:
                    print("nachovňo je to =", vysledky[3])
            if i == priklady[4]:
                inp = input(f"kolik je {i} ")
                if inp == vysledky[4]:
                    print("vysledek je OK je to =", vysledky[4])
                    break
                else:
                    print("nachovňo je to =", vysledky[4])
            if i == priklady[5]:
                inp = input(f"kolik je {i} ")
                if inp == vysledky[5]:
                    print("vysledek je OK je to =", vysledky[5])
                    break
                else:
                    print("nachovňo je to =", vysledky[5])
            if i == priklady[6]:
                inp = input(f"kolik je {i} ")
                if inp == vysledky[6]:
                    print("vysledek je OK je to =", vysledky[6])
                    break
                else:
                    print("nachovňo je to =", vysledky[6])
            if i == priklady[7]:
                inp = input(f"kolik je {i} ")
                if inp == vysledky[7]:
                    print("vysledek je OK je to =", vysledky[7])
                    break
                else:
                    print("nachovňo je to =", vysledky[7])
            if i == priklady[8]:
                inp = input(f"kolik je {i} ")
                if inp == vysledky[8]:
                    print("vysledek je OK je to =", vysledky[8])
                    break
                else:
                    print("nachovňo je to =", vysledky[8])
            if i == priklady[9]:
                inp = input(f"kolik je {i} ")
                if inp == vysledky[9]:
                    print("vysledek je OK je to =", vysledky[9])
                    break
                else:
                    print("nachovňo je to =", vysledky[9])

        nasob[i] = inp
    print("-----------------")
    print("tohle jsi počítal ==> \n", nasob)
    print("-----------------")


pocitej()
