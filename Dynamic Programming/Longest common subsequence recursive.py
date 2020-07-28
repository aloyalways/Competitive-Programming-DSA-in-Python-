def lcs(X,Y,n,m):
    if n==0 or m==0:
        return 0
    elif X[n-1]==Y[m-1]:
        return 1+lcs(X,Y,n-1,m-1)
    else:
        return max(lcs(X,Y,n,m-1), lcs(X,Y,n-1,m))

X="abcdgh"
Y="abedfhr"
print(lcs(X,Y,len(X),len(Y)))