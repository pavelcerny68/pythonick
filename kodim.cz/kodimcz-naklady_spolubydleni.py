# utraty pri spolubydleni a zpusob jak se vyrovnat
import statistics

vydaje = [
    ["Petr", "Prací prášek", 240],
    ["Ondra", "Savo", 80],
    ["Pavla", "Toaleťák", 65],
    ["Zuzka", "Mýdlo", 50],
    ["Pavla", "Závěs do koupelny", 350],
    ["Libor", "Pivka na kolaudačku", 124],
    ["Petr", "Pytle na odpadky", 75],
    ["Míša", "Utěrky na nádobí", 130],
    ["Ondra", "Toaleťák", 120],
    ["Míša", "Pečící papír", 30],
    ["Zuzka", "Savo", 80],
    ["Petr", "Tapeta na záchod", 315],
    ["Ondra", "Toaleťák", 64],
]


seznamJmen = []
utraty = []

for vydaj in vydaje:
    jmeno = vydaj[0]
    utrata = vydaj[2]

    if jmeno in seznamJmen:
        index = seznamJmen.index(jmeno)
        utraty[index] += utrata
    else:
        seznamJmen.append(jmeno)
        utraty.append(utrata)

prumernaUtrata = statistics.mean(utraty)

for jmeno in seznamJmen:
    index = seznamJmen.index(jmeno)
    vyrovnani = round(utraty[index] - prumernaUtrata)

    if vyrovnani > 0:
        print(jmeno + " dostane\t" + str(vyrovnani))
        print()
    else:
        print(jmeno + " má dáti\t" + str(-vyrovnani))
        print()
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
