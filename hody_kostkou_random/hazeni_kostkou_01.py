from random import randint

pole = []
pocet_hodu = 10
for x in range(pocet_hodu):
    cisla = randint(2,15) 
    pole.append(cisla)
print("Padlo 10 čísel:  ", pole)    

