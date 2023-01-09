# Zadejte rychlost v m/s a převeďte na km/hod

rychl_metr_za_s = int(input("Zadej rychlost v metrech za sekundu: "))
rychl_km_za_h = rychl_metr_za_s * 3.6

print("Rychlost: ", rychl_metr_za_s, "m/s  je ", rychl_km_za_h, "km za hodinu ")
