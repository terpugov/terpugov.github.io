import time
import random
import numpy as np
from heapq import merge

#
# f = open('text.txt', 'r')
# list = f.read()
# f.close()
# list = list.split(',')
# list = np.array(list, np.int16)
# print(list, list.size)
# list = range(10)
#random.shuffle(list) # random.shuffle(list)
arr = np.array([1,4,6,7,9,10,11])

start = time.time()
def heapsort(arr):
    for i in xrange(len(arr)/2-1, 0, -1):

        left_leaf = arr[2*i+1]
        if left_leaf > arr[i]:
            arr[2*i+1], arr[i] = arr[i], arr[2*i+1]
        if arr[2*i+2] <= len(arr) and arr[2*i+2] > arr[i]:
            arr[2*i+2], arr[i] = arr[i], arr[2*i+2]
heapsort(arr)
print (time.time()-start)
print arr








