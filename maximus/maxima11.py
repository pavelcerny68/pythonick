bigList = [[1, 3], [6, 8], [2, 22, 4], [7, 10], [1, 5, 2, 6]]

i = 0
j = 0

while i<len(bigList):
    while j<len(bigList[i]):
        print(bigList[i][j])
        j=j+1;
    i=i+1
 