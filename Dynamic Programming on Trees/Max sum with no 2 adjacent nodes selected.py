from collections import defaultdict
dp=[[0]*2 for _ in range(100)]

def dfs(x,parent):
    #two cases for the values
    taking_x,not_taking_x=v[x-1],0
    
    for child in G[x]:
        if child==parent:
            continue
        dfs(child,x)
        taking_x+=dp[child][True]
        not_taking_x+=dp[child][False]
        
    dp[x][True]=not_taking_x #if parent of x is taken, x is not taken
    dp[x][False]=max(taking_x,not_taking_x) #if parent of x is not taken

n=int(input())
v=list(map(int,input().split()))
G=defaultdict(list)
for i in range(n-1):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)
dfs(1,-1)

print(dp[1][False]) #1 never has its "parent" selected.