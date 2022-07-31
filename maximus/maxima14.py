def findMax(num):
  rem = 0
  while(num):
    rem = num%10
    return rem

print('Number with max remainder is:', max(11,48,33,17,19, key=findMax))


num = [11,48,33,17,19]
print('Number with min remainder is:', min(num, key=findMax))

# ('Number with max remainder is:', 19)
# ('Number with min remainder is:', 11)