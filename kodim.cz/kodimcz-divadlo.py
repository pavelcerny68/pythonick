play = "Každý má svou pravdu"
number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 345
total_price = price_per_ticket * number_of_tickets

print(
    "Cena "
    + str(number_of_tickets)
    + " lístků na hru "
    + play
    + " je celkem "
    + str(total_price)
    + " Kč."
)

print(f"Cena {number_of_tickets} lístků na hru {play} je celkem {total_price} Kč.")
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


number_of_tickets = int(input("Kolik si přejete lístků? "))
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 500:
    discount = 0.1
    total_price = total_price * (1 - discount)
    print(f"Získáváte slevu {discount * 100} %")

print(f"Celková cena nákupu je {total_price} Kč.")
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


items_in_stock = 5
number_of_items = int(input("Kolik si přejete koupit kusů zboží? "))

if number_of_items <= items_in_stock:
    print("Položky byly vloženy do košíku.")
else:
    print(f"Bohužel máme na skladě posledních {items_in_stock} kusů.")
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


points = int(input("Kolik bodů získal student v testu? max 100 "))
if points <= 60:
    mark = 5
elif points <= 70:
    mark = 4
elif points <= 80:
    mark = 3
elif points <= 90:
    mark = 2
else:
    mark = 1
print(f"Známka z testu je {mark}.")
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")


price_per_ticket = 190
age = int(input("Jaký je váš věk? "))
if age >= 18:
    number_of_tickets = int(input("Kolik si přejete lístků? "))
    total_price = number_of_tickets * price_per_ticket
    if total_price >= 1000:
        discount = 0.25
        print(f"Získáváte slevu {discount * 100} %")
    elif total_price >= 500:
        discount = 0.1
        print(f"Získáváte slevu {discount * 100} %")
    else:
        discount = 0
    total_price *= 1 - discount
    print(f"Celková cena nákupu je {round(total_price)} Kč.")
else:
    print("Tento film bohužel není mládeži přístupný.")
