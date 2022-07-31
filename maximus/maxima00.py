# hledání maxima
pole = [30, 5, 9, 10, 11, 1, 9, 14, 99]

max = pole[0]  # maximální hodnota
min = pole[0]  # minimální hodnota
i = 0  # index procházení polem

for i in pole:
    if i > max:
        max = i

for i in pole:
    if i < min:
        min = i


print("maximální číslo je: ", max, "\n")
print("minimální číslo je: ", min)
