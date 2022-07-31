def maxN( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max

print(maxN([1, 2, -8, 5, 9, 100, 25, 132, 44]))
