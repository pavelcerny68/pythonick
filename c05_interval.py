# Vygenerujte 20 celých náhodných celých čísel v rozsahu 10..50. 
# Zjistěte, o kolik se jejich střední hodnota (průměr) 
# liší od středu intervalu, tedy od 30.
import random
stred = 30
nahoda = (random.sample(range(10, 51, 1), 20))
# od 10 do 50 krok 1, 20 cisel
delenec = (sum(nahoda) / stred)
rozdil = (stred-delenec)
print(nahoda) 
print("soucet vsech cisel =",sum(nahoda),"\n" )
print("soucet cisel / 30  =", round(delenec, 2),"\n")
print("rozdil od 30 je =",round(rozdil, 2))

   
    