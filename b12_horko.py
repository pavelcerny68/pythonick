# Program se zeptá, zda je den a zda je horko (odpověď a/n).
# Pouze v případě obou odpovědí kladných vám navrhne jít si zaplavat.
# Použijte jen jeden příkaz IF (ale se složenou podmínkou).
# Jednodušší varianta: předpokládejme, že uživatel bude
# uvědoměle zadávat malá písmena. Složitější varianta: program
# bude reagovat stejně na „a“ i „A“

d = input("Je den?")
t = input("Je horko?")

if d == "a" or d == "A" and t == "a" or t == "A":
    print("Běž si zaplavat")
else:
    print("v noci není zas takové horko.")
