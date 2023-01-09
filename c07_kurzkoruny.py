# Nasimulujte minutu po minutě kurz koruny k euru 
# prvních dvacet minut po opuštění kurzového závazku ČNB. 
# Bude oscilovat mezi 26 (včetně) a 28 (ne včetně) Kč/Euro. 
# V MsgBoxu je vypište (pomocí Mod)  tak, že budou vždy po pěti na řádku 
# (oddělené tabulátorem či čárkou nebo mezerou). Vypište s dvěma desetinnými čísly.
import random
from random import randint

for i in range(1,21):
    x = random.randint(26,28)
    print(i,".min", " = ", x, "CZK")
    

   