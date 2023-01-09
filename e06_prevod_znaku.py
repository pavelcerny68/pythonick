# Zadejte postupně několik písmen. Program potom
# náhodně vygeneruje slovo (shluk písmen),
# které se bude skládat z těchto písmen (např. vždy 5 znaků).
# Písmena se mohou opakovat a nemusí být použita všechna.
# zadávání můžete ukončit třeba číslem 0 nebo třeba stiskem
# klávesy enter. (Varianta: vygenerujte třeba 10 slov.)
# Varianta: Místo zadání z klávesnice vygeneruje prvotních
# několik písmen počítač.

import random

letters = []

for i in range(5):
    letters.append(chr(random.randint(ord("a"), ord("z"))))

while True:
    letter = input("Zadejte písmeno (pro ukončení zadávání zadejte 'konec'): ")
    if letter.lower() == "konec":
        break
    else:
        letters.append(letter)

for i in range(10):
    word = ""
    for i in range(5):
        word += random.choice(letters)
    print(f"Vygenerované slovo: {word}")
