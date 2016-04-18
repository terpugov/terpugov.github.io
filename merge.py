import time
import random
import numpy as np
from heapq import merge


f = open('text.txt', 'r')
list = f.read()
f.close()
list = list.split(',')
list = np.array(list, np.int16).tolist()
#list = range(10)
#random.shuffle(list) # random.shuffle(list)


start = time.time()
def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))



print(merge(list))
print (time.time()-start)








