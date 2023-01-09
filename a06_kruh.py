# Zadejte poloměr kruhu. Vypočítejte obvod (o=2PIr) a plochu (P=PIr2)

r = int(input("Zadej poloměr kruhu v cm: "))
Obvod = 2 * 3.14 * r
Obsah = 3.14 * r * r

print(
    "poloměr kruhu je: ",
    r,
    "cm, obvod kruhu je: ",
    Obvod,
    "cm, obsah kruhu je",
    Obsah,
    "cm2",
)
