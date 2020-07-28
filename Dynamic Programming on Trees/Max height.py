dp=[0]*100
def dfs(v,u,parent):
    maximum=0
    for child in v[u]:
        if child==parent:
            continue
        dfs(v,child,u)
        maximum=max(maximum,1+dp[child])
    dp[u]+=maximum

def maximumValue(v):
    dfs(v,1,0)
    return dp[7]

n=15
v={} 
for i in range(n + 1): 
    v[i]=[] 
    
v[1].append(2), v[2].append(1) 
v[1].append(3), v[3].append(1)  
v[1].append(4), v[4].append(1)  
v[2].append(5), v[5].append(2)  
v[2].append(6), v[6].append(2)  
v[3].append(7), v[7].append(3)  
v[4].append(8), v[8].append(4)  
v[4].append(9), v[9].append(4)  
v[4].append(10), v[10].append(4)  
v[5].append(11), v[11].append(5)  
v[5].append(12), v[12].append(5)  
v[7].append(13), v[13].append(7)  
v[7].append(14), v[14].append(7)  
v[14].append(15), v[15].append(14)  

print(maximumValue(v))