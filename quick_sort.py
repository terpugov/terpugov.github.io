import time
import random
import numpy as np
f = open('text.txt', 'r')
list = f.read()
f.close()
list = list.split(',')
list = np.array(list, np.int16).tolist()
#list = range(10)
#random.shuffle(list) # random.shuffle(list)


start = time.time()
def quicks(arg):
    list_less = []
    list_equal = []
    list_greater = []

    if len(arg) > 1:
        for i in range(len(arg)):
            if arg[i] < arg[-1]:
                list_less.append(arg[i])
            elif arg[i] == arg[-1]:
                list_equal.append(arg[i])
            else:
                list_greater.append(arg[i])
        list_less = quicks(list_less)
        list_greater = quicks(list_greater)
        return list_less + list_equal + list_greater
    else:
        return arg




print(quicks(list))
print (time.time()-start)








