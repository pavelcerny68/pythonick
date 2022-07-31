import roman

number = int(input("Vloz ceske cislo = napr. rok:  "))
print(roman.toRoman(number))

numbery = input("Vloz rimske cislice = napr. MDCLXI  ")
print(roman.fromRoman(numbery))


number = int(input("cislo > "))  # 10
n1 = roman.toRoman(number)

print(n1)
print(roman.fromRoman(n1))
