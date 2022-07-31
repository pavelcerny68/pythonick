import random


def hodit():
    store = []
    for i in range(20):
        hazim = random.randint(1, 6)
        store.append(hazim)
    return store


hody = hodit()
print(hody)
# cisla = [1, 2, 3, 4, 5, 6]
# for x in range(20):
#     print(random.choice(cisla))
