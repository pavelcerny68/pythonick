#hledání maxima
pole = {30, 5, 29, 100, 11, 19, 9, 14}

#poleList = list(pole)  # jde ze SET() udělat LIST() 

max = 0
i = 0

for i in pole:
	if i > max:
		max = i

min = max
for i in pole:
	if i < min:
		min = i

print("maximální číslo je: ", max, "\n")
print("minimální číslo je: ", min)


