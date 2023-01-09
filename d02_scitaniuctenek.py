# Máte schované účtenky z různých nákupů, nevíte ale,
# kolik účtenek je. Proto částky na účtenkách budete
# zadávat postupně, jako poslední zadáte nulu.
# Program spočítá, kolik jste utratili a zároveň oznámí,
# kolik nákupů přesáhlo částku 100 Kč.

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
celkem = 0
nakupyNad100 = 0
while True:
    cena = float(input("Zadejte částku na účtence: "))
    if cena == 0:
        break

    celkem += cena
    if cena > 100:
        nakupyNad100 += 1
print("Celkem jste utratili {} Kč.".format(celkem))
print("Počet nákupů přesahujících 100 Kč: {}".format(nakupyNad100))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
