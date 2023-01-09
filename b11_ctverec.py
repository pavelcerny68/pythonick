# Zadejte dvě kladná čísla, která představují délky stran obdélníka.
# Zjistěte, zda se jedná o čtverec a zobrazte zprávu ve tvaru:
# "Čtverec má dálku strany..." nebo "Obdélník má rozměry ... x ..."

a = int(input("Zadej délku 1. strany obdélníka: "))
b = int(input("Zadej délku 2. strany obdélníka: "))

if a == b:
    print("Jedná se o čtverec - délka strany je: ", a)
else:
    print("Jedná se o obdélník - rozměry jsou: a=", a, "b=", b)
