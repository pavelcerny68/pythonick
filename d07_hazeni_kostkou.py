# Program hází kostkou tak dlouho,
# dokud nepadne šestka. Potom vypíše,
# kolik hodů bylo potřeba.

import random

pocetHodu = 0
while True:
    hazeni = random.randint(1, 6)
    pocetHodu += 1
    if hazeni == 6:
        print(f"Padla šestka na {pocetHodu}. hodu!")
        break
    else:
        print("Nepadla šestka, zkuste to znovu.")
