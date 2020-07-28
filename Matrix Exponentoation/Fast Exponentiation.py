#Calcuting a^n in O(logn)
def power(a,n):
    if n==0:
        return 1
    elif n==1:
        return a
    else:
        r=power(a,n//2)
        if n%2==0:
            return r*r
        else:
            return r*a*r

a=int(input())
n=int(input())
ans=power(a,n)
print(ans)