import time
import random
import numpy as np
# list = range(1000)
# random.shuffle(list)
f = open('text.txt', 'r')
list = f.read()
f.close()
list = list.split(',')
list = np.array(list, np.int16).tolist()
count = 0
# list = range(10)
# random.shuffle(list)
start = time.time()

for j in range(0, len(list)/2):
    changed = False
    for i in range(1+j, len(list)-j):
        if list[i-1] > list[i]:
            changed = True
            list[i-1],list[i] = list[i], list[i-1]
        # print(i-1,i)
        # print(j,list)

        if list[-i-1] > list[-i]:
            changed = True
            list[-i],list[-i-1] = list[-i-1], list[-i]
        # print(-i-1,-i)
        # print(j, list)
        # print("\n")
    if(not changed):
        break
print (time.time()-start)
print list
