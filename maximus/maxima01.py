
def myMax(list1):
    max = list1[0]
    for x in list1:
        if x > max :
            max = x    	
    return max

list1 = [11, 20, 4, 45, 99]
print("max cislo je: ", myMax(list1))
