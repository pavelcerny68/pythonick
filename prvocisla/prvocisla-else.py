n = int(input("Zadej číslo: "))
d = 2

while d < n:
    if n % d == 0:
        print("Číslo", n, "je dělitelné", d, "není to prvočíslo")
        break
    d += 1
else:
    print("Číslo", n, "je prvočíslo")
