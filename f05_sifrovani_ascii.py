# Napište šifrovací funkci, které se předá písmeno
# a která vrátí následující písmeno v anglické abecedě.
# Tedy znak, jehož pozice v ASCII tabulce je o jedno
# vyšší S jedinou výjimkou: pro „z“ vrátí „a“.
# doplňte funkci aby předalo číslo n a funkce pak
# v ASCII tabulce se posouvá o n pozic.
# Tedy například pro n=2 převede: a->c, y->a, z->b


def zasifrovat(znak, n):
    kod_znaku = ord(znak)
    posunuty_kod = kod_znaku + n
    if znak.islower():
        if posunuty_kod > 122:
            posunuty_kod -= 26
    elif znak.isupper():
        if posunuty_kod > 90:
            posunuty_kod -= 26
    return chr(posunuty_kod)


print(zasifrovat("a", 2))
print(zasifrovat("y", 2))
print(zasifrovat("z", 2))
# vysledek je
# c, a, b

# funkce zasifrovat, která přijímá písmeno
# a celé číslo n jako vstup a vrací písmeno, které je n pozic
# po něm v abecedě.  ord(znak) převádí znak na jeho ASCII kód.
# Například ord('a') vrátí hodnotu 97, což je ASCII kód
# pro písmeno 'a'. kod_znaku + n posune ASCII kód o n pozic.
# Například pokud  kod_znaku je 97 (kód pro 'a') a n je 2,
# kod_znaku + n vrátí  hodnotu 99, což je kód pro písmeno 'c'.
# Příkazy if a elif # kontrolují, zda je posunutý kód mimo
# rozsah malých  (od 97 do 122 včetně) nebo velkých
# (od 65 do 90 včetně) písmen. Pokud ano, posunutý kód se
# vrací zpět do rozsahu odečtením 26 (počtem písmen v abecedě)
# Nakonec se pomocí chr(posunuty_kod) převede posunutý kód
# zpět na písmeno a vrátí se. Například pokud je posunuty_kod 99,
# chr(posunuty_kod) vrátí 'c'.
