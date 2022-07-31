import random
from random import randint

randoms = []
r = []

for i in range(10):
    randoms.append((randint(1,100),randint(1,100)))	
    a = randint(5,15)   
    b = randint(10,11)  
    r.append((a,b))
print(randoms)
print("--------------------")
print(r)
