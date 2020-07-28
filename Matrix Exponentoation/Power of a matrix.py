#Power of matrix arr of size m*m to the power n.
def multiply(a,b):
    c=[[0]*m for i in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(m):
                c[i][j]+=a[i][k]*b[k][j]
    return c

def power(arr,n):
    if n==1:
        return arr
    if n%2!=0:
        return multiply(arr,power(arr,n-1))
    x=power(arr,n//2)
    return multiply(x,x)
    
for _ in range(int(input())):
    m,n=map(int,input().split())
    arr=[]
    for i in range(m):
        arr.append(list(map(int,input().split())))
    ans=power(arr,n)
    print(ans)