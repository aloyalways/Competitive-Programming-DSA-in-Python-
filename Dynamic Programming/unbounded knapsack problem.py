def knapsack(val,wt,W,n):
    t = [[None]*(W+1) for x in range(n+1)] 
    for i in range(n+1): 
        for j in range(W+1): 
            if i==0 or j==0: 
                t[i][j] = 0
            elif wt[i-1] <= j: 
                t[i][j] = max(val[i-1] + t[i][j-wt[i-1]], t[i-1][j]) 
            else: 
                t[i][j] = t[i-1][j] 
    print(t[n][W]) 

val=[60,100,120]
wt=[10,20,30]
W=50
n=len(val)
knapsack(val,wt,W,n)
