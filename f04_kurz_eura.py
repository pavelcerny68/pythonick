# Sestavte funkci Kurs, která má dva parametry:
# prvním je číslo ve významu korun, druhým
# je tříznakový řetězec ve významu kódu měny
# (“EUR“, “USD“, “GBP“), na kterou se tyto
# koruny mají vyměnit. Výsledkem volání funkce
# je částka v dané měně, rovnající se danému
# počtu korun (nebo hodnota -1, jestliže jde
# o měnu, pro kterou není kurs znám). Kurz bude
# ve funkci zadán „natvrdo“, např. 27,35 pro euro.
# Tedy volat se tedy měla např. takto
# MsgBox kurs(273.5, "EUR")
# Vypsat by měla 10. Tedy že 255,3 Kč je 10 Euro.
import math


def kurs(koruny, mena):
    if mena == "EUR":
        return round((koruny / 27.35), 2)
    elif mena == "USD":
        return round((koruny / 25.00), 2)
    elif mena == "GBP":
        return round((koruny / 32.50), 2)
    else:
        return -1


txt1 = "převod na --> euro"
txt2 = "převod na --> dolary"
txt3 = "převod na --> libry"
txt4 = "převod z neznámé měny nakoruny"
print(kurs(628.55, "EUR"))  # vrátí 10.0 převod na €
print(kurs(155.11, "USD"))  # vrátí 10.0 převod na $
print(kurs(132.112, "GBP"))  # vrátí 10.0  převod nd libry
print(kurs(1000, "CZK"), ("---> nezadaná měna"))  # vrátí -1 neví se v jaké měně to je
