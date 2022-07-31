values = [10, 23, 72, 110, 773, 322, 63, 1, 34, 5, 10]
maximum = values[0]

for i in values:
    if i > maximum:
        maximum = i

print(f"The maximum value is: {maximum}")