import re

s = 0
a = dict()
b = dict()
r = "MCCXXXIV" #1234

a["CM"] = 900
a["IX"] = 9
a["IV"] = 4
a["XL"] = 40
a["CD"] = 400
a["XC"] = 90

b["M"] = 1000
b["C"] = 100
b["D"] = 500
b["X"] = 10
b["V"] = 5
b["L"] = 50
b["I"] = 1

# Nejprve zpracujte zaludne ctyrky a devitky a odstrante je z retezce.

for key in a:
    if key in r:
        r = re.sub(key, "", r)
        s += a[key]

# Pak rovnou vynasobte ty, ktere nejsou tak zaludne, jejich poctem.

for key in b:
    s += r.count(key) * b[key]

print(s)  # 1234

