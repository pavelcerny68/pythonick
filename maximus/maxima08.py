from typing import ValuesView
import heapq

values = [10, 23, 72, 110, 773, 322, 63, 1, 34, 5, 10]
print(f"The maximum values in order are {heapq.nlargest(5, values)}") # 5 nejvetsich cisel