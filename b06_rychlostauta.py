# První auto ujelo trasu s1 za čas t1 a druhé trasu s2 za čas t2.
# (údaje zadejte). Spočítejte průměrnou rychlost obou aut
# a vypište zprávu "... auto je o ... rychlejší".

km1 = int(input("Zadej délku trasy 1. auta v km: "))
tm1 = int(input("Zadej dobu jízdy 1. auta v hod: "))
kmh1 = km1 / tm1

km2 = int(input("Zadej délku trasy 2. auta v km: "))
tm2 = int(input("Zadej dobu jízdy 2. auta v hod: "))
kmh2 = km2 / tm1

if kmh1 > kmh2:
    k1mh = kmh1 - kmh2
    print("Auto č.1 jede rychle ji o: ", k1mh, "km/h rychleji")

else:
    k2mh = kmh2 - kmh1
    print("Auto č.2 jede rychle ji o: ", k2mh, "km/h rychleji")
