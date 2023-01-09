# Funkci se předá znak a funkce vrátí řetězec:
# „malé písmeno“, „velké písmeno“, „číslice“, „ostatní“.


def poznejZnak(znak):
    asci = ord(znak)
    if asci >= 97 and asci <= 122:
        return "malé písmeno"
    elif asci >= 65 and asci <= 90:
        return "velké písmeno"
    elif asci >= 48 and asci <= 57:
        return "číslice"
    else:
        return "neznámý znak"


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(poznejZnak("c"))  # vytiskne "malé písmeno"
print(poznejZnak("Q"))  # vytiskne "velké písmeno"
print(poznejZnak("2"))  # vytiskne "číslice"
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(poznejZnak("@"))  # vytiskne "neznámý znak"
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# def poznejZnak(znak):
#     if znak.islower():
#         return "malé písmeno"
#     elif znak.isupper():
#         return "velké písmeno"
#     elif znak.isdigit():
#         return "číslice"
#     else:
#         return "NEZNÁMÝ ZNAK"

# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(poznejZnak("c"))  # vytiskne "malé písmeno"
# print(poznejZnak("Q"))  # vytiskne "velké písmeno"
# print(poznejZnak("12"))  # vytiskne "číslice"
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(poznejZnak("@"))  # vytiskne "ostatní"
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# def poznejZnak(znak):
#     if "a" <= znak <= "z":
#         return "malé písmeno"
#     elif "A" <= znak <= "Z":
#         return "velké písmeno"
#     elif "0" <= znak <= "9":
#         return "číslice"
#     else:
#         return "ostatní"


# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(poznejZnak("c"))  # vytiskne "malé písmeno"
# print(poznejZnak("Q"))  # vytiskne "velké písmeno"
# print(poznejZnak("12"))  # vytiskne "číslice"
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(poznejZnak("@"))  # vytiskne "ostatní"
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# def poznejZnak(znak):
#     asci = ord(znak)
#     if 97 <= asci <= 122:
#         return "malé písmeno"
#     elif 65 <= asci <= 90:
#         return "velké písmeno"
#     elif 48 <= asci <= 57:
#         return "číslice"
#     else:
#         return "ostatní"


# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(poznejZnak("c"))  # vytiskne "malé písmeno"
# print(poznejZnak("Q"))  # vytiskne "velké písmeno"
# print(poznejZnak("2"))  # vytiskne "číslice"
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(poznejZnak("@"))  # vytiskne "ostatní"
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
