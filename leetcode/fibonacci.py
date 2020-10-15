#recursive solution
def fib(n):
    if (n<=2):
        return 1
    return fib(n-1)+fib(n-2)

#print(fib(6)) #should be 8

#dp solution
def fib_dp(n):
    a = [0]*n
    a[0] = a[1] = 1
    for i in range(2, n):
        a[i] = a[i-1] + a[i-2] 
    #print(a)
    return a

fib_dp(6)