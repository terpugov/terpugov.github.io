"python3"
#import time
n = int(input())
#start = time.time()
#def reqursiveFibonachi(n):
#    if n <=1:
#        return n
#    else:
#        retur5n reqursiveFibonachi(n-1)+reqursiveFibonachi(n-2)
#print(reqursiveFibonachi(n),'reqursiveFibonachi')
#print (time.time()-start)
#start = time.time()
def Fibonachi(n):
    fib = [0,1,1]
    if n < len(fib):
        return fib[n]
    else:
        i = 2
        while i < n:
            last_N = (fib[i]+fib[i-1])%10
            fib.append(last_N)
            i = i + 1

    return fib[i]
print(Fibonachi(n))
#print (time.time()-start)
