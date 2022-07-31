id_number = input("Zadejte rodné číslo: ")
year_of_birth = id_number[0] + id_number[1]
year_of_birth = int(year_of_birth)
if year_of_birth > 20:
    year_of_birth = 1900 + year_of_birth
else:
    year_of_birth = 2000 + year_of_birth
print(f"Uživatel(ka) se narodil(a) v roce {year_of_birth}.")
print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

sales = 0
for item in books:
    sales += item["sold"]
    sales += item["sold"] * item["price"]
print(f"Celkové tržby jsou {sales} Kč.")
print(f"Celkem bylo prodáno {sales} knih.")

for item in books:
    if item["year"] == 2019:
        sales += item["sold"] * item["price"]
print(f"Celkové tržby za knihy prodané v roce 2019 jsou {sales} Kč.")
