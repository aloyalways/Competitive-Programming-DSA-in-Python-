def knapsack(val,wt,W,n):
    t = [[-1]*(W+1) for _ in range(n+1)]
    if n==0 or W==0:
        return 0
    if t[n][W]!=(-1):
        return t[n][W]
    if wt[n-1]<=W:
        t[n][W]=max(val[n-1]+knapsack(val,wt,W-wt[n-1],n-1),knapsack(val,wt,W,n-1))
        return t[n][W]
    else:
        t[n][W]=knapsack(val,wt,W,n-1)
        return t[n][W]

val=[60,100,120]
wt=[10,20,30]
W=50
n=len(val)
print(knapsack(val,wt,W,n))
