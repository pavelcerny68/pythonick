prompt = "Please enter a number from 1 to 20 (20 to stop): "
numbers = []
number = int(input(prompt))

while number != 20:
    numbers.append(number)
    number = int(input(prompt))

print("the maximum value is", max(numbers))