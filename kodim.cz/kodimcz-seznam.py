# rozsah 1--100 ob tri hodnoty 3 === x % 3
vysl = [x for x in range(1, 101) if x % 3 == 0]
print(vysl)
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
# zaindexuj seznam jmen
x = [[i, jmeno] for i, jmeno in enumerate(["petr", "jana", "vlasta", "onyx"])]
print(x)
# [[0, 'petr'], [1, 'jana'], [2, 'vlasta'], [3, 'onyx']]
