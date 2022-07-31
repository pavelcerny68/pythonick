largest = 0
while True:
    inp = int(input("Please enter a number from 1 to 20 (20 to stop): "))
    if inp == 20:
        break
    if inp > largest:
        largest = inp
print("The largest number was", largest)