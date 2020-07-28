def SieveOfEratosthenes(n):
    prime=[True for _ in range(n+1)]
    p=2
    while p*p<=n:
        if prime[p]:
            for i in range(p*2,n+1,p):
                prime[i]=False
        p+=1
    prime[0]=False
    prime[1]=False
    for i in range(n+1):
        if prime[i]:
            print(i,end=' ')
    
n=100
print("Prime numbers less than or equal to 100 are: ")
SieveOfEratosthenes(n)