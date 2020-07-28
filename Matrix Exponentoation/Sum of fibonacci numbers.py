#Sum of Fibonacci Numbers is S(n)=F(n+2)-1
def fib(n):
    F=[[1,1],[1,0]]
    if n==0:
        return 0
    power(F,n-1)
    return F[0][0]
    
def power(F,n):
    if n==0 or n==1:
        return
    M=[[1,1],[1,0]]
    power(F,n//2)
    multiply(F,F)
    if n%2!=0:
        multiply(F,M)
        
def multiply(F,M):
    a=(F[0][0]*M[0][0]+F[0][1]*M[1][0])
    b=(F[0][0]*M[0][1]+F[0][1]*M[1][1])
    c=(F[1][0]*M[0][0]+F[1][1]*M[1][0])
    d=(F[1][0]*M[0][1]+F[1][1]*M[1][1])
    
    F[0][0]=a
    F[0][1]=b
    F[1][0]=c
    F[1][1]=d

for _ in range(int(input())):
    n=int(input())
    x=fib(n+2)-1
    print(x)
        