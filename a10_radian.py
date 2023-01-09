# Převeďte úhel zadaný v radiánech na stupně.
# Návod: řešte trojčlenkou. Plnému kruhu odpovídá 360 stupňů
# nebo 2 pí radiánů (přibližně 6,28 radiánů).
# Tedy jeden radián je 180/ = 57,296 stupňů.
# Kdo neví, co jsou radiány, tak tento program nemusí vypracovávat.

radian_stupne = 57.296
radian = int(input("Zadej počet radiánů: "))

print(radian, "radiánů je: ", radian * radian_stupne, "stupňů")
