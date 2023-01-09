# Zadejte částku peněz, které jsou uloženy v bance,
# roční úrok a délku uložení (počet roků).
# Vypočítejte, kolik bude v bance po uplynutí uvedené doby.
# Nepočítejte úroky z úroků.
# Modelový příklad: 1000 Kč na 2 roky s úrokem 1 % ročně = 1020 Kč

penize_v_bance = 1000
rocni_urok_procenta = 1 / 100
doba_ulozeni = 2
novy_zustatek = penize_v_bance + (doba_ulozeni * (penize_v_bance * rocni_urok_procenta))

print("Po roce mám v bance: ", novy_zustatek)
