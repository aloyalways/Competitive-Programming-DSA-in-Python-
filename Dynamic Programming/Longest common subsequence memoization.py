def lcs(X,Y,n,m):
    t=[[-1]*(m+1) for _ in range(n+1)]
    if n==0 or m==0:
        return 0
    if t[n][m]!=-1:
        return t[n][m]
    elif X[n-1]==Y[m-1]:
        t[n][m]=1+lcs(X,Y,n-1,m-1)
        return t[n][m]
    else:
        t[n][m]=max(lcs(X,Y,n,m-1), lcs(X,Y,n-1,m))
        return t[n][m]

X="abcdgh"
Y="abedfhr"
print(lcs(X,Y,len(X),len(Y)))