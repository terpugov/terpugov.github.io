"python3"
#import time
s = input()

lst = s.split()
a = int(lst[0])
b = int(lst[1])
#start = time.time()
#def reqursiveFibonachi(n):
#    if n <=1:
#        return n
#    else:4
#        return reqursiveFibonachi(n-1)+reqursiveFibonachi(n-2)
#print(reqursiveFibonachi(n),'reqursiveFibonachi')
#print (time.time()-start)
#start = time.time()
def gcd(a,b):
    if b == 0:
        return a
    else:
        a1 = a%b
        return gcd(b,a1)






print(gcd(a,b))
#print (time.time()-start)
