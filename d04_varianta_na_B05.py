# Program postupně čte nejprve jméno
# a pak výšku žáka. Prázdné jméno načítání
# ukončuje. Poté zobrazí jméno a výšku nejvyššího žáka.
# Když jsou nejvyšší dva a více stejně vysocí,
# napíše jen jednoho.


vyska = 0
jmenoStudenta = ""

# Načítáme jména a výšky žáků
jmeno = input("Zadejte jméno žáka: ")
while jmeno != "":
    vstup = int(input("Zadejte výšku žáka v cm: "))

    # Pokud je žák nejvyšší, nastavíme ho jako nejvyššího
    if vstup > vyska:
        vyska = vstup
        jmenoStudenta = jmeno

    # Načteme další jméno žáka
    jmeno = input("Zadejte jméno žáka: ")

# Vytiskneme jméno a výšku nejvyššího žáka
print(f"Nejvyšší žák je {jmenoStudenta} s výškou {vyska} cm.")
