class Sort(object):
    def __init__(self, list):
        self.to_sort = list
        list[0] = 100
        self.to_sort[-1]=200
        print(list)
        print(self.to_sort)
li = [i for i in range(1,10)]
# li2 = list(li)
# li2[1] = -100
# li_sort = Sort(li)
# print li_sort.to_sort
# print li
# print li2

f=open('field.html', 'r')
iter = iter(f)

while(1):
    try:
        line = iter.next()
        print line
    except StopIteration:
        print "stop"
        break