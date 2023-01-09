# Vytvořte program, který táhne 5 čísel Sportky (čísla 1 až 49).
# Čísla se (na rozdíl od Sportky) mohou opakovat

import random

num_list = random.sample(range(1, 50), 5)
print(num_list)
