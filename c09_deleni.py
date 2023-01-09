# Zadejte z klávesnice celé kladné číslo větší než dvě,
# program vypíše všechny jeho dělitele, nepočítaje 1 a sebe sama
# (použij operátor modulo).
#
# Pokud žádný není, oznámí, že se jedná
# o prvočíslo. Pro kontrolu u čísla 12 jsou dělitele čísla: 2, 3, 4, 6.

# A číslo 13 je prvočíslo. Pozn.: dělitel nějakého čísla, je takové číslo,
# kterým je možno dělit beze zbytku. Takže trojka je dělitelem čísla 12,
# protože se do něj vejde přesně čtyřikrát. Zatímco pětka není dělitelem
# čísla 12, protože se tam vejde dvakrát, ale zůstane zbytek 2.
# Nápověda: Je třeba ve smyčce spočítat počet dělitelů
# tedy při každém nalezení dělitele zvýšit toto počitadlo o jedničku).
# A po smyčce zjistit, zda je počet nulový:
# v tom případě se jedná o prvočíslo.

cis = int(input("Zadáno číslo: "))
lst=[]
for i in range(2, cis+1): 
    if (cis % i) == 0:
        lst.append(i)
        print("Dělitel č. ", cis, " = ", i)
  
# prv = [i for i in range(2, cis) if cis > 1 if cis % i == 0]
# print("dělitelé čísla:", cis, "jsou", prv)
