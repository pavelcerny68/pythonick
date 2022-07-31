#  cti ze souboru mereni.txt

with open("mereni.txt", encoding="utf-8") as vstup:
    radky = vstup.readlines()

radky = [radek.split("\t") for radek in radky]
radky = [[radek[0], float(radek[1])] for radek in radky]
print(radky)
# [['po', 17.3], ['út', 16.8], ['st', 15.1], ['čt', 13.2], ['pá', 14.0], ['so', 13.9], ['ne', 15.8]]
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
jmena = ["Roman", "Jana", "Radek", "Petra", "Vlasta"]
jmena = [jmeno + "\n" for jmeno in jmena]
with open("uzivatele.txt", mode="w", encoding="utf-8") as vystup:
    v = str(vystup.writelines(jmena))
print(v)
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
