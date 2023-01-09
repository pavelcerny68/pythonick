# Počítač se zeptá:  "Chcete skončit?  (A/N)"
# Při stisku A program skončí, při stisku čehokoliv
# jiného se vypíše "A stejně skončím!" a program skončí.

konec = input("Chcete skončit?  ")

if konec == "A":
    print("konec")

if konec != "A":
    print("A stejně skončím")
