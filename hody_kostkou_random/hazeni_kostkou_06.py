# Vytvor funckiu, ktorá vráti dvojrozmerné pole výskytov hodených čísel.
# Príklad výstupu: [[1, 7], [2, 4], [3, 1], [4, 2], [5, 3], [6, 3]]
# (t.j. jednotku sme hodili sedem krát, dvojku sme hodili štyri krát atď.)

from hod_kostkou_0 import hazej

hazeni = hazej()
print(hazeni)


def dupli(hazeni):
    store = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]
    for hod in hazeni:
        for j in range(len(store)):
            if hod == store[j][0]:
                store[j][1] += +1
    return store


store = dupli(hazeni)
print(store)
