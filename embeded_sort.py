import time
import random
import numpy as np
f = open('text.txt', 'r')
list = f.read()
f.close()
list = list.split(',')
list = np.array(list, np.int16).tolist()
start = time.time()
list.sort()
print (time.time()-start)