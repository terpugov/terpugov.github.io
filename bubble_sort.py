import random

temp_list1 = []
temp_list2 = []
print list
count = 0
i = 1
while True:
    if count < 9:

        if list[i-1] > list[i]:
            temp_list1 = list[i]
            temp_list2 = list[i-1]
            list[i-1] = temp_list1
            list[i] = temp_list2
            temp_list1 = []
            temp_list2 = []
            i = i + 1
            if i == 9 :
                print "finish"
                i = 1
                count = 0
        else:
            count = count + 1
        print list
        print count
    else:
        break

