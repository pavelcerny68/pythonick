# Sestavte program, který se zeptá na délku běžecké trati v metrech
# a poté na čas běžce na této trati ve vteřinách. Poté zobrazí,
# jakou průměrnou rychlostí v [km/hod] běžec běžel

delka_m = int(input("Zadej délku běžecké trati v metrech: "))
cas_bezce = int(input("Zadej za jakou dobu běžec trať uběhl ve vteřinách: "))

rychlost_bezce = delka_m / cas_bezce
# 6.25 m/s
kmh = rychlost_bezce * 3.6

print("Rychlost běžce: ", rychlost_bezce, "m/s  a to je:", kmh, "km/h")
