m = {}

def fib(n):
    f = 1
    if not n in m:
        if n>2:
            f = fib(n-1)+fib(n-2)
        m[n] = f
    else:
        f = m[n]
    return f

#because of recursion this has upperbound of 1000
#print(fib(99))
#print(m)

fibHash = {}

def fibBottemUp(n):
    f = 1
    for k in range(1,n+1):
        if k > 2:
            f = fibHash[k-1] + fibHash[k-2]
        else:
            f = 1
        fibHash[k] = f
    return f

print(fibBottemUp(6666))