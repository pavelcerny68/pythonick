import sys

celkem = int(sys.argv[1])
hodin = celkem // 60
minut = celkem % 60
print(str(hodin) + ":" + str(minut))
# spustit pres CMD --> python kodimcz-kolik_hodin_minut.py 450 --> 7:30
