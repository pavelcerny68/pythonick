# Tabulka ASCII: zobrazit v  MsgBoxu
# v levém sloupci čísla např. 65 až 100
# a v pravém příslušný znak.
# ord('A') #65
# chr(65) # 'A'
for cisla in range(65, 123):
    print(cisla, " = ", chr(cisla))
# 65  =  A
# 66  =  B
# 67  =  C
# 68  =  D
# 69  =  E
# atd