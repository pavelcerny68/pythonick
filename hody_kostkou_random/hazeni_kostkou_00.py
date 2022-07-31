import random
from random import randint

print("Na kostce je číslo:  ")

for i in range(10):
	# 10x hoď kostkou
	print(random.randint(1, 6))
	i+=1
