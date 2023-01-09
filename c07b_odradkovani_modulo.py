# Ve smyčce for jdoucí od 1 do 20 vypisujte počitadlo 
# (tedy postupně 1 až 20). 
# Ale ne všechna čísla na jednom řádku nebo všechna 
# čísla pod sebou, nýbrž takto:
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15 
# 16 17 18 19 20
# Odřádkování řešte pomocí operátoru Mod. 
# Tedy zeptáte se, zda je právě pořadí čísla dělitelné pěti. 
# A pokud ano, tak odřádkujete.

for x in range(1, 21):
    if x % 5 == 0:
        print(x, "\n")
    else: 
        print(x, end=" ")    

#jina verze        
# for x in range(1, 21):
#     if x == 5 or x == 10 or x == 15 or x == 20:
#         print(x,"\n")
#     else: 
#         print(x, end=" ")    

    