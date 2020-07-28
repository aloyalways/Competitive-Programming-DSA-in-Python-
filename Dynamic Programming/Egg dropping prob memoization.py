import sys
def eggDroppingProb(e,f):
    t=[[-1]*(f+1) for _ in range(e+1)]
    ans=sys.maxsize
    if f==0 or f==1:
        return f
    if e==1:
        return f
    if t[e][f]!=-1:
        return t[e][f]
    for k in range(1,f+1):
        temp=1+max(eggDroppingProb(e-1,k-1),eggDroppingProb(e,f-k))  #Max is used for worst case
        if temp<ans:
            ans=temp #Min used for minimum number of effects
    t[e][f]=ans
    return ans
        
e=3
f=5
print(eggDroppingProb(e,f))