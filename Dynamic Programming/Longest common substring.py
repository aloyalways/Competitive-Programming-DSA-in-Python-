def lcs(X,Y,n,m):
    t=[[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j]=0
            elif X[i-1]==Y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=0
    ans = list(map(max, t))
    return max(ans)

X="ABCDGH"
Y="ACDGHR"
print(lcs(X,Y,len(X),len(Y)))