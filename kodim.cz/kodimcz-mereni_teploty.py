# [radek[0] for radek in mereni] === "po"
# [radek[1] for radek in mereni] === "17.3"
mereni = [
    ["po", 17.3],
    ["út", 16.8],
    ["st", 15.1],
    ["čt", 13.2],
    ["pá", 14.0],
    ["so", 13.9],
    ["ne", 15.8],
]
teploty = [radek[1] for radek in mereni]
te = [radek[0] for radek in mereni]
prumer = sum(teploty) / len(teploty)
rozdily = [abs(t - prumer) for t in teploty]
min_rozdil = min(rozdily)
index = rozdily.index(min_rozdil)

print("teploty-radek1", teploty)
print("teploty-radek1", te)

print("prumer", prumer)
print("rozdily", rozdily)
print("min_rozdil", min_rozdil)
print("index-0", index)

print(
    "Den s teplotou nejblíž průměru je "
    + str(mereni[index][0])
    + " naměřená teplota je:  "
    + str(mereni[index][1])
)
