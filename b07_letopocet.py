# Uživatel zadá letopočet (od roku 1600).
# Program vrátí název státního útvaru, ve kterém jsme se tehdy
# nacházeli (Rakousko, Rakousko-Uhersko, Československá republika,
# Protektorát Böhmen und Mähren atd.). Řešte pomocí else if.

lp = 0

lp = int(input("Vlož letopočet (1600, 1865, 1918, 1939):  "))

if lp > 1600 and lp <= 1865:
    print("Vznik Rakousko-Uherska")
if lp == 1918:
    print("Vznik Rakouska a Československa")
if lp == 1939:
    print("Protektorát Čechy a Moravy")
