# slovo = input("Zadejte slovo: ")
slovo = "0> TESTOVACÍ ŘETĚZEC start1> Příliš žluťoučký kůň úpěl ďábelské ódy2> TESTOVACÍ ŘETĚZEC stop!"
delka = len(slovo)
print("testovací řetězec má délku slov: ", delka)
print("---------")
samohlasky = 0
souhlasky = 0
cisla = 0
zvl_znaky = 0
mezery = 0


for znak in slovo:
    if znak in "aáAÁeéěEÉĚiíIÍoóOÓuúůUÚŮ":
        samohlasky = samohlasky + 1
    elif znak in "bBcčCČdďDĎfFgGhHjJkKlLmMnňNŇpPqQrřRŘsšSŠtťTŤvVwWxXzžZŽyýYÝ":
        souhlasky = souhlasky + 1
    elif znak in "0123456789":
        cisla = cisla + 1
    elif znak in "<>=-+*/&#@€$!?_)(~@":
        zvl_znaky += 1
    else:
        pass

mezery = slovo.count(" ")
pocet = int(samohlasky + souhlasky + cisla + zvl_znaky + mezery)

print("samohlásek", samohlasky)
print("souhlásek", souhlasky)
print("čísel", cisla)
print("zvl_znaky", zvl_znaky)
print("mezer", slovo.count(" "))
print("---------")
print("roztříděných znaků je: ", pocet)
