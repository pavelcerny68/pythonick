# Uživatel opakovaně zadá znak, program vždy odpoví,
# zda se jedná o písmeno, číslici nebo jiný znak.
# Zadávání končí zadáním např. nuly
# Řešte pomocí else if

while True:
    znak = input("Zadejte znak: ")
    if znak == "0" or znak == 0:
        print("Ukončuji program.")
        break
    elif znak.isalpha():
        print("Znak je písmeno.")
    elif znak.isdigit():
        print("Znak je číslicí.")
    else:
        print("Znak je jiným znakem.")
