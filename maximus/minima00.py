def min2(x, y):
    if x < y:
        return x
    else:
        return y


def min3(x, y, z):
    return min2(min2(x, y), z)


print(min2(23, 42))
print(min3(62, 95, 6))
# 23
# 6
